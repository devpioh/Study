// NetworkConv.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <string>
#include <WinSock2.h>



int main()
{
	auto strAddr = "203.211.218.102:9190";
	char strAddrBuff[50];

	SOCKADDR_IN servAddr;
	int size;

	WSADATA wsaData;
	WSAStartup(MAKEWORD(2, 2), &wsaData);

	size = sizeof(servAddr);

	WSAStringToAddressW(strAddr, AF_INET, NULL, (SOCKADDR*)&servAddr, &size);

    return 0;
}

