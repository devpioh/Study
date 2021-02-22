# Direct3D 초기화

## Direct3D 12 기본적인 초기화 단계
  1. D3D12CreateDevice 함수를 이용해서 ID3D12Device를 생성.
  2. ID3D12Fence 객체를 생성하고 서술자들의 크기를 얻는다.
  3. 4X MSAA 품질 수준 지원 여부 점검.
  4. 명령 대기열과 명령 목록 할당자, 그리고 메인 명령 목록을 생성.
  5. 교환 사술을 서술 하고 생성.
  6. 응용 프로그램에 필요한 서술사 힙들을 생성.
  7. 후면 버퍼의 크기를 설정하고, 후면 버퍼에 대한 렌더 대상 뷰를 생성.
  8. 깊이/스텐실 버퍼 생성하고, 그와 연관된 깊이/스텐실 뷰를 생성한다.
  9. 뷰포트와 가위 판정용 사각형(scissor rectangle) 설정
<br>
<br>

### 1. 장치 생성
 + Direct3D 초기화는 Direct3D 12 장치(ID3D12Device)를 생성하는것으로 시작.
   - 장치(device)는 디스플레이 어댑터를 나타내는 객체.
   - 디스플레이 어댑터는 물리적 장치 또는 소프트웨어.
 + Direct3D 12 장치는 기능 지원 점검, 자원/뷰/명령목록 생성등에도 사용.
 + D3D12CreateDevice
 ```c++
 HRESULT WINAPI D3D12CreateDevice(
     IUnKnown* pAdapter,    // 장치가 나타내는 어댑터 지정, 널 포인터를 지정 시 시스템 기본(primary) 디스플레이 어뎁터를 사용
     D3D_FEATURE_LEVEL MinimumFeatureLevel,     // 응용 프로그램이 요구하는 최소 기능 수준
     REFIID riid,  // 생성하고자 하는 ID3D12Device의 COM ID
     void** ppDevice // 생성된 장치의 포인터
 );
 ```
<br>

### 2. 울타리 생성과 서술자 크기 얻기
 + 서술자 크기는 GPU마다 다를 수 있으므로, 실행 시점에서 적절한 메서드를 호출하여 확인.
 + 추후 서술자 크기가 필요할 때 바로 사용할 수 있도록 멤버 변수에 저장.
 ```c++
 ex)
 // 울타리 생성
 ThrowIfFailed(md3dDevice->CreateFence(0, D3D12_FENCE_FLAG_NONE, IID_PPV_ARGS(&mFence)));

 // 렌더 타겟 뷰 서술자 크기
 mRtvDescriptorSize = md3dDevice->GetDescriptorHandleIncrementSize( D3D12_DESCRIPTOR_HEAP_TYPE_RTV );
 // 뎁스/스텐실 뷰 서술자 크기
 mDsvDescriptorSize = md3dDevice->GetDescriptorHandleIncrementSize( D3D12_DESCRIPTOR_HEAP_TYPE_DSV );
 // 상수 버퍼, 셰이더 리소스, 정렬되지 않은 엑세스 보기 서술자 크기
 mCbvSrvDescriptorSize = md3dDevice->GetDescriptorHandleIncrementSize( D3D12_DESCRIPTOR_HEAP_TYPE_CBV_SRV_UAV );
 ```
<br>

 ### 3. 4X MSAA 품질 수준 지원 점검
  + 4X MSAA는 비용이 크지 않으면서도 화질이 많이 개선.
  + Direct3D 11급 장치가 모든 렌더 대상 형식에서 4X MSAA를 지원
  + 4X MSAA 지원 여부 명시적으로 확인
  ```c++
  ex)
  D3D12_FEATURE_DATA_MULTISAMPLE_QUALITY_LEVELS msQualityLevels;
  msQualityLevels.Format = mBackBufferFormat;
  msQualityLevels.SampleCount = 4;
  msQualityLevels.Flags = D3D12_MULTISAMPLE_QUALITY_LEVELS_FLAG_NONE;
  msQualityLevels.NumQualityLevels = 0;

  ThrowIfFailed(md3dDevice->CheckFeatureSupport(
      D3D12_FEATURE_MULTISAMPLE_QUALITY_LEVELS,
      &msQualityLevels,
      sizeof(msQualityLevels)
  ));
  ```
<br>

### 4. 명령 대기열과 명령 목록 생성
 ```c++
 ex)
 ComPtr<ID3D12CommandQueue> mCommandQueue;
 ComPtr<ID3D12CommandAllocator> mDirectCmdListAlloc;
 ComPtr<ID3D12Graphics> mCommandQueue;

 void D3DApp::CreateCommandObjects()
 {
     D3D12_COMMAND_QUEUE_DESC queueDesc = {};
     queueDesc.Type = D3D12_COMMAND_LIST_TYPE_DIRECT;
     queueDesc.Flag = D3D12_COMMAND_QUEUE_FLAG_NONE;

     ThrowIfFailed(md3dDevice->CreateCommandQueue( &queueDesc, IID_PPV_ARGS(&mCommandQueue)));

     ThrowIfFailed(md3dDevice->CreateCommandAllocator( 
         D3D12_COMMAND_LIST_TYPE_DIRECT,
         IID_PPV_ARGS(&mDirectCmdListAlloc) ));

     ThrowIfFailed(md3dDevice->CreateCommandList(
         0,
         D3D12_COMMAND_LIST_TYPE_DIRECT,
         mDirectCmdListAlloc.Get(),      // 연관된 명령 할당자
         nullptr,                               // 초기 파이프 라인 상태 객체
         IID_PPV_ARGS(mCommandList.GetAddressOf())
     ));

     // 닫힌 상태로 시작
     // 이후 명령 목록을 처음 참조 시 Reset을 호출 할는데, Reset을 호출 하려면 명령 목록이 닫혀 있어야 된다.
     mCommandList->Close();
 }
 ```
<br>

### 5. 교환 사슬의 서술과 생성
 + DXGI_SWAP_CHAIN_DESC
   ```c++
   typedef struct DXGI_SWAP_CHAIN_DESC
   {
       DXGI_MODE_DESC BufferDesc;     // 후면 버퍼의 속성들을 정의하는 구조체
       DXGI_SAMPLE_DESC SampleDesc; // 다중 표본화 표본 갯수와 품질 수준을 서술
       DXGI_USAGE BufferUsage;          // 후면 버퍼를 렌더 대상으로 사용하는지 설정
       UINT BufferCount;                    // 교환 사슬이 사용할 버퍼의 개수, 이중 버퍼링일 경우 2로 세팅
       HWND OutputWindow;             // 렌더링 결과가 표시될 창의 핸들
       BOOL Windowed;                     // 창 모드이면 true, 전체 화면 모드이면 false
       DXGI_SWAP_EFFECT SwapEffect; 
       UINT Flags; // 추가 플래그, DXGI_SWAP_CHAIN_FLAG_ALLOW_SWITCH를 지정 시 전체화면으로 세팅될때 적절한 크기로 세팅된다.
   } DXGI_SWAP_CHAIN_DESC;
   ```
 + DXGI_MODE_DESC
   ```c++
   typedef struct DXGI_MODE_DESC
   {
       UINT Width;         // 버퍼 해상도 너비(가로)
       UINT Height;        // 버퍼 해상도 높이(세로)
       DXGI_RATIONAL RefreshRate;
       DXGI_FORMAT Format; // 버퍼 디스플레이 형식
       DXGI_MODE_SCANLINE_ORDER ScanlineOrdering; // 순차 주사 대 비월 주사
       DXGI_MODE_SCALING Scaling; // 미미지를 모니터에 맞게 확대or축소 하는 방식
   } DXGI_MODE_DESC;
   ```
 + IDXGIFactory::CreateSwapChain
   ```c++
   HRESULT IDXGIFactory::CreateSwapChain(
       IUnknown *pDevice,                       // ID3D12CommandQueue 포인터
       DXGI_SWAP_CHAIN_DESC *pDesc,     // 교환 사슬 서술 구조체 포인터
       IDXGISwapChain **ppSwapChain       // 생성된 교환 사슬 인터페이스 포인터
   );
   ```
<br>

### 6. 서술자 힙 생성
 + 서술자 힙은 서술자의 종류마다 따로 생성
 + 