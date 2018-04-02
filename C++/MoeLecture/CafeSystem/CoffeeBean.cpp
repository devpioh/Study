#include "stdafx.h"
#include "CoffeeBean.h"


CoffeeBean::CoffeeBean(const char *_name, int _price)
{
	int len		= strnlen_s(_name, 1024);
	name		= new char[len+1];
	memset(name, 0, len+1);
	strcpy(name, _name);

	price		= _price;
}


CoffeeBean::~CoffeeBean()
{
	delete[]name;
}


void CoffeeBean::Disyplay()
{
	std::cout << "name : " << name << std::endl;
	std::cout << "price : " << price << std::endl;
}