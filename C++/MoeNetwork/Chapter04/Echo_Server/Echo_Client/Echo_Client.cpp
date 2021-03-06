// Echo_Client.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
#include <string.h>
#include <winsock2.h>

#define BUF_SIZE 1024

void ErrorMessage(const char *message);


int main( int argc, char *argv[] )
{
	WSADATA wsaData;
	SOCKET hSocket;
	SOCKADDR_IN servAdr;
	char message[BUF_SIZE];
	int strLen;

	if (3 != argc)
	{
		std::cout << "Usage : " << argv[0] << " <IP> <PORT>" << std::endl;
		exit(1);
	}

	if (0 != WSAStartup(MAKEWORD(2, 2), &wsaData))
	{
		ErrorMessage("WSAStartup() error!");
	}


	hSocket = socket(PF_INET, SOCK_STREAM, 0);
	if (INVALID_SOCKET == hSocket)
	{
		ErrorMessage("socket() error!");
	}

	memset(&servAdr, 0, sizeof(servAdr));
	servAdr.sin_family = AF_INET;
	servAdr.sin_addr.s_addr = inet_addr(argv[1]);
	servAdr.sin_port = htons(atoi(argv[2]));

	if (SOCKET_ERROR == connect(hSocket, (SOCKADDR*)&servAdr, sizeof(servAdr)))
	{
		ErrorMessage("connect() error!");
	}
	else
	{
		std::cout << "Connected !!" << std::endl;
	}

	while (true)
	{
		std::cout << "Input message (q to quit) : ";
		std::cin >> message;

		if (!strcmp(message, "q\n") || !strcmp(message, "Q\n"))
			break;

		send(hSocket, message, strlen(message), 0);
		strLen = recv(hSocket, message, BUF_SIZE - 1, 0);
		message[strLen] = 0;

		std::cout << "Message from server : " << message << std::endl;
	}

	closesocket(hSocket);
	WSACleanup();

    return 0;
}


void ErrorMessage(const char *message)
{
	std::cout << "Error : " << message << std::endl;
	exit(1);
}

