#pragma once
#include "System\D3DApp.h"


class InitD3DApp : public DX12PE::D3DApp
{
public:
	virtual bool Initialize() override;
	virtual void CreateRtvAndDsvDescriptorHeap() override;
};