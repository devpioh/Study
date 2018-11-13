using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(MeshFilter), typeof(MeshRenderer))]
public class BuildGrid : MonoBehaviour 
{
	public int xSize				= 10;
	public int ySize				= 5;

	private Mesh mesh				= null;
	private Vector3[] gridVertices	= null;
	private int[] gridIndices		= null;

	private void Awake()
	{
		// StartCoroutine( DelayedBuild() );
		Build();
	}

	private IEnumerator DelayedBuild()
	{	
		mesh			= new Mesh();
		gridVertices	= new Vector3[(xSize + 1) * (ySize + 1)];
		gridIndices		= new int[xSize * ySize * 6];
		int index		= 0;
		var wait		= new WaitForSeconds(0.05f);
		var meshFilter	= gameObject.GetComponent<MeshFilter>();
		meshFilter.mesh	= mesh;
		mesh.name		= "grid";
		
		for( int y = 0; y <= ySize; y++ )
		{
			for( int x = 0; x <= xSize; x++ )
			{
				gridVertices[index] = new Vector3( x, y, 0f);
				index++;

				yield return wait;
			}
		} 

		mesh.vertices	= gridVertices;

		int vi = 0;
		int ti = 0;
		int col = 0;
		while( col < ySize )
		{
			int row = 0;
			while( row < xSize )
			{
				gridIndices[ti] = vi;
				gridIndices[ti + 2] = gridIndices[ti + 3] = vi + 1;
				gridIndices[ti + 1] = gridIndices[ti + 4] = vi + xSize + 1;
				gridIndices[ti + 5] = vi + xSize + 2;

				Debug.LogFormat( "row [{0}] : {1}, {2}, {3}, {4}, {5}, {6}", row,
				gridIndices[ti], gridIndices[ti+1], gridIndices[ti+2],
				gridIndices[ti+3], gridIndices[ti+4], gridIndices[ti+5]);

				mesh.triangles = gridIndices;
				yield return wait;
				
				row++;
				ti += 6;
				vi++;
			}

			vi++;
			col++;
		}
	}

	private void Build()
	{
		var meshFilter	= gameObject.GetComponent<MeshFilter>();
		mesh			= new Mesh();
		meshFilter.mesh	= mesh;
		mesh.name		= "grid";

		gridVertices	= new Vector3[(xSize + 1) * (ySize + 1)];
		gridIndices		= new int[xSize * ySize * 6];

		for( int y = 0, i = 0; y <= ySize; y++ )
		{
			for( int x = 0; x <= xSize; x++, i++ )
			{
				gridVertices[i] = new Vector3( x, y, 0f);
			}
		}

		mesh.vertices = gridVertices;

		for( int y = 0, ti = 0, vi = 0; y < ySize; y++, vi++ )
		{
			for( int x = 0; x < xSize; x++, ti += 6, vi++ )
			{
				gridIndices[ti] = vi;
				gridIndices[ti + 2] = gridIndices[ti + 3] = vi + 1;
				gridIndices[ti + 1] = gridIndices[ti + 4] = vi + xSize + 1;
				gridIndices[ti + 5] = vi + xSize + 2;
			}
		}

		mesh.triangles = gridIndices;
	}

	private void OnDrawGizmos()
	{
		if( null == gridVertices ) { return; }

		Gizmos.color = Color.black;
		for( int i  = 0;  i < gridVertices.Length; i++ )
		{
			Gizmos.DrawSphere( gridVertices[i], 0.1f );
		}
	}
}
