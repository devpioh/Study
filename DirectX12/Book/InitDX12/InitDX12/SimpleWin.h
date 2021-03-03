#pragma once
#include "System/WinApp.h"

class InitWin : public DX12PE::WinApp
{
public:
	InitWin(HINSTANCE hinst) : WinApp(hinst)
	{
		InitWindow();
		winApp = this;
	}

	~InitWin() {};

protected:
	virtual LRESULT CALLBACK MsgProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam) override;
};