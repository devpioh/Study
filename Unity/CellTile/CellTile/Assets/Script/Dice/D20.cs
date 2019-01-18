using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent(typeof(MeshFilter), typeof(MeshRenderer))]
public class D20 : MonoBehaviour 
{
	public List<Material> test		= new List<Material>();

	private MeshFilter filter;
	private MeshRenderer renderer;
	private Mesh mesh;
	private List<Vector3> vertices	= new List<Vector3>();
	private List<int> triangles		= new List<int>();

	private void Awake()
	{
		BuildDebug();
		BuildDice();
	}

	private void BuildDice()
	{
		renderer			= GetComponent<MeshRenderer>();
		filter				= GetComponent<MeshFilter>();
		mesh				= new Mesh();

		vertices.AddRange( DiceMetrics.D20Vertices );
		
		triangles.AddRange( new int[] 
		{
			// pentagon1
			0, 11, 5,
			0, 5, 1,
			0, 1, 7, 
			0, 7, 10,
			0, 10, 11,

			// triangle adjacent pentagon1 
			1, 5, 9,
			5, 11, 4,
			11, 10, 2,
			10, 7, 6,
			7, 1, 8,

			// pentagon2
			3, 9, 4,
			3, 4, 2,
			3, 2, 6, 
			3, 6, 8, 
			3, 8, 9,

			// triangle adjacent pentagon2
			4, 9, 5,
			2, 4, 11,
			6, 2, 10,
			8, 6, 7, 
			9, 8, 1,
		} );


		mesh.vertices		= vertices.ToArray();
		mesh.triangles		= triangles.ToArray();

		filter.mesh			= mesh;
	}

	private void BuildDebug()
	{
		var rect1			= new GameObject("Rect1");
		rect1.transform.SetParent( transform );

		var rect1Filter		= rect1.AddComponent<MeshFilter>();
		var rect1Renderer	= rect1.AddComponent<MeshRenderer>();
		var rect1Mesh		= new Mesh();

		rect1Mesh.vertices	= new Vector3[] { DiceMetrics.D20Vertices[0], DiceMetrics.D20Vertices[1], DiceMetrics.D20Vertices[2], DiceMetrics.D20Vertices[3] };
		rect1Mesh.triangles	= new int[] { 0, 1, 3, 0, 3, 2 };
		rect1Filter.mesh 	= rect1Mesh;
		rect1Renderer.material = test[0];


		var rect2			= new GameObject("Rect2");
		rect2.transform.SetParent( transform );

		var rect2Filter		= rect2.AddComponent<MeshFilter>();
		var rect2Renderer	= rect2.AddComponent<MeshRenderer>();
		var rect2Mesh		= new Mesh();

		rect2Mesh.vertices	= new Vector3[] { DiceMetrics.D20Vertices[4], DiceMetrics.D20Vertices[5], DiceMetrics.D20Vertices[6], DiceMetrics.D20Vertices[7] };
		rect2Mesh.triangles	= new int[] { 0, 1, 3, 0, 3, 2 };
		rect2Filter.mesh 	= rect2Mesh;
		rect2Renderer.material = test[1];


		var rect3			= new GameObject("Rect3");
		rect3.transform.SetParent( transform );

		var rect3Filter		= rect3.AddComponent<MeshFilter>();
		var rect3Renderer	= rect3.AddComponent<MeshRenderer>();
		var rect3Mesh		= new Mesh();

		rect3Mesh.vertices	= new Vector3[] { DiceMetrics.D20Vertices[8], DiceMetrics.D20Vertices[9], DiceMetrics.D20Vertices[10], DiceMetrics.D20Vertices[11] };
		rect3Mesh.triangles	= new int[] { 0, 1, 3, 0, 3, 2 };
		rect3Filter.mesh 	= rect3Mesh;
		rect3Renderer.material = test[2];

	}

	private void OnDrawGizmos()
	{
		Gizmos.color = Color.black;
		for( int i = 0; i < DiceMetrics.D20Vertices.Length; i++ )
		{
			Gizmos.DrawSphere( DiceMetrics.D20Vertices[i], 0.05f );
		}
	}
}
