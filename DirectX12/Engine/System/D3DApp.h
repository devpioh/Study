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
		virtual bool Initialize();

		int Run();

		bool CheckSupport4XMASAA() const		{ return 0 < m4xMASSQuality; }
		bool Is4xMSAAState() const				{ return m4xMASSState; }
		void Set4xMSAAState(bool massActive)	{ m4xMASSState = massActive; }

		virtual LRESULT CALLBACK MsgProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam) override;

	protected:
		D3DApp(HINSTANCE hInstace);
		D3DApp(const D3DApp& d3dApp)				= delete;
		D3DApp& operator=(const D3DApp& d3dApp)		= delete;
		virtual ~D3DApp();


		virtual void CreateRtvAndDsvDescriptorHeap();
		virtual void OnResize();
		virtual void Update(const Clock& clock)		= 0;
		virtual	void Draw(const Clock& clock)		= 0;

		virtual void OnMouseDown(WPARAM btnState, int x, int y)		{}
		virtual void OnMouseUp(WPARAM btnState, int x, int y)		{}
		virtual void OnMouseMove(WPARAM btnState, int x, int y)		{}

	protected:
		virtual bool InitDirect3D();

		void CreateCommandObjects();
		void CreateSwapChain();
		void FlushCommandQueue();

		
		ID3D12Resource* CurrentBackBuffer() const			
		{
			return mSwapChainBuffers[mCurrentBackBufferNum].Get(); 
		}

		D3D12_CPU_DESCRIPTOR_HANDLE CurrentBackBufferView() const		
		{ 
			return CD3DX12_CPU_DESCRIPTOR_HANDLE(
				mRtvHeap->GetCPUDescriptorHandleForHeapStart(),
				mCurrentBackBufferNum,
				mRtvDescriptorSize);
		}

		D3D12_CPU_DESCRIPTOR_HANDLE DepthStencilView() const
		{
			return mDsvHeap->GetCPUDescriptorHandleForHeapStart();
		}


		//[todo] : move to helper
		void CalcFrameState();
		void LogAdapters();
		void LogAdapterOuputs(IDXGIAdapter* adapter);
		void LogOutputDisplayModes(IDXGIOutput* output, DXGI_FORMAT format);
		///

	protected:
		Microsoft::WRL::ComPtr<IDXGIFactory4>				mDxgiFactory;
		Microsoft::WRL::ComPtr<IDXGISwapChain>				mSwapChain;
		Microsoft::WRL::ComPtr<ID3D12Device>				mD3dDevice;
		Microsoft::WRL::ComPtr<ID3D12Fence>					mFence;
		Microsoft::WRL::ComPtr<ID3D12CommandQueue>			mCommandQueue;
		Microsoft::WRL::ComPtr<ID3D12CommandAllocator>		mCommandAlloc;
		Microsoft::WRL::ComPtr<ID3D12GraphicsCommandList>	mCommandList;
		Microsoft::WRL::ComPtr<ID3D12Resource>				mSwapChainBuffers[SWAP_CHAIN_COUNT];
		Microsoft::WRL::ComPtr<ID3D12Resource>				mDepthStencilBuffer;
		Microsoft::WRL::ComPtr<ID3D12DescriptorHeap>		mRtvHeap;
		Microsoft::WRL::ComPtr<ID3D12DescriptorHeap>		mDsvHeap;

		D3D12_VIEWPORT		mScreenViewport;
		D3D12_RECT			mScissorRect;

		Clock				mClock;

		D3D_DRIVER_TYPE		mD3dDriverType			= D3D_DRIVER_TYPE_HARDWARE;
		DXGI_FORMAT			mBackBufferFormat		= DXGI_FORMAT_R8G8B8A8_UNORM;
		DXGI_FORMAT			mDepthStencilFormat		= DXGI_FORMAT_D24_UNORM_S8_UINT;

		UINT64				mCurrentFence			= 0;
		UINT				mRtvDescriptorSize		= 0;
		UINT				mDsvDescriptorSize		= 0;
		UINT				mCbvSrvDescriptorSize	= 0;
		int					mCurrentBackBufferNum	= 0;

		UINT				m4xMASSQuality			= 0;
		bool				m4xMASSState			= false;
	};
}
