using UnityEngine;

using HexCoord;

public class HexCell : MonoBehaviour
{
    public Hex hex;
    public int index;

    private void OnDrawGizmos() 
    {
        Gizmos.color = Color.red;
        Gizmos.DrawSphere(transform.localPosition, 0.5f);    
    }
}
