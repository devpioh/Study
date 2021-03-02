#include "pch.h"
#include "WinApp.h"

using namespace DX12PE;

LRESULT CALLBACK WndProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
	return WinApp::GetApp()->MsgProc(hWnd, msg, wParam, lParam);
}

WinApp* WinApp::winApp = nullptr;

WinApp::WinApp(HINSTANCE hInstance)
	: hInst(hInstance)
{
	hWnd = nullptr;
}

WinApp::~WinApp()
{

}

bool WinApp::InitWindow()
{
	if (nullptr == hInst)
		return false;

	WNDCLASSEX wndClass;
	wndClass.cbSize			= sizeof(WNDCLASSEX);
	wndClass.style			= CS_HREDRAW | CS_VREDRAW;
	wndClass.lpfnWndProc	= WndProc;
	wndClass.hInstance		= hInst;
	wndClass.cbClsExtra		= 0;
	wndClass.cbWndExtra		= 0;
	wndClass.hIcon			= LoadIcon(hInst, IDI_APPLICATION);
	wndClass.hIconSm		= LoadIcon(hInst, IDI_APPLICATION);
	wndClass.hCursor		= LoadCursor(NULL, IDC_ARROW);
	wndClass.hbrBackground	= (HBRUSH)GetStockObject(NULL_BRUSH);
	wndClass.lpszMenuName	= NULL;
	wndClass.lpszClassName	= L"myApp";
	

	if (!RegisterClassEx(&wndClass))
		return false;

	hWnd					= CreateWindow(
		wndClass.lpszClassName,
		L"DX12",
		WS_OVERLAPPEDWINDOW,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		NULL,
		NULL,
		hInst,
		NULL
		);

	return false;
}
