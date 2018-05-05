#pragma once
#include "stdafx.h"

class Person
{
public:
	Person(const char *name, int age)
	{
		int len = strnlen(name, -1);
		if (0 > len)
		{
			std::cout << "Error Name Size" << std::endl;
			return;
		}

		this->name = new char[len + 1];
		strcpy_s(this->name, len, name);

		this->age = age;
	}

	Person(const Person &copy) : age( copy.age )
	{
		int len = strnlen(copy.name, -1);
		if (0 > len)
		{
			std::cout << "Error Name Size" << std::endl;
			return;
		}

		this->name = new char[len + 1];
		strcpy_s(this->name, len, copy.name);
	}

	~Person()
	{
		delete[] name;

		std::cout <<"Call destructor!"<< std::endl;
	}

public:
	void Show()
	{
		std::cout << "Name : " << name << std::endl;
		std::cout << "Age : " << age << std::endl;
	}

private:
	char *name;
	int age;
};
