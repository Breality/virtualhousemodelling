using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class CamMovement : MonoBehaviour
{
    private Vector3 rotateValue;
    public main mainScript;
    public GameObject DaddyRoom, DaddyObj;
    Dictionary<KeyCode, Vector3> movements = new Dictionary<KeyCode, Vector3> {
        { KeyCode.RightArrow, new Vector3(0, 0, -1) }, {KeyCode.LeftArrow,  new Vector3(0, 0, 1)}, {KeyCode.UpArrow,  new Vector3(1, 0, 0)},
        { KeyCode.DownArrow,   new Vector3(-1, 0, 0)} };

    /*public Dictionary<string, Dictionary<string, string>> items = new Dictionary<string, Dictionary<string, string>> { };
    private void Start()
    {
        items["Table"] = new Dictionary<string, string> { {"aka","test" }};
    }
    */
    void Update()
    {

        if (mainScript.menu == "Designing")
        { // cam movement
            rotateValue = new Vector3();

            DaddyRoom.transform.position = findPos(DaddyRoom.transform) ;
            
        }
    }
    public Vector3 findPos(Transform trans)
    {
        Ray ray = new Ray(trans.position, transform.forward);
        Vector3 dir = ray.direction;//gets the direction the ray is going to so that the perpendicular normal ray can bbe taken to get the straffe ray.
        Vector3 left = -1 * Vector3.Cross(dir, Vector3.up).normalized;
        Vector3 pos = (ray.GetPoint(Input.GetAxis("Vertical") * 0.025F) - trans.position) + left * Input.GetAxis("Horizontal") * 0.025F;

        pos = trans.position - pos;
        Vector3 minP = new Vector3(275, 155, -18);
        Vector3 maxP = new Vector3(315, 160, 32);
        pos = new Vector3(Mathf.Min(Mathf.Max(minP.x, pos.x), maxP.x), Mathf.Min(Mathf.Max(minP.y, pos.y), maxP.y),
            Mathf.Min(Mathf.Max(minP.z, pos.z), maxP.z));
        return pos;
    }
}