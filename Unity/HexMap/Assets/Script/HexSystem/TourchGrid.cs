using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TourchGrid : MonoBehaviour
{
    private void Update() 
    {
        if( Input.GetMouseButtonUp(0) )
        {
            Ray inputRay = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if(Physics.Raycast(inputRay, out hit) )
                    Tourch(hit.point);
        }
    }

    private void Tourch(Vector3 pos)
    {
        pos = transform.InverseTransformPoint(pos);
        var hex = HexCoord.HexCoordinate.PositionToHex(pos);
        HexCoord.DevLog.Log(pos);
        HexCoord.DevLog.Error( hex.ToString() );
    }
}
