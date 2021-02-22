# SIMD 연산을 위한 벡터&행렬 사용 규칙
<br>

## XMVECTOR
### 1. 변수의 선언과 저장
   + 지역 변수나 전역 변수에는 XMVECTOR를 사용한다.
   + 클래스 자료 멤버에는 XMFLOAT2나 XMFLOAT3, XMFLOAT4를 이용한다.
   + 계산을 수행하기 전에 저장 함수들을 이용해서 XMFLOATn를 XMVECTOR로 변환 한다.
   + XMVECTOR 인스턴스들로 계산을 수행한다.
   + 저장 함수들을 이용해서 XMVECTOR를 XMFLAOT로 변환 한다.

<br>
<br>

### 2.  XMVECTOR, XMFLOATn에 데이터를 저장하는 방법
   + XMFLOATn를 XMVECTOR에 저장
     - XMLoadFloatn( const XMFLOATn* pSorce ) 
   + XMVECTOR를 XMFLOATn에 저장
     - XMStoreFloatn( XMFLOATn* pDestination, FXMVECTOR v ) 
   + XMVECTOR의 각 성분 요소를 접근하거나 변경할때
     - XMVectorGetc( FXMVECTOR v )
     - XMVectorSetc( FXMVECTOR v )

* 각 변수/함수명 뒤에 n/c 의 경우는 차원의 수 혹은 좌표축
  * XMFLOATn  ==> XMFLOAT2
  * XMVectorGetc(FXMVECTOR v) ==> XMVectorGetX(FXMVECTOR v)

<br>
<br>

### 3. 매개변수 전달
   * XMVECTOR를 인스턴스를 인수로 해서 함수 호출시 효율성을 위해 스택이 아닌 SSE/SSE2 레지스터를 통해 함수로 전달이 되어야 된다.
   * 전달 가능한 인수의 개수는 플랫폼(32bit Windows, 64bit Windows, Windows RT등)과 컴파일러에 따라 다르다.
   * 플랫폼/컴파일러의 의존성을 없애기 위해, XMVECTOR의 매개변수는 FXMVECTOR/GXMVECTOR/HXMVECTOR/CXMVECTOR라는 형식을 사용,
   * SSE/SSE2 레지스터 활용을 위한 호출규약도 컴파일러마다 다르므로 의존성을 제거를 위해 함수 이름앞에다 반드시 XM_CALLCONV 라는 호출 규약 지시자를 붙인다.
   * 함수가 XMVECTOR를 매개변수로 받을때 갯수에 따라 사용되는 형식의 규칙은 다음과 같다.
     + 1, 2, 3 번째의 매개변수는 반드시 FXMVECTOR 형식을 사용.
     + 4 번째 매개변수는 반드시 GXMVECTOR 형식을 사용.
     + 5, 6 번째 매개변수는 반드시 HXMVECTOR 형식을 사용.
     + 그 이상의 매개변수는 반드시 CXMVECTOR 형식을 사용.
     + 예)
         ```c++
         void XM_CALLCONV CustomFunc(    // 의존성 제거를 위해 함수명 앞에 XM_CALLCONV 지시자를 붙인다.
            FXMVECTOR v1,
            FXMVECTOR v2, 
            FXMVECTOR v3,                       // 1, 2, 3번 매개변수는 규칙에 따라 FXMVECTOR 형식 사용.
            GXMVECTOR v4,                      // 4 번 매개변수는 규칙에 따라 GXMVECTOR 형식 사용.
            HXMVECTOR v5,
            HXMVECTOR v6,                      // 5, 6번 매개변수는 규칙에 따라 HXMVECTOR 형식을 사용.
            CXMVECTOR v7,
            CXMVECTOR v8,
            CXMVECTOR v9 );                     // 그 이상의 매개변수들은 규칙에 따라 CXMVECTOR 형식을 사용.
         ```

   * 생성자의 경우에는 조금 다른 규칙이 적용된다.
     + 생성자 앞에는 XM_CALLCONV를 붙이지 않는다.
     + 1, 2, 3 매개변수는 동일하게 FXMVECTOR 형식을 사용하지만 그 이상의 매개변수는 CXMVECTOR 형식을 사용한다.
     + 예)
         ```c++
         MYCUSTOMDATA(                       // 생성자이므로 XM_CALLCONV 지시자를 붙이지 않는다.
            FXMVECTOR v1,
            FXMVECTOR v2, 
            FXMVECTOR v3,                       // 1, 2, 3번 매개변수는 규칙대로 FXMVECTOR 형식을 사용.
            CXMVECTOR v4,
            CXMVECTOR v5,
            CXMVECTOR v6,
            CXMVECTOR v7,
            CXMVECTOR v8,
            CXMVECTOR v9 );                     // 그 이상의 매개변수들은 CXMVECTOR 형식을 사용한다.
         ```

   * 만약 매개변수 중간에 다른 형식의 데이터를 받는 경우에도 같은 규칙을 적용한다.
     + 예)
         ```c++
         void XM_CALLCONV CustomFunc2(
            float f1,                                   // float
            FXMVECTOR v1, 
            FXMVECTOR v2,                       
            float f2,                                  // float
            FXMVECTOR v3,                       // 1, 4번 매개변수 데이터가 float이지만 무시하고 XMVECTOR의 개수만 적용된다. 2, 3, 5번 매개변수는 XMVECTOR 이므로 FXMVECTOR 형식을 사용한다.
            float f3
            GXMVECTOR v4,                      // 마찬가지로 규칙에 따라 4번째 XMVECTOR 매개변수이므로 GXMVECTOR 형식을 사용한다.
            HXMVECTOR v5);                     // 규칙에 따라 5번째이므로 HXMVECTOR를  사용한다.
         );
         ``` 
   
<br>
<br>

### 4. 상수 벡터
   * 정수 데이터인 경우에는 XMVECTOR32 형식을 사용한다. 예) static const XMVECTOR32 g_vZero = { 0, 0, 0, 0 }    
   * 실수 데이터인 경우에는 XMVECTORF32 형식을 사용한다. 예) XMVECTORF32 vHalf = {0.5f, 0.5f, 0.5f, 0.5f};
   * {}를 이용한 초기화 구문의 경우에도 적용된다.
   
<br>

* 스칼라가 반환 값인  함수(내적 연산 함수등)인 경우에도 XMVECTOR를 반환하는 함수를 볼 수 있다.<br>
이는 스칼라 연산으로 인한 SIMD 벡터 연산 전환을 최소화 하려는 것이다. 계산 도중 최대한 모든 연산을 SIMD로 유지하는것이 더 효율적이다.

<br>
<br>
<br>

## XMMATRIX
### 1. 변수의 선언과 저장
   + 행렬 데이터를 저장할때는 벡터의 저장과 마찬가지로 XMFLOAT4X4를 사용한다.
   + 행렬 계산은 XMFLOAT4X4를 XMMATRIX 형으로 변형하여 계산한다.
   + XMFLOAT4X4를 XMMATRIX에 저장
     - XMLoadFloat4x4(const XMFLOAT4X4* pSource)
   + XMMATRIX를 XMFLOAT4X4에 저장
     - XMStoreFloat4x4(XMFLOAT4X4* pDestination, FXMMATRIX M);

<br>
<br>

### 2. 매개변수 전달
   + 함수의 XMMATRIX 매개변수를 선언할때도 XMVECTOR 매개변수 선언규칙을 따른다.(XMVECTOR 3. 매개변수 전달참고)
   + XMMATRIX의 경우 XMVECTOR 매개변수 4 개에 해당
   + 생성자의 경우 모든 매개변수는 CXMMATRIX 형을 사용하며, XM_CALLCONV 지시자를 사용하지 않는다