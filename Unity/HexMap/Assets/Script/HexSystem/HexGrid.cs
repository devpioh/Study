using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

using HexCoord;
using DevTool;


public class HexGrid : MonoBehaviour
{
    public Canvas debugCanvas;
    public Text cellDebugTextPrefab;
    public HexCell cellPrefab;
    public HexMapMesh holder;
    

    public int row = 1;
    public int col = 1;

    private List<HexCell> hexCells = new List<HexCell>();

    private void Awake() 
    {
        DevLog.ASSERT(null != cellPrefab);
        DevLog.ASSERT(null != holder);

        int index        = 0;
        for(int z = 0; z < col; z++)
        {
            for(int x = 0; x < row; x++)
            {
                hexCells.Add( CreateCell(x, z, index++) );
            }
        }

        holder.Generate(hexCells);
    }

    public HexCell CreateCell(int x, int z, int i)
    {
        var cell        = Instantiate<HexCell>(cellPrefab, holder.transform);

         //[todo] : trick, 축 정렬을 위해 아래와 같이 처리한다. (ex:1 / 2 는 연산하면 0.5f로 나와야 되지만 c#에서는 0 으로 떨어진다.)
        cell.hex        = new Hex(x - z / 2, z);
        cell.index      = i;
        cell.name       = $"[{cell.index.ToString()}] : {cell.hex.ToString()}";

        var pos         = cell.transform.localPosition;
        float col       = x + ((z&1) * 0.5f); // or x + ((z * 0.5f) - z / 2);
        pos.x           = col * (HexMeterices.innerRadius * 2f);
        pos.z           = z * (HexMeterices.outerRadius * 1.5f) ;      

        cell.transform.localPosition = pos;

        CreateDebugText(cell);

        return cell;
    }

    private Text CreateDebugText(HexCell cell)
    {
        var pos         = new Vector3(cell.transform.localPosition.x, cell.transform.localPosition.z, 0f);
        var text        = Instantiate<Text>(cellDebugTextPrefab, debugCanvas.transform);
        text.text       = $"{cell.hex.x.ToString()}\n{cell.hex.y.ToString()}\n{cell.hex.z.ToString()}";
        text.rectTransform.localPosition = pos;

        return text;
    }
}
