using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using HexCoord;

[RequireComponent(typeof(MeshFilter), typeof(MeshRenderer))]
public class HexMapMesh : MonoBehaviour
{
    private List<Vector3> vertices      = new List<Vector3>();
    private List<int> triangles         = new List<int>();
    private List<Vector2> uvs           = new List<Vector2>();

    private Mesh mesh;

    private void Awake() 
    {
        var filter      = GetComponent<MeshFilter>();
        filter.mesh     = mesh = new Mesh();
        mesh.name       = "Hex Gird Mesh";
    }

    public void Generate(List<HexCell> cells)
    {
        if( null == cells )
            return;

        mesh.Clear();
        vertices.Clear();
        triangles.Clear();
        uvs.Clear();

        for( int i = 0; i < cells.Count; i++ )
        {
            Generate(cells[i]);
        }

        mesh.vertices   = vertices.ToArray();
        mesh.triangles  = triangles.ToArray();
        mesh.RecalculateNormals();
    }

    private void Generate(HexCell cell)
    {
        if( null == cell )
            return;
        
        var center = cell.transform.localPosition;

        for( int i = 0; i < 6; i++ )
            AddTriangle(center, center + HexMeterices.hexCorner[i], center + HexMeterices.hexCorner[i + 1] );
    }

    private void AddTriangle(Vector3 v1, Vector3 v2 , Vector3 v3)
    {
        int index = vertices.Count;

        vertices.Add(v1);
        vertices.Add(v2);
        vertices.Add(v3);

        triangles.Add(index);
        triangles.Add(index + 1);
        triangles.Add(index + 2);
    }
}
