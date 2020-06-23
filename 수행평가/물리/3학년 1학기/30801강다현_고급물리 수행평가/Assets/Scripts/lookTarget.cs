using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
/*
================================================================================================
 - 질량중심 좌표계의 카메라가 질량 중심을 따라 이동하도록 함
 - Monobehaviour 클래스를 사용함(UnityEngine)
================================================================================================
*/

public class lookTarget : MonoBehaviour
{
    public Transform target;
    private Transform tr;
 
    void Start()
    {
        tr = GetComponent<Transform>();
    }
 
    void LateUpdate()
    {
        //질량중심 카메라의 이동
        tr.position = new Vector3(target.position.x - 0.52f, tr.position.y, target.position.z - 6.56f);
    }
}
