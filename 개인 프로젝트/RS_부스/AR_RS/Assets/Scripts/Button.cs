using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Button : MonoBehaviour
{
    [SerializeField] Text txt_output;
    [SerializeField] GameObject UI;

    public void OnClick1(){
        txt_output.text = txt_output.text+"1";
    }
    public void OnClick2(){
        txt_output.text = txt_output.text+"2";
    }
    public void OnClick3(){
        txt_output.text = txt_output.text+"3";
    }
    public void OnClick4(){
        txt_output.text = txt_output.text+"4";
    }
    public void OnClick5(){
        txt_output.text = txt_output.text+"5";
    }
    public void OnClick6(){
        txt_output.text = txt_output.text+"6";
    }
    public void OnClick7(){
        txt_output.text = txt_output.text+"7";
    }
    public void OnClick8(){
        txt_output.text = txt_output.text+"8";
    }
    public void OnClick9(){
        txt_output.text = txt_output.text+"9";
    }
    public void OnClick0(){
        txt_output.text = txt_output.text+"0";
    }
    public void OnClickC(){
        txt_output.text = txt_output.text.Substring(0,txt_output.text.Length-1);
    }
    public void OnClickE(){
        if (txt_output.text == "0328"){
            UI.SetActive(false);
        }
        else{
            txt_output.text = "";
        }
    }
}
