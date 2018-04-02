#pragma once
#include "stdafx.h"

class NameCard
{
public:
	NameCard( const char *name, const char *phone, const char *company, COMP_POS pos);
	~NameCard();

public:
	void Show();

private:
	char *name;
	char *phone;
	char *company;

	COMP_POS pos;
};

