# Direct3D 12 초기화

## 기본 지식
### 1. COM(Component Object Model)
 DirectX에서 프로그래밍 언어 독립성과 하위 호환성을 위해 사용한 기술

### 2. 텍스쳐 형식
 +  DXGI_FORMAT_R32G32B32_FLOAT  : 각 원소는 32비트 부동 소수점 성분 3개로 구성
 +  DXGI_FORMAT_R16G16B16A16_UNORN : 각 원소는 [0, 1] 구간 16비트 성분 4개로 구성
 +  DXGI_FORMAT_R32G32_UINT : 각 원소는 부호없는 32비트 정수 성분 2개로 구성
 +  DXGI_FORMAT_R8G8B8A8_UNORM : 각 원소는 [0, 1] 구간 부호 없는 8비트 성부 4개로 구성
 +  DXGI_FORMAT_R8G8B8A8_SNORM : 각 원소는 [-1, 1] 구간 부호 있는 8비트 성분 4개로 구성
 +  DXGI_FORMAT_R8G8B8A8_SINT : 각 원소는 [-128, 128] 구간 부호 있는 8비트 성분 4개로 구성
 +  DXGI_FORMAT_R8G8B8A8_UINT : 각 원소는 [0, 255] 구간 부호 없는 8비트 성분 4개로 구성


### 3. 교환 사슬(IDXGISwapChain)
### 4. 깊이 버퍼(depth buffer)
### 5. 자원(Resource)과 서술자(Descriptor)
 + GPU 자원(Resource) : 후면/깊이/스텐실 버퍼등, 범용 적인 메모리 조각
 + 바인딩(Binding) : 그리기 호출(Draw call)이 참조할 GPU 자원들을 렌더링 파이프라인에 연결하는 작업
 + 서술자(Descriptor) 객체 :  그리기 호출은 직접적으로  GPU 자원을 참조 하지않고 서술자 객체를 통해 자원을 참조
 + 자원은 앞서 설명했듯이 범용적인 메모리 조각들인데 이는 렌더링 파이프라인의 서로 다른 단계(Stage)에서 사용이 가능.
 + 자원 자체는 자신이 렌더 대상으로 쓰이는지, 아니면 깊이/스텐실 버퍼나 셰이더 자원으로 쓰이는지에 대해 알 수 없다.
 + 자원의 일부영역만 렌더링 파이프라인에 묶고 싶은데, 자원에는 이런 부분 영역에 대한 정보가 없다.
 + 이런 자원에 대한 정보를 서술하는 것이 서술자 객체.
 + 서술자의 종류
   - CBV / SRV / UAV 서술자들은 각각 상수 버퍼(contant buffer), 셰이더 자원(shader resource), 순서 없는 접근 (unordered access view)를 서술한다.
   - 표본추출기(Sampler) 서술자는 텍스처 적용에 쓰이는 표본추출기 자원을 서술
   - RTV 서술자는 렌더 대상(Render target) 자원을 서술
   - DSV 서술자는 깊이/스텐실(Depth/Stencil) 자원을 서술
 + 서술자 힙(decrtiptor heap)은 응용프로그램이 사용하는 서술자들이 저장되는 힙
 + 서술자의 종류마다 개별적인 서술자 힙이 필요
 + 한 종류의 서술자에 대해 여러 개의 힙을 둘 수 있다.
 + 하나의 자원을 참조하는 서술자가 하나뿐이여야만 하는 것은 아님, 여러 서술자가 하나의 자원을 참조 할 수 있다.
 + 하나의 자원을 렌더링 파이프라인의 여러단계에 묶을 수 있는데, 이때 단계마다 개별적인 서술자가 필요.

### 6. 다중표본화
 + 앨리어싱(aliasing) : 모니터에서 임의의 선을 그리면 계단처럼 보이는 현상

### 7. 기능 수준(feature level)
 + 기능 수준이란 개념은 Direct11에서 도입된 것으로 코드에서는 D3D_FEATURE_LEVEL 이라는 열거형으로 대표된다.
 ```c++
 enum D3D_FEATURE_LEVEL
 {
     D3D_FEATURE_LEVEL_9_1       = 0x9100,
     D3D_FEATURE_LEVEL_9_2       = 0x9100,
     D3D_FEATURE_LEVEL_9_3       = 0x9100,
     D3D_FEATURE_LEVEL_10_0     = 0x9100,
     D3D_FEATURE_LEVEL_10_1     = 0x9100,
     D3D_FEATURE_LEVEL_11_0     = 0x9100,
     D3D_FEATURE_LEVEL_11_1     = 0x9100,
 } D3D_FEATURE_LEVEL;
 ```
 + 기능수준은 GPU가 지원하는 기능들의 엄격한 집합을 정의 (예 : 기능수준 11을 지원하는 GPU는 반드시 Direct11의 기능 전체를 지원)
   - 현재 GPU의 기능 수준을 파악하기만 하면, 구체적으로 어떤 기능을 사용할수 있는지를 확실히 알수 있기 때문
   - 사용자의 하드웨어가 특정 기능 수준을 지원하지 않는 경우 응용프로그램의 샐행을 아에 포기하는 대신 더 낮은 기능 수준으로 후퇴 하는 전략을 사용 가능

### 8. DXGI(DirectX Graphics Infrastructure)
 + 여러 그래픽 API의 공통적인 그래픽 기능 작업모음

### 9. 상주성(residency)
 + Direct12에서 응용프로그램은 자원을 GPU 메모리에서 올리거나 내리는 상주성 관리가 중요
 + 성능 측면에서 한가지 주의점은 같은 자원을 짧은 시간에 GPU 메모리에 올렸다 내렸다 하는 상황을 피하는것이 중요
 + Direct12는 응용프로그램이 GPU 메모리 상주성을 제어가능
   - HRESULT ID3D12Device::MakeResident( UINT NumObjects, ID3D12Pageable *const *ppObjects);
   - HRESULT ID3D12Device::Evict( UINT NumObjects, ID3D12Pageable *const *ppObjects );
   
<br>
<br>

  