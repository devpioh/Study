#include "pch.h"
#include "System/D3DApp.h"

class InitD3D : public DX12PE::D3DApp
{
public:
	InitD3D(HINSTANCE hInst) : D3DApp(hInst) 
	{
		InitWindow();
		InitDirect3D();

		winApp = this;
	};
	~InitD3D() {};

	virtual void Update() override {};
	virtual void Draw() override {};
};


int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInst, LPSTR lpCmdLine, int nCmdShow)
{
	InitD3D initD3D(hInstance);

	ShowWindow(initD3D.AppHandle(), nCmdShow);
	UpdateWindow(initD3D.AppHandle());

	MSG msg;
	while(GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}

	return (int)msg.wParam;
}

