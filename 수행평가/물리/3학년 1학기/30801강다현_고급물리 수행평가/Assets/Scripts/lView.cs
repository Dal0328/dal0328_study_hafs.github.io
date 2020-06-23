using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
================================================================================================
 - 실험실 좌표계로 카메라를 변경하는 기능을 구현함
 - Monobehaviour 클래스를 사용함(UnityEngine)
================================================================================================
*/

public class lView : MonoBehaviour
{
    public Camera lCamera;
    public Camera cCamera;

    public void OnclicklView(){
        cCamera.enabled = false; //질량중심 좌표계
        lCamera.enabled = true; //실험실 좌표계
    }
}
