using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class HexGrid : MonoBehaviour 
{
	public int width		= 6;
	public int height		= 6;

	public Color defaultColor	= Color.white;

	public HexCell cellPrefab;
	public Text	cellLabelPrefab;

	private HexCell[] cells;
	private Canvas gridCanvas;
	private HexMesh hexMesh;

	private void Awake()
	{
		gridCanvas	= GetComponentInChildren<Canvas>();
		hexMesh		= GetComponentInChildren<HexMesh>();
		cells		= new HexCell[height * width];

		for( int z = 0, i = 0; z < height; z++ )
		{
			for( int x = 0; x < width; x++ )
			{
				CreateCell( x, z, i++ );
			}
		}
	}

	private void Start()
	{
		hexMesh.Triangulate(cells);
	}

	public void Refresh()
	{
		hexMesh.Triangulate(cells);
	}

	public void TouchCell( Vector3 position, Color color )
	{
		position					= transform.InverseTransformPoint( position );
        HexCoordinates coordinates	= HexCoordinates.FromPosition( position );
		int index					= coordinates.X + coordinates.Z * width + coordinates.Z / 2;
		HexCell cell				= cells[index];
		cell.color					= color;
		hexMesh.Triangulate( cells );

		// Debug.LogFormat( "Touched at : {0} : {1}", coordinates, position );
	}

	public HexCell GetCell( Vector3 position )
	{
		position					= transform.InverseTransformPoint( position );
		HexCoordinates coordinates	= HexCoordinates.FromPosition( position );
		int index					= coordinates.X + coordinates.Z * width + coordinates.Z / 2;

		return cells[index];
	}

	private void CreateCell( int x, int z, int index )
	{
		//var pos			= new Vector3( x * 10f, 0f, z * 10f );
		var pos			= Vector3.zero;
		//pos.x			= x * (HexMetrics.innerRadius * 2f);
		//pos.x			= (x + z * 0.5f) * (HexMetrics.innerRadius * 2f);
		pos.x			= (x + z * 0.5f - z / 2) * (HexMetrics.innerRadius * 2f); // trick : (int)1 / (int)2  이 경우 컴파일러는 0으로 계산.
		pos.z			= z * (HexMetrics.outerRadius * 1.5f);

		var cell		= Instantiate<HexCell>(cellPrefab);
		cell.transform.SetParent(transform, false);
		cell.transform.localPosition = pos;
		cell.coordinates = HexCoordinates.FromOffsetCoordinates(x, z);
		cell.color		= defaultColor;
		cell.name		= cell.coordinates.ToString();

		// connect cell
		if( 0 < x )
		{
			cell.SetNeighbor( HexDirection.W, cells[index - 1] );
		}

		if( 0 < z )
		{
			if( 0 == ( z & 1 ) )
			{
				cell.SetNeighbor(HexDirection.SE, cells[index - width]);
				if( 0 < x )
				{
					cell.SetNeighbor(HexDirection.SW, cells[index - width - 1]);
				}
			}
			else
			{
				cell.SetNeighbor(HexDirection.SW, cells[index - width]);
				if( x < width - 1 )
				{
					cell.SetNeighbor( HexDirection.SE, cells[index - width + 1]);
				}
			}
		}



		var label		= Instantiate<Text>( cellLabelPrefab );
		label.rectTransform.SetParent( gridCanvas.transform, false );
		label.rectTransform.anchoredPosition = new Vector2( pos.x, pos.z );
		label.text		= cell.coordinates.ToStringOnSeparateLines();

		cell.uiRect		= label.rectTransform;

		cells[index]	= cell;
	}
}
