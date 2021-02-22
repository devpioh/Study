# SIMD (Single Instruction, Multiple Data)
## 단일 명령어 다중 데이터 처리
<br>
 한 번에 데이터 하나를 명령어 하나로 처리하는 SISD(Single Instruction, Single Data)와는 달리 <em><strong>한 번에 여러 데이터를 하나의 명령어로 처리하는 방식.</strong></em><br>
 현재 대부분의 프로그램 동작방식은 SISD 방식으로 동작한다. <br>
 이는 하나의 명령으로 하나의 데이터를 처리하는것이므로 2개의 데이터 처리를 위해서는 2번 연산된다.(n개의 데이터 처리를 위해서는 n번 연산)<br>
 하지만 SIMD의 경우 다량의 데이터가 동일 연산을 한다면 1번의 연산만으로 데이터를 처리할 수 있다.(n개의 데이터를 1번 연산)<br><br><br>

 위의 내용을 간단한 코드로 예를 들어 보면 아래와 같다.
### SISD
``` c++
void main()
{
    int arrayA[4]   = { 0, 1, 2, 3 };
    int arrayB[4]   = { 4, 5, 6, 7 };
    int result[4]    = { 0, };

    result[0]        = arrayA[0] + arrayB[0];
    result[1]        = arrayA[1] + arrayB[1];
    result[2]        = arrayA[2] + arrayB[2];
    result[3]        = arrayA[3] + arrayB[3];

    /* same code
    for(int i = 0; i < 4; i++)
        result[i]     = arrayA[i] + arrayB[i];
    */

    for(int i = 0; i < 4; i++)
        cout << i << : << result[i] << endl;
}
```
 배열의 각 요소를 덧셈 연산하여 저장하는 간단한 코드이다. 배열 요소의 덧셈 연산부분을 어셈블리어로 변환하면 아래와 같다.
```
// result[0]        = arrayA[0] + arrayB[0];
mov     tmp, [arrayA]
add      tmp, [arrayB]
mov     [result], tmp

// result[1]        = arrayA[1] + arrayB[1];
mov     tmp, [arrayA+1]
add      tmp, [arrayB+1]
mov     [result+1], tmp

// result[2]        = arrayA[2] + arrayB[2];
mov     tmp, [arrayA+2]
add      tmp, [arrayB+2]
mov     [result+2], tmp

// result[3]        = arrayA[3] + arrayB[3];
mov     tmp, [arrayA+3]
add      tmp, [arrayB+3]
mov     [result+3], tmp
```

 8번의 이동 연산과 4번의 덧셈 연산이 실행되어 총 12번 연산이 수행된다.
<br>
<br>

### SIMD
``` c++
void main()
{
    __declspec(align(16)) int arrayA[4]   = { 0, 1, 2, 3 };
    __declspec(align(16)) int arrayB[4]   = { 4, 5, 6, 7 };
    __declspec(align(16)) int result[4]    = { 0, };

    __m128i xmm0            = _mm_load_si128((__m128i*)arrayA);
    __m128i xmm1            = _mm_load_si128((__m128i*)arrayB);
    __m128i xmmResult      = _mm_add_epi32(xmm0, xmm1);
    _mm_store_si128((__m128i*)result, xmmResult);

        for(int i = 0; i < 4; i++)
            cout << i << : << result[i] << endl;
}
```
 SISD 처리 코드와 동일한 코드지만 몇몇 다른부분이 있다. <br>먼저 배열 선언부를 보면 SISD와는 다르게 align(16) 으로 배열로 선헌된 변수를 16바이트로 메모리 정렬을 하고 있다. 메모리를 정렬하는 이유는 다른 글에서 설명하기로 한다.<br>
덧셈 연산부는 SIMD 명령어로 처리한다. SISD 연산과 마찬가지로 해당 부분을 어셈블리어로 변환해보면 아래와 같다.
```
movdqa     xmm0, arrayA         // __m128i xmm0            = _mm_load_si128((__m128i*)arrayA);
movdqa     xmm1, arrayB         // __m128i xmm1            = _mm_load_si128((__m128i*)arrayB);
paddd       xmm0, xmm1         // __m128i xmmResult      = _mm_add_epi32(xmm0, xmm1);
movdqa     result,  xmm0        // _mm_store_si128((__m128i*)result, xmmResult);
```
 3번의 이동 연산과 1번의 덧셈 연산이 실행된다. 하지만 SISD와는 다르게 각 요소별로 덧셈이 이뤄지지 않고 한번에 덧셈 연산이 실행되어 총 연산 횟수는 4번이다. 

 기존 SISD 와 대비 SIMD로 구현하는 경우 성능적 으로 더욱 효율적이이라는 것을 확인이 가능하다.
 다량의 데이터나 벡터/행렬 데이터 구조 처리 시 성능적으로 아주 큰 이득을 볼 수 있다.

 하지만 SIMD는 모든 CPU에서 지원되는게 아니라 각 아키텍처 모델에 따라 SIMD를 지원한다.

* Intel / AMD 
  - MMX  :  멀티미디어 확장
  - SSE  : 스트리밍 SIMD 확장
  - AVX / AVX-512  : 고급 벡터 확장


| SIMD Extenstion | MMX | SSE | AVX | AVX-512 |
|:---|:---:|:---:|:---:|:---:|
| 레지스터 크기(bits) | 64 | 128 | 256 | 512 |
</br>

* ARM
  - NEON
