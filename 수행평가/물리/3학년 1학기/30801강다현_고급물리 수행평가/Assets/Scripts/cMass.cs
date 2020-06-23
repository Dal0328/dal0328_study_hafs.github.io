using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class cMass : MonoBehaviour
{
    public GameObject Object1;
    public GameObject Object2;
    public Rigidbody rb_Object1;
    public Rigidbody rb_Object2;
    public GameObject Center;

    void Update()
    {
        rb_Object1 = Object1.GetComponent<Rigidbody>();
        rb_Object2 = Object2.GetComponent<Rigidbody>();
        Center.transform.position = (rb_Object1.mass*Object1.transform.position+rb_Object2.mass*Object2.transform.position)/(rb_Object1.mass+rb_Object2.mass);
    }
}
