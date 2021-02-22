# CPU와 GPU의 상호 작용
### 1. 명령 목록과 명령 대기열
 + 명령 목록(command list)은 GPU가 실행하는 명령 모음(그리기 명령/자원 참조등등)
 + GPU는 명령 대기열(command queue)을 가진다.
 + CPU에서 그리기 명령들이 담긴 명령 목록을 DirectX api를 통해 명령 대기열에 제출해도 GPU가 즉시 명령을 실행하지 않는다.
   - 명령들은 GPU가 처리 할 준비가 되어야 명령을 실행한다. GPU가 이전 명령을 처리하고 있는 중에는 명령대기열에 해당 명령들을 대기시킨다.
   - GPU의 명령 대기열이 비어 있으면 GPU가 놀게 되고, 반대로 대기열이 꽉차면 CPU가 놀게되어 비효율 적이다. 
   - DirectX12의 고성능 응용 프로그램을 만들기 위한 핵심은 가용 자원을 최대한 활용할 수 있게 CPU/GPU가 쉴세 없이 돌아가게 만드는것.

 + ID3D12CommandAllocator
   - 명령 목록 생성시 사용되는 메모리 할당자
   - 명령 목록에 추가된 명령들은 이 할당자의 메모리에 저장
   - ID3D12CommandAllocator 생성
      ```c++
      HRESULT ID3D12Device::CreateCommandAllocator(
          D3D12_COMMAND_LIST_TYPE type, // 명령 목록 종류 
          REFIID riid, // 생성하고자 하는 ID3D12CommandAllocator 인터페이스의 COM ID
          void **ppCommandAlloctor // 생성된 명령 할당자를 가르키는 포인터
      );
      ```
      - D3D12_COMMAND_LIST_TYPE type : 명령 목록의 종류
        1. D3D12_COMMAND_LIST_TYPE_DIRECT : GPU가 직접 실행 하는 명령 목록
        2. D3D12_COMMAND_LIST_TYPE_BUNDLE : 명령목록을 만드는데에는 CPU의 부담이 어느정도 따른다. Direct12에서는 이런 일련의 명령들을 소위 "묶음 "단위로 기록할수 있는 최적화 수단을 제공. 단, Direct12의 그리기 API들은 이미 최적화 되어 있으므로 성능상 이득이 있는 경우에만 사용( 무조건 사용 금지 )

 + 명령 목록(command list) 생성
   ```c++
   ex)
   HRESULT ID3D12Device::CreateCommandList(
       UINT nodeMask,   // GPU가 여려개일 때 사용, GPU 어댑터 노드를 지정하는 비트마스크 , GPU가 1개 일 때는 0 세팅
       D3D12_COMMAND_LIST_TYPE type, // 명령 목록의 종류(D3D12_COMMAND_LIST_TYPE_DIRECT, D3D12_COMMAND_LIST_TYPE_BUNDLE)
       ID3D12CommandAllocator *pCommandAllocator, // 명령 목록을 할당 하는 명령 할당자.
       ID3D12PipelineState *pInitialState, // 명령 목록 초기 파이프라인 상태를 지정
       REFIID riid, // 명령 목록의 COM ID
       void **ppCommandList // 생성된 명령 목록를 가르키는 포인터
   );
   ```
 + 명령 목록에 명령 추가
   ```c++
   ex)
   // mCommandList는 ID3D12CommandList 포인터
   // 각 메서드들의 이름을 보면 즉시 실행될거 같지만 실행 되지 않고 명령목록에 기록된다.
   mCommandList->RSSetViewports( 1,  &mScreenViewport);
   mCommandList->ClearRenderTargetView(mVackBufferView, Colors::LightSteelBlue, 0, nullptr);
   mCommandList->DrawIndexedInstanced(36, 1, 0, 0, 0);

   // 명령목록에 명령을 다 추가 했으면 명령 목록을 닫는다.
   // 반드시 ID3D12CommandQueue::ExecuteCommandLists() 호출 전 명령 목록을 닫아줘야 된다.
   mCommandList->Close();
   ```
 + 명령 목록/할당자 초기화
    ```c++
   HRESULT ID3D12CommandList::Reset(
     ID3D12CommandAllocator *pAllocator,    // 명령 할당자
     ID3D12PipelineState *pInitialState           // 명령 목록 파이프라인 상태 지정
   )
    ```
   - 명령 목록을 초기 생성시 와 같은 상태로 만든다.
   - 명령 목록을 재설정 하여도 명령 대기열에 있는 명령들은 초기화 되지 않는다. 
   - 한 프레임을 완성하고 명령 할당자(ID3D12CommandAllocator)의 메모리를 다음 프레임에서 다시 재사용하기 위해 초기화가 필요.
     - HRESULT ID3D12CommandAllocator::Reset()로 초기화
     - 명령 대기열에서 명령 할당자 안의 자료를 참조 하고 있을 수 있다.
     - GPU가 명령 할당자에 담긴 모든 명령이 실행된게 확인 될때까지는 절대로 명령 할당자를 재설정 하지 말아야 된다.
 + 명령 대기열 생성
   ```c++
    ex)
    // COM 인터페이스로 ID3D12CommandQueue 선언
    Microsoft::WRL::ComPtr<ID3D12CommandQueue> mCommandQueue;

    // D3D12_COMMAND_QUEUE_DESC 구조체로 명령 대기열 서술
    D3D12_COMMAND_QUEUE_DESC queueDesc = {};
    queueDesc.Type = D3D12_COMMAND_LIST_TYPE_DIRECT;
    queueDesc.Flags = D3D12_COMMAND_QUEUE_FLAG_NONE;

    // 서술된 D3D12_COMMAND_QUEUE_DESC 구조체를 가지고 ID3D12CommandQueue 생성.
    ThrowIfFailed(md3dDevice->CreateCommandQueue(& queueDesc, IID_PPV_ARGS(&mCommandQueue)));
   ```
 + 명령 대기열에 명령 목록 등록
   ```c++
   // 명령 대기열에 명령 목록을 등록하기 전 명령 목록은 반드시 ID3D12GraphicsCommandList::Close()를 호출 해야된다.
   void ID3D12CommandQueue::ExecuteCommandLists(
     UINT Count,    // 명령 목록들의 갯수
     ID3D12CommandList *const *ppCommandLists // 명령 목록들의 배열 첫번째 포인터.
   );
   ```
   - 명령 대기열에 명령 목록을 추가 하는 작업도 많은 부하를 일으킨다.
   - 명령 목록들을 모아서 한거번에 명령 대기열에 추가 하는 것이 이득.

### 2. CPU/GPU 동기화
 + 한 시스템에서 두 개의 처리장치가 병렬로 실행되다 보니 여러가지 동기화 문제가 발생
   - 특정 위치 P1에 물체 A를 그리는 작업을 한다고 하자
   - CPU는 R이라는 자원에 A를 그리기 위한 위치 P1를 기록하고 A를 참조하는 그리기 명령 D를 명령 대기열에 추가한다.
   - 만일 GPU가 그리기 명령 D를 실행하기 전에 새 위치 P2를 자원 A에 기존에 있던 P1에 덮어 쓴다면 원래 의도했던 위치 P1에 그려지지 않는다.
 + 이런 문제의 해결책 중 하나는  GPU가 명령 대기열의 명령들 중 특정 지점 까지의 모든 명령 을 다 처리 할때까지 CPU를 기다리게 하는것.
 + 대기열의 모든(특정 지점까지의) 명령을 처리하는 것을 가리켜 명령 대기열을 비운다 또는 방출한다(flush)라고 한다.
 + 대기열을 비울때/방출할때, 필요한 것이 울타리(fence)라는 객체이다.
 + ID3D12Fence 의 생성
   ```c++
   HRESULT ID3D12Device::CreateFence(
     UNIT64 InitialVlaue, // 특정 시점의 울타리 지점을 식별하는 변수, 보통 초기 0으로 세팅후 새 울타리를 생성할때마나 값을 1씩 증가
     D3D12_FENCE_FLAGS Flags,
     FEFIID riid,
     void **ppFence
   );

   ex)
   ThrowIfFailed(md3dDevice->CreateFence(
     0,
     D3D12_FENCE_FALG_NONE, 
     IID_PPV_ARGS(&mFence))
     );
   ```
 ### 3. 자원 상태 전이
  + 흔히 쓰이는 렌더링 효과 중 한 단계에서 GPU가 자원에 자료를 기록하고 이후 단계에서 해당 자원에 자료를 읽어서 처리하는 방식이 많음
  + 그런데 GPU가 자원에 자료를 다 기록하지 않았거나, 기록을 하지 않은상태에서 자원을 읽으면 문제가 생김(자원 위험 상황, resource hazard)
  + Direct3D에서는 해당 문제를 해결하기 위해 자원에 상태를 부여한다.
  + 자원의 상태를 Direct3D에게 보고하는것은 전적으로 응용 프로그램의 몫

### 4. 명령 목록을 이용한 다중 스레드 활용
  + Direct3D 12는 다중 스레드를 효율적으로 활용할수 있도록 설계.
  + 1개의 명령 목록을 하나의 스레드에서 처리하지 않고 여러 스레드에 각각의 명령 목록을 병렬로 구축하여 처리
  + 명령 목록 구축에 다중스레드를 적용 할때 주의 사항
    1. 명령 목록은 자유 스레드(free-threaded) 모형을 따르지 않는다. 즉, 보통의 경우 여러 스레드가 같은 명령 목록을 공유 하지 않으며, 그 메서드들을 동시에 호출 하지 않는다. 일반적으로 각 스레드는 각자 자신만의 명령 목록을 가진다.
    2. 명령 할당자도 자유 스레드가 아니다. 각 스레드는 자신만의 명령 할당자를 가진다.(명령 목록과 동일)
    3. 명령 대기열의 경우 자유 스레드 모형을 따른다. 즉, 여러 스레드가 같은 명령 대기열에 접근 해서 그 메서드들을 동시 호출 할 수 있다. 특히 스레드들이 각자 자신이 생성한 명령 목록을 동시에 명령 대기열에 제출 할 수 있다.
    4. 성능상의 이유로, 응용 프로그램은 동시에 기록할수 있는 명령 목록들의 최대 개수를 반드시 초기화 시점에서 설정