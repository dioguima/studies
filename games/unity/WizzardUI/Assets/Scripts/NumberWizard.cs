using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NumberWizard : MonoBehaviour {

    [SerializeField]
    int max = 1000;
    [SerializeField]
    int min = 1;
    int guess = 500;

    // Use this for initialization
    void Start ()
    {
        max += 1;
        NextGuess();
	}
	
    public void OnPressHigher()
    {
        min = guess;
        NextGuess();
    }

    public void OnPressLower()
    {
        max = guess;
        NextGuess();
    }

    void NextGuess()
    {
        guess = (max + min) / 2;
    }
}
