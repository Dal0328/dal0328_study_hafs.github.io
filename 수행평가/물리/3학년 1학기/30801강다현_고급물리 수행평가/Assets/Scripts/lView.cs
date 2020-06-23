using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class lView : MonoBehaviour
{
    public Camera lCamera;
    public Camera cCamera;

    public void OnclicklView(){
        cCamera.enabled = false;
        lCamera.enabled = true;
    }
}
