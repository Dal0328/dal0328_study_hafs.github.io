using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;

/*
================================================================================================
 - UI의 시작, 질량 및 속도 설정, 충돌 후 방향 설정(각도 설정) 등의 기능들을 구현함
 - Math와 Monobehaviour 클래스를 사용함(System, UnityEngine)
================================================================================================
*/

public class bStart : MonoBehaviour
{
    //오브젝트 및 변수 지정
    public GameObject Object1;
    public GameObject Object2;
    public GameObject Target1;
    public GameObject Target2;
    public GameObject Cube;
    public Camera lCamera; //실험실 좌표계
    public Camera cCamera; //질량중심 좌표계
    public Text txtObj;
    public Text btxt;
    public InputField InputObject1; //물체1의 질량, 속도
    public InputField InputObject2; //물체2의 질량
    public Rigidbody rb_Object1;
    public Rigidbody rb_Object2;
    public Slider uSlider;
    int speed  = 5;
    bool notPressed = true;
    bool isStart = false;
    bool isCollide = false;
    bool notCal = true;
    bool rotate = true;
    bool cubemv = true;
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

    public void OnclickbStart(){ //시작 버튼을 누르면 작동되는 함수
        if (notPressed){ //시작 상태의 버튼 누를 시 작동
            radian = uSlider.value * Math.PI;
            dCos = Math.Cos(radian);
            tTan = Math.Sqrt((1.0f-dCos)/(1.0f+dCos)); // 2배각 공식을 이용하여 1/2각만큼의 tan값을 구함

            sObject1= InputObject1.text; //오브젝트1의 질량과 속도
            tObject1 = sObject1.Split(new char[] {','});
            mass_Object1 = float.Parse(tObject1[0]);
            velocity_Object1 = int.Parse(tObject1[1]);
            
            sObject2= InputObject2.text; //오브젝트2의 질량
            mass_Object2 = float.Parse(sObject2);
            
            rb_Object1 = Object1.GetComponent<Rigidbody>();
            rb_Object2 = Object2.GetComponent<Rigidbody>();
            rb_Object1.mass = mass_Object1;
            rb_Object2.mass = mass_Object2;

            cubemv = true;

            txtObj.text = "진행 방향의 각도(라디안)\r\n: 0"+"\r\n물체1 질량 : "+tObject1[0]+"\r\n물체1 속력 : "+tObject1[1]+"\r\n물체2 질량 : "+sObject2+"\r\n물체2 속력 : 0";
            btxt.text = "초기화";
            notPressed = false;
        }
        else{ //초기화 상태의 버튼 누를 시 작동
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
        if (cubemv){
            Cube.transform.position = Vector3.MoveTowards(Cube.transform.position,Object1.transform.position,velocity_Object1*speed * Time.deltaTime);
            if(Cube.transform.position.z <= 52.7f){
                cubemv = false;
                isStart = true;
            }
        }
        if(Object1.transform.position.z-Object2.transform.position.z<=5){ //오브젝트의 크기가 5이므로 z값의 차가 5 이하일 때 충돌이라 여기고 작동
            isStart = false;
            isCollide = true;
            //탄성 충돌일 때, 운동량 보존 법칙과 운동에너지 보존 법칙을 고려한 충돌 이후 속도
            lvelocity_Object1 = Math.Sqrt((Math.Pow(velocity_Object1,2))*(1.0f/(1.0f+(mass_Object2/mass_Object1)*(4.0f*(Math.Pow(dCos,2))/(Math.Pow(1.0f-mass_Object2/mass_Object1,2))))));
            lvelocity_Object2 = Math.Sqrt((Math.Pow(velocity_Object1,2)-Math.Pow(lvelocity_Object1,2))*(mass_Object1/mass_Object2));
            txtObj.text = "진행 방향의 각도(라디안)\r\n: "+radian.ToString()+"\r\n물체1 질량 : "+tObject1[0]+"\r\n물체1 속력 : "+lvelocity_Object1.ToString()+"\r\n물체2 질량 : "+sObject2+"\r\n물체2 속력 : "+lvelocity_Object2.ToString();
        }
        if (isStart){ //충돌 전 오브젝트1을 일정한 속도로 오브젝트 2를 향하여 이동
            Object1.transform.position = Vector3.MoveTowards(Object1.transform.position,Object2.transform.position,velocity_Object1*speed * Time.deltaTime);
            
            if (rotate){
                Object1.transform.eulerAngles += new Vector3(2,0,0);
                if(Object1.transform.eulerAngles.x >= 85.0f){
                    rotate = false;
                }
            }
            else{
                Object1.transform.eulerAngles += new Vector3(-2,0,0);
                if(Object1.transform.eulerAngles.x <= -85.0f){
                    rotate = true;
                }
            }
        }
        else if(isCollide){ //충돌 후 작동
            //오브젝트가 충돌 이후 화면 밖으로 벗어날 것을 고려하여 카메라의 고도 점점 높임
            cCamera.transform.position += new Vector3(0.0f,0.1f,0.0f);
            lCamera.transform.position += new Vector3(0.0f,0.1f,0.0f);
            if (notCal){ //방향 설정(타켓 오브젝트 위치시킴)
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
            else{ //타겟 오브젝트 설정 이후 해당 방향으로 오브젝트1,2를 일정한 속도로 이동
                if (rotate){
                    Object1.transform.eulerAngles += new Vector3(2,0,0);
                    Object2.transform.eulerAngles += new Vector3(2,0,0);
                    if(Object1.transform.eulerAngles.x >= 85.0f){
                        rotate = false;
                    }
                }
                else{
                    Object1.transform.eulerAngles += new Vector3(-2,0,0);
                    Object2.transform.eulerAngles += new Vector3(-2,0,0);
                    if(Object1.transform.eulerAngles.x <= -85.0f){
                        rotate = true;
                    }
                }
                Object1.transform.position = Vector3.MoveTowards(Object1.transform.position,Target1.transform.position,Convert.ToSingle(lvelocity_Object1)*speed * Time.deltaTime);
                Object2.transform.position = Vector3.MoveTowards(Object2.transform.position,Target2.transform.position,Convert.ToSingle(lvelocity_Object2)*speed * Time.deltaTime);
            }
        }
    }
}