using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotate : MonoBehaviour
{
    public GameObject objectRotate;
    public float rotateSpeed = 19f;

    void Update()
    {
        if(objectRotate.GetComponent<MeshRenderer>().enabled == true){
            if(objectRotate.transform.rotation.y < 0){
                objectRotate.transform.rotation = Quaternion.Euler (new Vector3 (0, 0, 0));
            }
            else if(objectRotate.transform.rotation != Quaternion.Euler (new Vector3 (0, 0, 0))){
                objectRotate.transform.Rotate(Vector3.down, rotateSpeed*Time.deltaTime);
            }
        }
        else{
            objectRotate.transform.rotation = Quaternion.Euler (new Vector3 (0, 42, 0));
        }
    }
}
