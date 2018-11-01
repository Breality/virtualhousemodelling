using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Networking;

public class ButtonHandler : MonoBehaviour {
    public InputField username;
    public InputField password;// Use this for initialization
    public GameObject main_menu;
    public GameObject editing_menu;
    public GameObject warning_sign;
    public Text warning_text;
    public main mainMan;
    string xmlText;
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}


    public void signin()
    {
        string user = username.text;
        string pass = password.text;
        xmlText = "<request><name>authenticateUser</name><username>" + user + "</username><password>" + pass + "</password></request>";
        StartCoroutine(CreateUser());
    }

    public void register()
    {
        string user = username.text;
        string pass = password.text;
        xmlText = "<request><name>createUser</name><username>" + user + "</username><password>" + pass + "</password></request>";
        StartCoroutine(CreateUser());
    }
    IEnumerator CreateUser()
    {

        using (UnityWebRequest www = UnityWebRequest.Post("http://35.0.123.166:9091", xmlText))
        {
            yield return www.SendWebRequest();

            if (www.isNetworkError || www.isHttpError)
            {
                Debug.Log(www.error);
            }
            else
            {
                if(www.downloadHandler.text=="False" && xmlText.Contains("createUser"))
                {
                    Send_user_message("Username take. Please try another.");
                }
                else if (www.downloadHandler.text == "False")
                {
                    Send_user_message("Username or password is incorrect.");
                }
                else
                {
                    main_menu.SetActive(false);
                    editing_menu.SetActive(true);
                    warning_sign.SetActive(false);
                    mainMan.menu = "Designing";
                    //set player id to downloadHandler.text - > cast to long
                }
            }
        }
    }
    public void Send_user_message(string message)
    {
        warning_text.text = message;
        warning_sign.SetActive(true);
    }

}

