using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NigerianPrince : MonoBehaviour
{
    public GameObject objectToSpawn;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.G))
        {
            Instantiate(objectToSpawn, transform.position, Quaternion.identity);

        }
    }
}
