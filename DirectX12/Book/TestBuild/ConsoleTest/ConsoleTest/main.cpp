#include <windows.h>
#include <DirectXMath.h>
#include <DirectXPackedVector.h>
#include <iostream>


using namespace std;
using namespace DirectX;
using namespace DirectX::PackedVector;


void Test1()
{
	cout.precision(8);

	// sse2 지원하는지 체크
	if (!XMVerifyCPUSupport())
	{
		cout << "do not supported DirectX12" << endl;
		return;
	}

	XMVECTOR u = XMVectorSet(1.0f, 1.0f, 1.0f, 0.0f);
	XMVECTOR n = XMVector3Normalize(u);

	float LU = XMVectorGetX(XMVector3Length(n));

	// 수학적으로는 반드시 LU는 크기가 1이어야 한다.
	cout << "LU : " << LU << endl;

	if (1.0f == LU)
		cout << "OK, this LU Length 1" << endl;
	else
		cout << "Nope, this LU Length : " << LU << endl;

	// 1을 임의의 지수로 제곱하여도 여전히 1이어야 된다.
	float powLU = powf(LU, 1.0e6f);
	cout << "LU^(1.0e6f) : " << powLU << endl;
}



void main()
{
	Test1();
}