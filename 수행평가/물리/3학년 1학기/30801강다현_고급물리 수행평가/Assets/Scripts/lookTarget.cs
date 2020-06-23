using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
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
        tr.position = new Vector3(target.position.x - 0.52f, tr.position.y, target.position.z - 6.56f);
    }
}
