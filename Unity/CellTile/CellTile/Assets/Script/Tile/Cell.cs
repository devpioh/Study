using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Cell : MonoBehaviour 
{
	public Material material;

	private void Awake()
	{
		var mesh		= new Mesh();
		var vertices	= new List<Vector3>();
		var uv			= new List<Vector2>();
		var center		= Vector3.zero;
		var radius		= 1f;

		vertices.Add( center );
		uv.Add( new Vector3(0.5f, 0.5f));
		var centerGo = new GameObject("0");
		centerGo.transform.position = center;
		centerGo.transform.SetParent( transform );


		for( int i = 0; i < 6; i++ )
		{
			var x = Mathf.Cos( i * 60 * Mathf.Deg2Rad ) * radius;
			var z = Mathf.Sin( i * 60 * Mathf.Deg2Rad ) * radius;
			var pos = new Vector3( x, 0f, z );
			
			var go = new GameObject((i + 1).ToString());
			go.transform.position = pos;
			go.transform.SetParent( transform );

			vertices.Add( pos );

			Debug.Log( pos );
		}

		var indeces = new int[]
		{
			0, 2, 1, 
			0, 3, 2, 
			0, 4, 3, 
			0, 5, 4, 
			0, 6, 5, 
			0, 1, 6, 
		};

		mesh.SetVertices( vertices );
		mesh.triangles = indeces;
		// mesh.SetUVs(0, uv );

		var meshfilter = gameObject.AddComponent<MeshFilter>();
		meshfilter.mesh = mesh;

		var meshRenderer = gameObject.AddComponent<MeshRenderer>();
		meshRenderer.material = material;
	}
}
