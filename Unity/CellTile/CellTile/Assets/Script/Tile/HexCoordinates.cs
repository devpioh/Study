using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[System.Serializable]
public struct HexCoordinates 
{
	public static HexCoordinates FromOffsetCoordinates( int x, int z )
	{ 
		return new HexCoordinates( x - z / 2, z ); 
	}

	public static HexCoordinates FromPosition( Vector3 position )
	{
		float x = position.x / (HexMetrics.innerRadius * 2f);
		float y = -x; 

		float offset = position.z / (HexMetrics.outerRadius * 3f);
		x 	= x - offset;
		y 	= y - offset;

		int iX = Mathf.RoundToInt(x);
		int iY = Mathf.RoundToInt(y);
		int iZ = Mathf.RoundToInt(-x -y);

		if( 0 != (iX+iY+iZ)  )
		{
			float dx = Mathf.Abs( x - iX );
			float dy = Mathf.Abs( y - iY );
			float dz = Mathf.Abs( -x -y - iZ );

			if( dx > dy && dx > dz )
			{
				iX = -iY - iZ;
			}
			else if( dz > dy )
			{
				iZ = -iX - iY;
			}
		}

		return new HexCoordinates( iX, iZ );
	}

	public int X		{ get{ return x; } }
	public int Z		{ get{ return z; } }
	public int Y		{ get{ return -X - Z; } }

	[SerializeField]
	private int x, z;

	public HexCoordinates( int x, int z )
	{
		this.x = x;
		this.z = z;
	}

	public override string  ToString()
	{
		return string.Format("({0}, {1}, {2})", X, Y, Z);
	}

	public string ToStringOnSeparateLines()
	{
		return string.Format("{0}\n{1}\n{2}", X, Y, Z);
	}
}
