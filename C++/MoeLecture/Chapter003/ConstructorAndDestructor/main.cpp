#pragma once
#include "stdafx.h"
#include "NameCard.h"

void main()
{
	NameCard manClerk("Lee", "010-1111-2222", "ABCEng", COMP_POS::CLERK);
	NameCard manSenior("Hong", "010-3333-4444", "OrangeEng", COMP_POS::SENIOR);
	NameCard manAssist("Lee", "010-5555-6666", "SoGoodComp", COMP_POS::ASSIST);

	manClerk.Show();
	manSenior.Show();
	manAssist.Show();
}
