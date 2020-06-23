using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
================================================================================================
 - 질량중심 좌표계로 카메라를 변경하는 기능을 구현함
 - Monobehaviour 클래스를 사용함(UnityEngine)
================================================================================================
*/

public class cView : MonoBehaviour
{
    public Camera lCamera;
    public Camera cCamera;

    public void OnclickcView(){
        cCamera.enabled = true; //질량중심 좌표계
        lCamera.enabled = false; //실험실 좌표계
    }
}
