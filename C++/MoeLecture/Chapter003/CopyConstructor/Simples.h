#pragma once
#include "stdafx.h"

class SoSimple
{
public:
	SoSimple(int n1, int n2) : num1(n1), num2(n2) {}
	SoSimple(SoSimple &copy) : num1(copy.num1), num2(copy.num2) { std::cout << "Called SoSimple( SoSimple &copy )" << std::endl; }

public:
	void Show()
	{
		std::cout << num1 << std::endl;
		std::cout << num2 << std::endl;
	}

private:
	int num1;
	int num2;
};


class SoSimple2
{
public:
	SoSimple2(int num) : num(num) {}
	SoSimple2(const SoSimple2 &copy) : num(copy.num) 
	{
		std::cout << "Called SoSimple2(const SoSimple2 &copy)" << std::endl;
	}

public:
	SoSimple2& AddNum(int num)
	{
		this->num += num;
		return *this;
	}

	void ShowData()
	{
		std::cout << "num: " << num << std::endl;
	}

private:
	int num;
};

SoSimple2 SimpleFuncOjb(SoSimple2 ob)
{
	std::cout << "prev resturn" << std::endl;
	return ob;
} 


class Temporary
{
public:
	Temporary(int n) : num(n) 
	{
		std::cout << "Create obj : " << this << std::endl;
	}
	
	Temporary(const Temporary &copy) : num(copy.num)
	{
		std::cout << "Copy obj : " << this << std::endl;
	}

	~Temporary()
	{
		std::cout << "Destroy obj : " << this << std::endl;
	}

public:
	void Show()
	{
		std::cout << "My Num is " << num << std::endl;
	}

private:
	int num;
};

Temporary TempFuncObj(Temporary ob)
{
	std::cout << "Param ADR : "<<&ob<< std::endl;

	return ob;
}

