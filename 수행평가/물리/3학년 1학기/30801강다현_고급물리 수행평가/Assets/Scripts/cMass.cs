using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
================================================================================================
 - 각 오브젝트들의 질량과 위치를 곱한 뒤 질량의 총합으로 나누어 질량중심을 구함 
 - Monobehaviour 클래스를 사용함(UnityEngine)
================================================================================================
*/

public class cMass : MonoBehaviour
{
    public GameObject Object1;
    public GameObject Object2;
    public Rigidbody rb_Object1;
    public Rigidbody rb_Object2;
    public GameObject Center;

    void Update() //실행과 동시에 반복하여 실행
    {
        rb_Object1 = Object1.GetComponent<Rigidbody>();
        rb_Object2 = Object2.GetComponent<Rigidbody>();
        //물체1과 물체2의 질량중심을 구함
        Center.transform.position = (rb_Object1.mass*Object1.transform.position+rb_Object2.mass*Object2.transform.position)/(rb_Object1.mass+rb_Object2.mass);
    }
}
