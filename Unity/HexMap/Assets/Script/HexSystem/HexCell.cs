using UnityEngine;

using HexCoord;

public class HexCell : MonoBehaviour
{
    public Hex hex;
    public int index;

    public int q => hex.x;
    public int r => hex.z;
    public int s => hex.y;

    public void Init( int row, int col, int index)
    {
        hex         = new Hex(row, col);
        this.index  = index;

        var pos     = transform.localPosition;
        pos.x       = (hex.x + hex.z * 0.5f) * (HexMeterices.innerRadius * 2f);
        pos.z       = hex.z * (HexMeterices.outerRadius * 1.5f);

        transform.localPosition = pos;
        name        = $"[{index.ToString()}] : {hex.ToString()}";
    }

    private void OnDrawGizmos() 
    {
        Gizmos.color = Color.red;
        Gizmos.DrawSphere(transform.localPosition, 0.5f);    
    }
}
