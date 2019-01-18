using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public static class DiceMetrics
{
	public enum DiceType
	{
		D2,				// coin
		D4, 			//
		D6,				// cube
		D8,				// Octahedron
		D12,			// Regular dodecahedron
		D20,			// Icosahedron
	}

	public const float diceRadius					= 1f;
	public static readonly float goldenRatio		= (1f + Mathf.Sqrt(5f))/2f;
	public static readonly Vector3[] D20Vertices	= new Vector3[]
	{
		// 1 rectangle
		new Vector3( -1f, goldenRatio, 0f ).normalized * diceRadius,
		new Vector3( 1f, goldenRatio, 0f ).normalized * diceRadius,
		new Vector3( -1f, -goldenRatio, 0f ).normalized * diceRadius,
		new Vector3( 1f, -goldenRatio, 0f ).normalized * diceRadius,

		// 2 rectangle
		new Vector3( 0f, -1f, goldenRatio ).normalized * diceRadius,
		new Vector3( 0f, 1f, goldenRatio ).normalized * diceRadius,
		new Vector3( 0f, -1f, -goldenRatio ).normalized * diceRadius,
		new Vector3( 0f, 1f, -goldenRatio ).normalized * diceRadius,

		// 3 rectangle
		new Vector3( goldenRatio, 0f, -1f ).normalized * diceRadius,
		new Vector3( goldenRatio, 0f, 1f ).normalized * diceRadius,
		new Vector3( -goldenRatio, 0f, -1f ).normalized * diceRadius,
		new Vector3( -goldenRatio, 0f, 1f ).normalized * diceRadius
		//[todo]
		// new Vector3( -goldenRatio, 0f, -1f ).normalized * diceRadius,
		// new Vector3( -goldenRatio, 0f, 1f ).normalized * diceRadius,
		// new Vector3( goldenRatio, 0f, -1f ).normalized * diceRadius,
		// new Vector3( goldenRatio, 0f, 1f ).normalized * diceRadius
	};


}