#include "stdafx.h"
#include "NameCard.h"


NameCard::NameCard( const char *name, const char *phone, const char *company, COMP_POS pos)
{
	int strLen = strnlen(name, -1);
	if (0 > strlen)
	{
		std::cout << "Error Size name" << std::endl;
		return;
	}
	this->name = new char[strLen + 1];
	strcpy(this->name, name);

	strLen = strnlen(phone, -1);
	if (0 > strlen)
	{
		std::cout << "Error Size phoneNumber" << std::endl;
		return;
	}
	this->phone = new char[strLen + 1];
	strcpy(this->phone, phone);

	strLen = strnlen(company, -1);
	if (0 > strlen)
	{
		std::cout << "Error Size phoneNumber" << std::endl;
		return;
	}
	this->company = new char[strLen + 1];
	strcpy(this->company, company);

	this->pos = pos;
}

NameCard::~NameCard()
{
	delete[] name;
	delete[] company;
	delete[] phone;
}

void NameCard::Show()
{
	std::cout << "Name : " << name << std::endl;
	std::cout << "Phone : " << phone << std::endl;
	std::cout << "Company : " << company << std::endl;

	switch (pos)
	{
	case COMP_POS::CLERK:		std::cout << "JobPos : CLERK" << std::endl;	break;
	case COMP_POS::SENIOR:	std::cout << "JobPos : SENIOR" << std::endl;	break;
	case COMP_POS::ASSIST:		std::cout << "JobPos : ASSIST" << std::endl;	break;
	}
}
