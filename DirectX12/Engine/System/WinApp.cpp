#include "pch.h"
#include "WinApp.h"

using namespace DX12PE;

LRESULT CALLBACK WndProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
	return WinApp::GetApp()->MsgProc(hWnd, msg, wParam, lParam);
}

WinApp* WinApp::mWinApp = nullptr;

WinApp::WinApp(HINSTANCE hInstance)
	: mhInst(hInstance)
{
	mWinApp				= this;
	mhWnd				= nullptr;
}

WinApp::~WinApp()
{

}

bool WinApp::InitWindow()
{
	if (nullptr == mhInst)
		return false;

	WNDCLASSEX wndClass;
	wndClass.cbSize			= sizeof(WNDCLASSEX);
	wndClass.style			= CS_HREDRAW | CS_VREDRAW;
	wndClass.lpfnWndProc	= WndProc;
	wndClass.hInstance		= mhInst;
	wndClass.cbClsExtra		= 0;
	wndClass.cbWndExtra		= 0;
	wndClass.hIcon			= LoadIcon(mhInst, IDI_APPLICATION);
	wndClass.hIconSm		= LoadIcon(mhInst, IDI_APPLICATION);
	wndClass.hCursor		= LoadCursor(NULL, IDC_ARROW);
	wndClass.hbrBackground	= (HBRUSH)GetStockObject(NULL_BRUSH);
	wndClass.lpszMenuName	= NULL;
	wndClass.lpszClassName	= mWinClassName.c_str();
	

	if (!RegisterClassEx(&wndClass))
		return false;

	mhWnd					= CreateWindow(
		wndClass.lpszClassName,
		mWinCaption.c_str(),
		WS_OVERLAPPEDWINDOW,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		mWinWidth,
		mWinHeight,
		NULL,
		NULL,
		mhInst,
		NULL
		);

	return NULL != mhWnd;
}
