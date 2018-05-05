#pragma once

#include "stdafx.h"
#include "SoSimple.h"
// #include "Point.h"
// #include "CafeManager.h"
// #include "Simples.h"
// #include "Person.h"


void main()
{
	// Point pos1(1, 2);
	// Point pos2(2, 4);
	// PointOP op;

	// ShowPointPos(op.PointAdd(pos1, pos2));
	// ShowPointPos(op.PointSub(pos2, pos1));

	// NameCard manClerk("Lee", "010-1111-2222", "ABCEng", COMP_POS::CLERK);
	// NameCard manSenior("Hong", "010-3333-4444", "OrangeEng", COMP_POS::SENIOR);
	// NameCard manAssist("Lee", "010-5555-6666", "SoGoodComp", COMP_POS::ASSIST);

	// manClerk.Show();
	// manSenior.Show();
	// manAssist.Show();

	// Temporary obj(7);
	// TempFuncObj(obj);

	// std::cout << std::endl;
	// Temporary tempRef = TempFuncObj(obj);
	// std::cout << "return Obj " << &tempRef << std::endl;
}

// void YourFunction(const SoSimple &obj)
// {
// 	obj.ShowData();
// }

// void ConstTest()
// {
// 	SoSimple obj1(2);
// 	const SoSimple obj2(7);

// 	obj1.ShowData();
// 	obj2.ShowData();

// 	YourFunction(obj1);
// 	YourFunction(obj2);
// }

// void CopyConstructorTest()
// {
// 	SoSimple sim1(15, 20);
// 	std::cout << "Previouse Create and init" << std::endl;
// 	SoSimple sim2 = sim1;
// 	std::cout << "After Create and init" << std::endl;

// 	//std::cout << "sim1" << std::endl;
// 	//sim1.Show();

// 	//std::cout << std::endl;

// 	std::cout << "sim2" << std::endl;
// 	sim2.Show();
// }

// void ShallowCopyAndDeepCopy()
// {
// 	Person man("Kim Kyung Hee", 29);
// 	Person copyMan = man;

// 	std::cout << "Man info" << std::endl;
// 	man.Show();
// 	std::cout << std::endl;
// 	std::cout << "CopyMan info" << std::endl;
// 	copyMan.Show();
// }

// void TemporaryObjectCopyConstructor()
// {
// 	SoSimple2 obj(7);
// 	SimpleFuncOjb(obj).AddNum(30).ShowData();
// 	obj.ShowData();
// }

// void TemporaryRef()
// {
// 	Temporary(100);
// 	std::cout << "**************************** after make" << std::endl << std::endl;

// 	Temporary(200).Show();
// 	std::cout << "**************************** after make" << std::endl << std::endl;

// 	const Temporary &ref = Temporary(300);
// 	std::cout << "**************************** end of make" << std::endl << std::endl;
// }

