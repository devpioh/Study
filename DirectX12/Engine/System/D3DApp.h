#pragma once
#include "WinApp.h"

#pragma comment(lib, "d3dcompiler.lib")
#pragma comment(lib, "D3D12.lib")
#pragma comment(lib, "dxgi.lib")

namespace DX12PE
{
	class Clock;

	class D3DApp : public WinApp
	{
	public:
		int Run();

		/*bool Is4xMSAAState() const;
		void Set4xMSAAState(bool value);*/

		virtual LRESULT CALLBACK MsgProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam) override;

	protected:
		D3DApp(HINSTANCE hInstace);
		D3DApp(const D3DApp& d3dApp) = delete;
		D3DApp& operator=(const D3DApp& d3dApp) = delete;
		virtual ~D3DApp();


		//virtual void CreateRtvAndDsvDescriptorHeap();
		virtual void OnResize();
		virtual void Update();
		virtual	void Draw();

		virtual void OnMouseDown(WPARAM btnState, int x, int y)		{}
		virtual void OnMouseUp(WPARAM btnState, int x, int y)		{}
		virtual void OnMouseMove(WPARAM btnState, int x, int y)		{}

	protected:
		virtual bool InitDirect3D();

		/*void CreateCommandObjects();
		void CreateSwapChain();
		void FlushCommandQueue();*/

		
		
		//ID3DResource
	
		//ID3D12Resource
		//ID3D12Resource* CurrentBackBuffer() const
		//ID3D12

	protected:
		//Clock systemClock;

		//Microsoft::WRL::

	};
}
