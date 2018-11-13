using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MeshDeformerInput : MonoBehaviour 
{
	public float force = 10f;

	private void Update()
	{
		if( Input.GetMouseButton(0) )
		{
			HandleInput();
		}
	}

	private void HandleInput()
	{
		Ray inputRay = Camera.main.ScreenPointToRay( Input.mousePosition );
		RaycastHit hit;

		if( Physics.Raycast(inputRay, out hit ) )
		{
			TouchCell( hit.point );
			//VisaulizeRay( hit.point );
		}
	}

	private void TouchCell( Vector3 position )
	{
		position = transform.InverseTransformPoint( position );
		Debug.Log( "Touched at : " + position );
	}

	private void VisaulizeRay( Vector3 point )
	{
		Debug.DrawLine( Camera.main.transform.position, point );
	}

}
