using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class StartBtn : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Button btn = gameObject.GetComponent<Button>();
        btn.onClick.AddListener(TaskOnClick);
        //btn.GetComponentInChildren<Text>().text = "Start";
    }

    void TaskOnClick()
    {
        string textCheck = gameObject.GetComponent<Button>().name;

        switch (textCheck)
        {

            case "Start":
                SceneManager.UnloadSceneAsync("Main Menu");
                SceneManager.LoadScene("Start");
                break;
            case "Quit":
                Application.Quit();
                break;
            default:
                break;


        }
    }
        // Update is called once per frame
        void Update()
        {

        }

}
