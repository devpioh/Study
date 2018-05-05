#pragma once
#include "stdafx.h"

class Point;

class PointOP
{
private:
	int opcnt;

public:
	PointOP() : opcnt(0) {}
	~PointOP()
	{
		cout << "Operation times : " << opcnt << endl;
	}

	Point PointAdd(const Point& p1, const Point& p2);
	Point PointSub(const Point& p1, const Point& p2);
};

class Point
{
private:
	int x;
	int y;

public:
	Point(const int &xPos, const int &yPos) : x(xPos), y(yPos) {}
	friend Point PointOP::PointAdd(const Point& p1, const Point& p2);
	friend Point PointOP::PointSub(const Point& p1, const Point& p2);
	friend void ShowPointPos(const Point& p);
};

Point PointOP::PointAdd(const Point& p1, const Point& p2)
{
	opcnt++;

	return Point( p1.x + p2.x, p1.y + p2.y);
}

Point PointOP::PointSub(const Point &p1, const Point &p2)
{
	opcnt++;

	return Point( p1.x - p2.x, p1.y - p2.y );
}

void ShowPointPos(const Point &p)
{
	cout << "x : " << p.x << ", ";
	cout << "y : " << p.y << endl;
}