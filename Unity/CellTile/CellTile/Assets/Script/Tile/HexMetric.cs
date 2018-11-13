using System.Collections;
using System.Collections.Generic;
using UnityEngine;


/// 정육각형 구조 정의
/// 정육각형은 정삼각형 6개가 모여 만들어진다.
/// 구현하기 쉽게 가상의 원을 2개 생각하여 만들어 본다.
/// 정삼각형의 한변을 반지름으로 하는 원과
/// 정삼각형의 높이를 반지름으로 하는 원을 생각한다.

// regualar hexagon
public static class HexMetrics
{
	public static Vector3 GetFirstCorner( HexDirection direction )
	{
		return corners[(int)direction];
	}

	public static Vector3 GetSecondCorner( HexDirection direction )
	{
		return corners[(int)direction + 1];
	}

	public static Vector3 GetFirstSolidCorner( HexDirection direction )
	{
		return corners[(int)direction] * solidFactor;
	}

	public static Vector3 GetSecondSolidCorner( HexDirection direction )
	{
		return corners[(int)direction + 1] * solidFactor;
	}

	public static Vector3 GetBridge( HexDirection direction )
	{
		//return (corners[(int)direction] + corners[(int)direction+1]) * 0.5f * blendFactor;
		return (corners[(int)direction] + corners[(int)direction+1]) * blendFactor;
	}

	public static Vector3 TerraceLerp( Vector3 a, Vector3 b, int step )
	{
		float h = step * HexMetrics.horizontalTerraceStepSize;
		a.x 	+= (b.x - a.x) * h;
		a.z		+= (b.z - a.z) * h;
		float v = ((step + 1) / 2) * HexMetrics.verticalTerraceStepSize;
		a.y		+= (b.y - a.y) * v;
		return a;
	}

	public static Color TerraceLerp( Color a, Color b, int step )
	{
		float h = step * HexMetrics.horizontalTerraceStepSize;
		return Color.Lerp( a, b, h );
	}

	public static HexEdgeType GetEdgeType( int elevation1, int elevation2 )
	{
		if( elevation1 == elevation2 )
		{
			return HexEdgeType.Flat;
		}

		int delta = elevation2 - elevation1;
		if( 1 == delta || -1 == delta )
		{
			return HexEdgeType.Slope;
		}

		return HexEdgeType.Cliff;
	}

	public const float outerRadius = 10f;
	public const float innerRadius = outerRadius  * 0.866025404f;
	public const float solidFactor = 0.75f;
	public const float blendFactor = 1f - solidFactor;

	public const float elevationStep = 5f;

	public const int terracesPerSlop = 2;
	public const int terracesSteps = terracesPerSlop * 2 + 1;

	public const float horizontalTerraceStepSize = 1f / terracesSteps;
	public const float verticalTerraceStepSize = 1f / (terracesPerSlop + 1);

	/// 필요한 정점은 6개지만 배열 인덱스 계산 편의를 위해 7번째 정점을 추가한다.(이때 정점은 0번의 정점과 같은 위치를 사용한다.)
	private static readonly Vector3[] corners = new Vector3[]
	{
		new Vector3( 0f, 0f, outerRadius ),
		new Vector3( innerRadius, 0f, 0.5f * outerRadius ),
		new Vector3( innerRadius, 0f, -0.5f * outerRadius ),
		new Vector3( 0f, 0f, -outerRadius ),
		new Vector3( -innerRadius, 0f, -0.5f * outerRadius ),
		new Vector3( -innerRadius, 0f, 0.5f * outerRadius ),
		new Vector3( 0f, 0f, outerRadius )
	};
}
