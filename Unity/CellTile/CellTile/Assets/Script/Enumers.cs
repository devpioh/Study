using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public enum HexDirection
{
	NE,
	E,
	SE,
	SW,
	W,
	NW
}

public static class HexDirectionExtensions
{
	public static HexDirection Opposite( this HexDirection direction )
	{
		return 3 > (int)direction ? (direction + 3) : (direction - 3);
	}

	public static HexDirection Previous( this HexDirection direction )
	{
		return HexDirection.NE == direction ? HexDirection.NW : (direction - 1);
	}

	public static HexDirection Next( this HexDirection direction )
	{
		return HexDirection.NW == direction ? HexDirection.NE : (direction + 1);
	}
}