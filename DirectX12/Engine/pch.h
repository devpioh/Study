#pragma once

// win 
#include <windows.h>
#include <windowsx.h>
#include <wrl.h>

// dx12
#include <dxgi1_4.h>
#include <d3d12.h>
#include <D3Dcompiler.h>
#include <DirectXMath.h>
#include <DirectXPackedVector.h>
#include <DirectXColors.h>
#include <DirectXCollision.h>

// dx12 utils
#include "d3dx12.h"

// std
#include <string>
#include <memory>
#include <algorithm>
#include <vector>
#include <array>
#include <unordered_map>
#include <cstdint>
#include <fstream>
#include <sstream>
#include <cassert>


// my helper
#include "Helper/CommonHelper.h"
#include "Helper/Log.h"
#include "Helper/Time.h"


constexpr int SWAP_CHAIN_COUNT = 2;