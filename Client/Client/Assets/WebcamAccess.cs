using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class WebcamAccess : MonoBehaviour
{

    static WebCamTexture backCam;
    public RawImage rawimage;


    void Start()
    {
        if (backCam == null)
            backCam = new WebCamTexture();

        //GetComponent<Renderer>().material.mainTexture = backCam;


        if (!backCam.isPlaying) { 
            rawimage.texture = backCam;
            rawimage.material.mainTexture = backCam;
            backCam.Play();
        }
    }

    void Update()
    {

    }
}