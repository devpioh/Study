using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace HexCoord
{
    public static class HexMeterices
    {
        // 육각형 구성을 단순화 하기 위해 2개의 원의 반지름을 정의
        // 육각형을 6개로 나누면 정삼각형으로 나눠지고 그 정삼각형의 높이는 내부 원의 반지름과 일하다.
        // 외부 원의 반지름은 정삼각형의 각 변과 동일한 길이를 가진다.
        // 2/srt(3) == 약 0.866025404f
        
        // 육각형 각 꼭지점을 접하는 외부의 원의 반지름
        public const float outerRadius = 10f;

        // 육각형 각 변을 접하는 내부의 원의 반지름
        public const float innerRadius = outerRadius * 0.866025404f;

        // 육각형을 구성하는 정점
        // 중심위치는 0, 0, 0
        public static Vector3[] hexCorner = 
        {
            new Vector3(0f, 0f, outerRadius),
            new Vector3(innerRadius, 0f, 0.5f * outerRadius),
            new Vector3(innerRadius, 0f, -0.5f * outerRadius),
            new Vector3(0f, 0f, -outerRadius),
            new Vector3(-innerRadius, 0f, -0.5f * outerRadius),
            new Vector3(-innerRadius, 0f, 0.5f * outerRadius),
            new Vector3(0f, 0f, outerRadius),
        };
    }
}