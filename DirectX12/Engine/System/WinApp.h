#pragma once
#include "pch.h"

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
		static WinApp* GetApp()				{ return mWinApp; }
	
		HINSTANCE AppInst() const			{ return mhInst; }
		HWND AppHandle() const				{ return mhWnd; }
		int GetWinDisplayState() const		{ return mWinDisplayState; }
		void SetWinDisplayState(int state)	{ mWinDisplayState = state; }
		virtual float AspectRatio() const	{ return static_cast<float>(mWinWidth) / mWinHeight; }
	

		virtual LRESULT CALLBACK MsgProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam) = 0;

	protected:
		WinApp(HINSTANCE hInstance);
		WinApp(const WinApp& win)				= delete;
		WinApp& operator=(const WinApp& win)	= delete;
		virtual ~WinApp();

		virtual bool InitWindow();

	protected:
		static WinApp*		mWinApp;
		HINSTANCE			mhInst;
		HWND				mhWnd;


		std::wstring mWinClassName		= L"MyWinApp";
		std::wstring mWinCaption		= L"MyWinApplication";
		int mWinDisplayState			= WIN_DISPLAY_STATE::e_ACTIVE;
		int mWinWidth					= 800;
		int mWinHeight					= 600;
	};
}


static LRESULT CALLBACK WndProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam);

