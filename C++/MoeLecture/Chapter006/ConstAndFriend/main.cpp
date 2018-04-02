#pragma once
#include "SoSimple.h"
#include "Point.h"

void YourFunction(const SoSimple &obj)
{
	obj.ShowData();
}

void ConstTest()
{
	SoSimple obj1(2);
	const SoSimple obj2(7);

	obj1.ShowData();
	obj2.ShowData();

	YourFunction(obj1);
	YourFunction(obj2);
}

int main()
{
	Point pos1(1, 2);
	Point pos2(2, 4);
	PointOP op;

	ShowPointPos(op.PointAdd(pos1, pos2));
	ShowPointPos(op.PointSub(pos2, pos1));

	return 0;
}

