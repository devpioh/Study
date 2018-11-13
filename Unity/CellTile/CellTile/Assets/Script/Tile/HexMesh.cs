using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent(typeof(MeshFilter), typeof(MeshRenderer))]
public class HexMesh : MonoBehaviour 
{
	private Mesh hexMesh;
	private List<Vector3> vertices;
	private List<int> triangles;
	private List<Color> colors;
	private MeshCollider meshCollider;

	private void Awake()
	{
		hexMesh			= new Mesh();
		hexMesh.name	= "Hex Mesh";
		vertices		= new List<Vector3>();
		triangles		= new List<int>();
		colors			= new List<Color>();
		meshCollider	= gameObject.AddComponent<MeshCollider>();

		var filter		= GetComponent<MeshFilter>();
		filter.mesh		= hexMesh;
	}

	public void Triangulate( HexCell[] cells )
	{
		hexMesh.Clear();
		vertices.Clear();
		triangles.Clear();
		colors.Clear();

		for( int i = 0; i < cells.Length; i++ )
		{
			Triangulate( cells[i] );
		}

		hexMesh.vertices	= vertices.ToArray();
		hexMesh.triangles	= triangles.ToArray();
		hexMesh.colors		= colors.ToArray();
		hexMesh.RecalculateNormals();

		meshCollider.sharedMesh = hexMesh;
	}

	private void Triangulate( HexCell cell )
	{	
		for(HexDirection d = HexDirection.NE; d <= HexDirection.NW; d++ )
		{
			Triangulate( d, cell);
		}
	}

	private void Triangulate( HexDirection direction, HexCell cell )
	{
		Vector3 center		= cell.transform.localPosition;
		Vector3 v1			= center + HexMetrics.GetFirstSolidCorner( direction );
		Vector3 v2			= center + HexMetrics.GetSecondSolidCorner( direction );

		AddTriangle( center, v1, v2 );
		AddTriangleColor( cell.color );

		//if( HexDirection.NE == direction )
		if( HexDirection.SE >= direction )
		{
			TriangluateConnection( direction, cell, v1, v2 );
		}

		// Vector3 bridge		= HexMetrics.GetBridge( direction );
		// Vector3 v3			= v1 + bridge;
		// Vector3 v4			= v2 + bridge;

		// AddQuad( v1, v2, v3, v4 );

		// var prevNeighbor	= cell.GetNeighbor( direction.Previous() ) ?? cell;
		// var neighbor		= cell.GetNeighbor( direction ) ?? cell;
		// var nextNeighbor	= cell.GetNeighbor( direction.Next() ) ?? cell;
		// var bridgeColor		= (cell.color + neighbor.color) * 0.5f;

		// AddQuadColor( cell.color, bridgeColor );

		// AddTriangle( v1, center + HexMetrics.GetFirstCorner(direction), v3 );
		// AddTriangleColor( cell.color, (cell.color + prevNeighbor.color + neighbor.color) / 3f, bridgeColor );

		// AddTriangle( v2, v4, center + HexMetrics.GetSecondCorner(direction) );
		// AddTriangleColor( cell.color, bridgeColor, (cell.color + neighbor.color + nextNeighbor.color) / 3f );
	}

	private void TriangluateConnection( HexDirection direction, HexCell cell, Vector3 v1, Vector3 v2 )
	{
		HexCell neighbor	= cell.GetNeighbor( direction );
		if( null == neighbor )
		{
			return;
		}

		Vector3 bridge		= HexMetrics.GetBridge( direction );
		Vector3 v3			= v1 + bridge;
		Vector3 v4			= v2 + bridge;
		v3.y = v4.y	= neighbor.Elevation * HexMetrics.elevationStep;

		AddQuad( v1, v2, v3, v4 );
		AddQuadColor( cell.color, neighbor.color );

		HexCell nextNeighbor = cell.GetNeighbor( direction.Next() );
		if( HexDirection.E >= direction && null != nextNeighbor )
		{
			Vector3 v5	= v2 + HexMetrics.GetBridge( direction.Next() );
			v5.y		= nextNeighbor.Elevation * HexMetrics.elevationStep;

			AddTriangle( v2, v4, v5 );
			AddTriangleColor( cell.color, neighbor.color, nextNeighbor.color );
		}
	}

	private void AddTriangle( Vector3 v1, Vector3 v2, Vector3 v3 )
	{
		int vertexIndex = vertices.Count;
		vertices.Add( v1 );
		vertices.Add( v2 );
		vertices.Add( v3 );
		triangles.Add( vertexIndex );
		triangles.Add( vertexIndex + 1);
		triangles.Add( vertexIndex + 2);
	}

	private void AddTriangleColor( Color color )
	{
		colors.Add( color );
		colors.Add( color );
		colors.Add( color );
	}

	private void AddTriangleColor( Color c1, Color c2, Color c3 )
	{
		colors.Add( c1 );
		colors.Add( c2 );
		colors.Add( c3 );
	}

	private void AddQuad( Vector3 v1, Vector3 v2, Vector3 v3, Vector3 v4 )
	{
		int vertexIndex = vertices.Count;
		vertices.Add(v1);
		vertices.Add(v2);
		vertices.Add(v3);
		vertices.Add(v4);
		triangles.Add( vertexIndex );
		triangles.Add( vertexIndex + 2 );
		triangles.Add( vertexIndex + 1 );
		triangles.Add( vertexIndex + 1 );
		triangles.Add( vertexIndex + 2 );
		triangles.Add( vertexIndex + 3 );
	}

	private void AddQuadColor( Color c1, Color c2 )
	{
		colors.Add( c1 );
		colors.Add( c1 );
		colors.Add( c2 );
		colors.Add( c2 );
	}
}
