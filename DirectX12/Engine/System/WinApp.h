#pragma once
#include <Windows.h>

namespace DX12PE
{
	enum WIN_DISPLAY_STATE
	{
		e_ACTIVE		= 0,
		e_PAUSE			= 1,
		e_MINIMAIZE		= 1 << 1,
		e_MAXIMIZE		= 1 << 2,
		e_RESIZING		= 1 << 3,
		e_FULLSCREEN	= 1 << 4,
	};

	class WinApp
	{
	public:
		static WinApp* GetApp()					{ return winApp; }
		inline HINSTANCE AppInst() const		{ return hInst; }
		inline HWND AppHandle() const			{ return hWnd; }
		inline int	GetWinDisplayState() const	{ return winDisplayState; }


		int SetWinDisplayState(int flag);
		virtual LRESULT CALLBACK MsgProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam) = 0;

	protected:
		WinApp(HINSTANCE hInstance);
		WinApp(const WinApp& win)				= delete;
		WinApp& operator=(const WinApp& win)	= delete;
		virtual ~WinApp();

		virtual bool InitWindow();

	protected:
		static WinApp* winApp;
		HINSTANCE hInst;
		HWND hWnd;

		int winDisplayState;
	};
}


static LRESULT CALLBACK WndProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam);

