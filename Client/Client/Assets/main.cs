using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System;
public class User
{
    public string username;
    public long id;

    public List<Item> items = new List<Item> { };

    public IEnumerator load()
    {
        // make request that loads all items
        yield return 0;
    }

    public IEnumerator save()
    {
        //make request that saves all items
        yield return 0;
    }

    public Item View(GameObject hit)
    {
        Debug.Log("Object hit!");
        foreach (Item item in items)
        {
            Debug.Log(item.reference);
            Debug.Log(hit);
            if (GameObject.ReferenceEquals(item.reference, hit.transform.parent.gameObject))
            {
                item.View();
                return item;
            }
        }
        Debug.Log("None Found");
        return null;
    }

}


public class Item
{
    public Vector3 pos;
    public GameObject reference;
    public long id;
    public List<Material> child_formats = new List<Material> { };
    public Vector3 preMovePos;
    public bool moving = false;
    public string formalName;

    public void move(Vector3 newpos)
    {
        reference.transform.position = newpos;
        pos = newpos;
    }

    public void View()
    {
        for (int a = 0; a < reference.transform.childCount; a++)
        {
            Transform child = reference.transform.GetChild(a);
            child_formats.Add(child.GetComponent<MeshRenderer>().material);
            child.GetComponent<MeshRenderer>().material = main.selected_tint;
        }
    }

    public void unView()
    {
        for (int a = 0; a < reference.transform.childCount; a++)
        {
            Transform child = reference.transform.GetChild(a);
            child.GetComponent<MeshRenderer>().material = child_formats[a];
        }
    }
}

public class main : MonoBehaviour
{
    public string menu = "Account Menu";

    public Storage dbfMan;
    public Transform DaddyFurn;
    public Transform furnStorage;
    public Camera mainCamara;
    public User clientUser;
    public static Material selected_tint;

    private Item currentSelection = null;
    private Item currentView;
    private Quaternion lastRot;

    // Use this for initialization
    void Start()
    {
        //Put back when requests are back (Server is on)
        //StartCoroutine("CreateUser"); 
        clientUser = new User() { id = long.MaxValue, username = "PlaceHolder123" };
    }

    // Update is called once per frame
    void Update()
    {
        if (mainCamara.transform.rotation != lastRot)
        {
            Ray ray = new Ray(mainCamara.transform.position, mainCamara.transform.forward);
            RaycastHit hit;
            if (Physics.Raycast(ray, out hit)) // something was hit!
            {
                Vector3 pos = hit.point;

                if (currentSelection != null)
                { //moved selected item to a new spot, slide it over
                    currentSelection.move(pos + new Vector3(0, -0.03f, 0));
                }
                else
                { //they're browsing, see if they hit anything
                    if (currentView != null && currentView.reference != hit.transform.gameObject) //looking at new item
                    {
                        currentView.unView();

                    }
                    currentView = clientUser.View(hit.transform.gameObject);

                }
            }


        }
        lastRot = mainCamara.transform.rotation;
    }

    public void newSelection(string name)
    {
        if (currentSelection != null)
        {
            GameObject reference = currentSelection.reference;
            currentSelection = null;
            GameObject.Destroy(reference);
        }
        else if (currentView != null)
        {
            currentView.unView();
            currentView = null;

        }

        GameObject furniture = DaddyFurn.Find(dbfMan.name2Model[dbfMan.items[name]["sku"]]).gameObject;
        furniture = Instantiate(furniture, furnStorage);
        furniture.SetActive(true);
        Item furnitureItem = new Item() { reference = furniture, formalName = name };
        currentSelection = furnitureItem;
        Debug.Log(name);

        for (int c = 0; c < furniture.transform.childCount; c++)
        {
            Transform childItem = currentSelection.reference.transform.GetChild(c);
            if ((childItem.name.Contains("plane")))
            {
                childItem.gameObject.SetActive(false);
            }
        }
    }

    public IEnumerator sendEmail(string email, string content)
    {
        string xmlText = "<request><name>sendEmail</name><email>" + email + "</email><message>" + content + "</message></request>";
        using (UnityWebRequest www = UnityWebRequest.Post("http://35.0.123.166:9091", xmlText))
        {
            yield return www.SendWebRequest();

            if (www.isNetworkError || www.isHttpError)
            {
                Debug.Log(www.error);
            }
        }
    }
    public void Command(string command)
    {   //Place, Cancel, Rotate
        if (command == "Email")
        {
            string[] itemHolder = new string[clientUser.items.Count];
            int c = 0;
            foreach (Item item in clientUser.items)
            {
                itemHolder[c] = item.formalName; ;
                c++;
            }

            string emailing = makeEmail(itemHolder);
            string emailed = "noor.nasri@hotmail.com";
            //send email request
            StartCoroutine(sendEmail(emailed, emailing));

        }
        else if (currentSelection != null && command == "Rotate")
        {
            currentSelection.reference.transform.Rotate(new Vector3(0, 90, 0));
        }
        else if ((command == "Place" || command == "Cancel") && currentSelection != null)
        {
            if (command == "Cancel")
            {
                if (currentSelection.moving)
                {
                    currentSelection.move(currentSelection.preMovePos);
                    currentSelection.moving = false;
                    for (int c = 0; c < currentSelection.reference.transform.childCount; c++)
                    {
                        Transform childItem = currentSelection.reference.transform.GetChild(c);
                        if (!(childItem.name.Contains("plane")))
                        {
                            MeshCollider newCollide = childItem.gameObject.AddComponent<MeshCollider>();
                        }
                    }
                }
                else
                {
                    GameObject.Destroy(currentSelection.reference);
                }

            }
            else if (command == "Place")
            {
                for (int c = 0; c < currentSelection.reference.transform.childCount; c++)
                {
                    Transform childItem = currentSelection.reference.transform.GetChild(c);
                    if (!(childItem.name.Contains("plane")))
                    {
                        MeshCollider newCollide = childItem.gameObject.AddComponent<MeshCollider>();
                    }
                }
                //make request for new item
                clientUser.items.Add(currentSelection); // one of the items
            }



            currentSelection = null;
        }
        else if (command == "Move" && currentView != null)
        {
            currentView.preMovePos = currentView.pos;
            currentView.moving = true;
            for (int c = 0; c < currentView.reference.transform.childCount; c++)
            {
                Transform childItem = currentView.reference.transform.GetChild(c);
                if (!(childItem.name.Contains("plane")))
                {
                    Destroy(childItem.gameObject.GetComponent<MeshCollider>());
                }
            }
            currentView.unView();
            currentSelection = currentView;
            currentView = null;
        }
        else if (command == "Destroy" && currentView != null)
        {
            GameObject.Destroy(currentView.reference);
            currentView = null;
            //make request for removing item
        }
    }

    IEnumerator CreateUser()
    {
        string user = "TestDude";
        string pass = "";
        string xmlText = "<request><name>authenticateUser</name><username>" + user + "</username><password>" + pass + "</password></request>";
        using (UnityWebRequest www = UnityWebRequest.Post("http://35.0.123.166:9091", xmlText))
        {
            yield return www.SendWebRequest();

            if (www.isNetworkError || www.isHttpError)
            {
                Debug.Log(www.error);
            }
            else
            {
                menu = "Designing";
                long id = long.Parse(www.downloadHandler.text);
                clientUser = new User() { id = id, username = user };
                yield return clientUser.load();
            }
        }
    }
    public string makeEmail(string[] orderedObjects)
    {
        string string_to_return = "";
        string_to_return += "^*^====================================================================^*^";
        string_to_return += "                        Breality Services Receipt                       ^*^";
        string_to_return += "====================================================================^*^";
        string_to_return += "YOUR ORDER:^*^";
        int orderNum = 1;
        double totCost = 0;
        for (int i = 0; i < orderedObjects.Length; i++)
        {
            string_to_return += "" + orderNum + ")" + orderedObjects[i] + " - $" + dbfMan.items[orderedObjects[i]]["sale_price"] + "^*^";
            string_to_return += "  ->Link: " + dbfMan.items[orderedObjects[i]]["product_page_url"] + "^*^";
            totCost += Double.Parse(dbfMan.items[orderedObjects[i]]["sale_price"]);
            orderNum += 1;
        }
        string_to_return += "====================================================================^*^";
        string_to_return += "RETAIL PRICE: " + totCost + "^*^";
        string_to_return += "====================================================================^*^";

        return string_to_return;
    }
}
