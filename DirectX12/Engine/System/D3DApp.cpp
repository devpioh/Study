#include "pch.h"
#include "D3DApp.h"


using namespace DX12PE;
using Microsoft::WRL::ComPtr;


D3DApp::D3DApp(HINSTANCE hInstance)
	: WinApp(hInstance)
{
}

D3DApp::~D3DApp()
{
	if (nullptr != mD3dDevice)
		FlushCommandQueue();
}

bool D3DApp::InitDirect3D()
{
	// active d3d debug layer
#if defined(DEBUG) || defined(_DEBUG)
	ComPtr<ID3D12Debug> debugCtrl;
	ThrowIfFailed(D3D12GetDebugInterface(IID_PPV_ARGS(&debugCtrl)));
	debugCtrl->EnableDebugLayer();
#endif

	// create DXFactory
	ThrowIfFailed(CreateDXGIFactory1(IID_PPV_ARGS(&mDxgiFactory)));

	// create hardware device
	HRESULT hardwareResult = D3D12CreateDevice(
		nullptr,						// use default adapter
		D3D_FEATURE_LEVEL_11_0,
		IID_PPV_ARGS(&mD3dDevice));


	// if failed use WARP adapter
	if (FAILED(hardwareResult))
	{
		ComPtr<IDXGIAdapter> pWARPAdapter;
		ThrowIfFailed(mDxgiFactory->EnumWarpAdapter(IID_PPV_ARGS(&pWARPAdapter)));

		ThrowIfFailed(D3D12CreateDevice(
			pWARPAdapter.Get(),
			D3D_FEATURE_LEVEL_11_0,
			IID_PPV_ARGS(&mD3dDevice)));
	}

	return true;
}

void D3DApp::CreateCommandObjects()
{
	D3D12_COMMAND_QUEUE_DESC queueDesc = {};
	queueDesc.Type		= D3D12_COMMAND_LIST_TYPE_DIRECT;
	queueDesc.Flags		= D3D12_COMMAND_QUEUE_FLAG_NONE;
	ThrowIfFailed(mD3dDevice->CreateCommandQueue(&queueDesc, IID_PPV_ARGS(&mCommandQueue)));


	ThrowIfFailed(mD3dDevice->CreateCommandAllocator(
		D3D12_COMMAND_LIST_TYPE_DIRECT,
		IID_PPV_ARGS(mCommandAlloc.GetAddressOf())));

	ThrowIfFailed(mD3dDevice->CreateCommandList(
		0, 
		D3D12_COMMAND_LIST_TYPE_DIRECT,
		mCommandAlloc.Get(),
		nullptr,
		IID_PPV_ARGS(mCommandList.GetAddressOf())));


	
	mCommandList->Close();
}

void D3DApp::CreateSwapChain()
{
	mSwapChain.Reset();

	DXGI_SWAP_CHAIN_DESC scDesc;
	scDesc.BufferDesc.Width			= mWinWidth;
	scDesc.BufferDesc.Height		= mWinHeight;
	scDesc.BufferDesc.RefreshRate.Numerator		= 60;
	scDesc.BufferDesc.RefreshRate.Denominator	= 1;
	scDesc.BufferDesc.Format		= mBackBufferFormat;
	scDesc.BufferDesc.ScanlineOrdering = DXGI_MODE_SCANLINE_ORDER_UNSPECIFIED;
	scDesc.BufferDesc.Scaling		= DXGI_MODE_SCALING_UNSPECIFIED;
	scDesc.SampleDesc.Count			= m4xMASSState ? 4 : 1;
	scDesc.SampleDesc.Quality		= m4xMASSState ? (m4xMASSQuality - 1) : 0;
	scDesc.BufferUsage				= DXGI_USAGE_RENDER_TARGET_OUTPUT;
	scDesc.BufferCount				= SWAP_CHAIN_COUNT;
	scDesc.OutputWindow				= mhWnd;
	scDesc.Windowed					= true;
	scDesc.SwapEffect				= DXGI_SWAP_EFFECT_FLIP_DISCARD;
	scDesc.Flags					= DXGI_SWAP_CHAIN_FLAG_ALLOW_MODE_SWITCH;

	ThrowIfFailed(mDxgiFactory->CreateSwapChain(
		mCommandQueue.Get(),
		&scDesc,
		mSwapChain.GetAddressOf()));
}

void D3DApp::FlushCommandQueue()
{

}


int D3DApp::Run()
{
	MSG msg = { 0 };

	mClock.Reset();

	while (WM_QUIT != msg.message)
	{
		if (PeekMessage(&msg, 0, 0, 0, PM_REMOVE))
		{
			TranslateMessage(&msg);
			DispatchMessage(&msg);
		}
		else
		{
			mClock.TickTock();

			if( false == Helper::HasFlag(mWinDisplayState, WIN_DISPLAY_STATE::e_PAUSE) )
			{
				CalcFrameState();
				Update(mClock);
				Draw(mClock);
			}
			else
			{
				Sleep(100);
			}
		}
	}

	return (int)msg.wParam;
}

void D3DApp::OnResize()
{

}

void D3DApp::LogAdapters()
{
	UINT i = 0;
	IDXGIAdapter* adapter = nullptr;
	std::vector<IDXGIAdapter*> adapterList;

	while (DXGI_ERROR_NOT_FOUND != mDxgiFactory->EnumAdapters(i, &adapter))
	{
		DXGI_ADAPTER_DESC desc;
		adapter->GetDesc(&desc);

		std::wstring text = L"***Adapter : ";
		text += desc.Description;
		text += L"\n";

		OutputDebugString(text.c_str());
		adapterList.push_back(adapter);
	}

	for (size_t i = 0; i < adapterList.size(); i++)
	{
		LogAdapterOuputs(adapterList[i]);
		ReleaseCOM(adapterList[i]);
	}
}

void D3DApp::LogAdapterOuputs(IDXGIAdapter* adapter)
{
	UINT i = 0; 
	IDXGIOutput* output = nullptr;

	while (DXGI_ERROR_NOT_FOUND != adapter->EnumOutputs(i, &output))
	{
		DXGI_OUTPUT_DESC desc;
		output->GetDesc(&desc);

		std::wstring text = L"***Output : ";
		text += desc.DeviceName;
		text += L"\n";

		LogOutputDisplayModes(output, DXGI_FORMAT_B8G8R8A8_UNORM);

		ReleaseCOM(output);

		++i;
	}
}

void D3DApp::LogOutputDisplayModes(IDXGIOutput* output, DXGI_FORMAT format)
{
	UINT count = 0;
	UINT flags = 0;

	output->GetDisplayModeList(format, flags, &count, nullptr);

	std::vector<DXGI_MODE_DESC> modeList(count);
	output->GetDisplayModeList(format, flags, &count, &modeList[0]);

	for (auto& mode : modeList)
	{
		UINT n = mode.RefreshRate.Numerator;
		UINT d = mode.RefreshRate.Denominator;

		std::wstring text =
			L"Width : " + std::to_wstring(mode.Width) + L" " +
			L"Height : " + std::to_wstring(mode.Height) + L" " +
			L"Refresh : " + std::to_wstring(n) + L"/" + std::to_wstring(d) + L"\n";

		::OutputDebugString(text.c_str());
	}
}


LRESULT CALLBACK D3DApp::MsgProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
	return 0;
}

