#pragma once
#include "CoffeeBean.h"

class CafeManager
{
public:
	CafeManager();
	~CafeManager();

public:
	void Run();

private:
	void MainMenu();
	void Input();
	void Exit();

private:
	bool isRun;
	int status;
	int oder;
};

