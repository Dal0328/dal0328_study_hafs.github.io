using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class cView : MonoBehaviour
{
    public Camera lCamera;
    public Camera cCamera;

    public void OnclickcView(){
        cCamera.enabled = true;
        lCamera.enabled = false;
    }
}
