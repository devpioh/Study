#include "stdafx.h"
#include "CafeManager.h"


CafeManager::CafeManager()
{
	isRun	= true;
	status	= 1;
	oder	= -1;
}


CafeManager::~CafeManager()
{
}


void CafeManager::Run()
{
	while(true == isRun)
	{
		MainMenu();
		Input();

		switch (oder)
		{
			case 5: Exit(); break;
		}
	}
}

void CafeManager::MainMenu()
{
	if (1 != status) { return; }

	std::cout << "1. Register Stock" << std::endl;
	std::cout << "2. Register Menu" << std::endl;
	std::cout << "3. Oder Menu" << std::endl;
	std::cout << "4. Balance Oder" << std::endl;
	std::cout << "5. Exit" << std::endl;

	status = 0;
}

void CafeManager::Input()
{
	std::cout << std::endl;
	std::cout << "Insert oder :";
	std::cin >> oder;
	std::cout << std::endl;
}

void CafeManager::Exit()
{
	isRun = false;
	std::cout << "Exit CafeSystem" << std::endl;
	std::cout << "Bye Bye!!" << std::endl;
}