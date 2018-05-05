#pragma once
#include "stdafx.h"

class SoSimple
{
private:
	int num;

public:
	SoSimple(int n) : num(n)
	{
	}

	SoSimple& AddNum(int n)
	{
		num += n;

		return *this;
	}

	void ShowData()
	{
		std::cout << "ShowData() -> num : " << num << std::endl;
	}

	void ShowData() const
	{
		std::cout << "const ShowData() -> num : " << num << std::endl;
	}
};
