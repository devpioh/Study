#include <iostream>
#include <conio.h>
#include "Helper/Time.h"
#include "../../../Common/GameTimer.h"



using namespace std;

enum E_KEY
{
	E_ESC = 27,
};


int main()
{
	bool isRun = true;

	GameTimer timer;
	DX12PE::Clock clock;

	//while (isRun)
	//{
	//	//timer.Tick();
	//	//cout << "[ " << timer.DeltaTime() << " ]" << endl;
	//	cout << "[ " << clock.countsPerSec << " ]" << endl;



	//	if (_kbhit())
	//		isRun = E_ESC != static_cast<E_KEY>(_getch());
	//}

	return 0;
}

