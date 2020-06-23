using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

public class bStart : MonoBehaviour
{
    public GameObject Object1;
    public GameObject Object2;
    public GameObject Target1;
    public GameObject Target2;
    public Camera lCamera;
    public Camera cCamera;
    public Text txtObj;
    public Text btxt;
    public InputField InputObject1;
    public InputField InputObject2;
    public Rigidbody rb_Object1;
    public Rigidbody rb_Object2;
    public Slider uSlider;
    int speed  = 5;
    bool notPressed = true;
    bool isStart = false;
    bool isCollide = false;
    bool notCal = true;
    int velocity_Object1;
    float mass_Object1;
    float mass_Object2;
    double radian;
    double dCos;
    double tTan;
    double lvelocity_Object1;
    double lvelocity_Object2;
    string[] tObject1;
    string sObject1;
    string sObject2;

    public void OnclickbStart(){
        if (notPressed){
            radian = uSlider.value * Math.PI;
            dCos = Math.Cos(radian);
            tTan = Math.Sqrt((1.0f-dCos)/(1.0f+dCos));

            sObject1= InputObject1.text;
            tObject1 = sObject1.Split(new char[] {','});
            mass_Object1 = float.Parse(tObject1[0]);
            velocity_Object1 = int.Parse(tObject1[1]);
            
            sObject2= InputObject2.text;
            mass_Object2 = float.Parse(sObject2);
            
            rb_Object1 = Object1.GetComponent<Rigidbody>();
            rb_Object2 = Object2.GetComponent<Rigidbody>();
            rb_Object1.mass = mass_Object1;
            rb_Object2.mass = mass_Object2;

            isStart = true;

            txtObj.text = "진행 방향의 각도(라디안)\r\n: 0"+"\r\n물체1 질량 : "+tObject1[0]+"\r\n물체1 속력 : "+tObject1[1]+"\r\n물체2 질량 : "+sObject2+"\r\n물체2 속력 : 0";
            btxt.text = "초기화";
            notPressed = false;
        }
        else{
            notPressed = true;
            btxt.text = "시작";
            isCollide = false;
            notCal = true;
            Object1.transform.position = new Vector3(0.0f,2.5f,35.0f);
            Object2.transform.position = new Vector3(0.0f,2.5f,0.0f);
            Target1.transform.position = new Vector3(0.0f,2.5f,0.0f);
            Target2.transform.position = new Vector3(0.0f,2.5f,0.0f);
            cCamera.transform.position = new Vector3(0.0f,35.0f,17.5f);
            lCamera.transform.position = new Vector3(0.3f,45.6f,16.5f);
        }
    }

    void Update()
    {
        if(Object1.transform.position.z-Object2.transform.position.z<=5){
            isStart = false;
            isCollide = true;
            lvelocity_Object1 = Math.Sqrt((Math.Pow(velocity_Object1,2))*(1.0f/(1.0f+(mass_Object2/mass_Object1)*(4.0f*(Math.Pow(dCos,2))/(Math.Pow(1.0f-mass_Object2/mass_Object1,2))))));
            lvelocity_Object2 = Math.Sqrt((Math.Pow(velocity_Object1,2)-Math.Pow(lvelocity_Object1,2))*(mass_Object1/mass_Object2));
            txtObj.text = "진행 방향의 각도(라디안)\r\n: "+radian.ToString()+"\r\n물체1 질량 : "+tObject1[0]+"\r\n물체1 속력 : "+lvelocity_Object1.ToString()+"\r\n물체2 질량 : "+sObject2+"\r\n물체2 속력 : "+lvelocity_Object2.ToString();
        }
        if (isStart){
            Object1.transform.position = Vector3.MoveTowards(Object1.transform.position,Object2.transform.position,velocity_Object1*speed * Time.deltaTime);
        }
        else if(isCollide){
            cCamera.transform.position += new Vector3(0.0f,0.1f,0.0f);
            lCamera.transform.position += new Vector3(0.0f,0.1f,0.0f);
            if (notCal){
                notCal = false;
                if (radian==0){
                    Target1.transform.position = Target1.transform.position + new Vector3(0.0f,0.0f,100.0f);
                    Target2.transform.position = Target2.transform.position + new Vector3(0.0f,0.0f,-100.0f);
                }
                else{
                    Target1.transform.position = Target1.transform.position + new Vector3(100.0f*Convert.ToSingle(tTan),0.0f,-100.0f);
                    Target2.transform.position = Target2.transform.position + new Vector3(-100.0f*Convert.ToSingle(tTan),0.0f,-100.0f);
                }
            }
            else{
                Object1.transform.position = Vector3.MoveTowards(Object1.transform.position,Target1.transform.position,Convert.ToSingle(lvelocity_Object1)*speed * Time.deltaTime);
                Object2.transform.position = Vector3.MoveTowards(Object2.transform.position,Target2.transform.position,Convert.ToSingle(lvelocity_Object2)*speed * Time.deltaTime);
            }
        }
    }
}