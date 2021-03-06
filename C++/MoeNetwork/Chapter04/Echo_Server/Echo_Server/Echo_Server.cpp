// Echo_Server.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//

#include "stdafx.h"
#include <string.h>
#include <iostream>
#include <winsock2.h>

#define BUF_SIZE 1024

void ErrorHandling(const char *msg);

int main( int argc, char *argv[] )
{
	WSADATA wsaData;
	SOCKET hServSock, hClntSock;
	SOCKADDR_IN servAdr, clntAdr;

	char message[BUF_SIZE];
	int strLen, i, clntAdrSize;

	if (2 != argc)
	{
		std::cout << "Usage : " << argv[0] << " <port>" << std::endl;
		exit(1);
	}

	if (0 != WSAStartup(MAKEWORD(2, 2), &wsaData))
	{
		ErrorHandling("WSAStartup() error!");
	}

	hServSock = socket(PF_INET, SOCK_STREAM, 0);
	if (INVALID_SOCKET == hServSock)
	{
		ErrorHandling("socket() error!");
	}

	memset(&servAdr, 0, sizeof(servAdr));
	servAdr.sin_family = AF_INET;
	servAdr.sin_addr.s_addr = htonl(INADDR_ANY);
	servAdr.sin_port = htons(atoi(argv[1]));
	
	if (SOCKET_ERROR == bind(hServSock, (SOCKADDR*)&servAdr, sizeof(servAdr)))
	{
		ErrorHandling("bind() error!");
	}


	if (SOCKET_ERROR == listen(hServSock, 5))
	{
		ErrorHandling("listen() error!");
	}

	clntAdrSize = sizeof(clntAdr);

	for (int i = 0; i < 5; i++)
	{
		hClntSock = accept(hServSock, (SOCKADDR*)&clntAdr, &clntAdrSize);

		if (-1 == hClntSock)
		{
			ErrorHandling("accept() error");
		}
		else
		{ 
			std::cout << "Connected client : " << i << std::endl;
		}

		while (0 != (strLen = recv(hClntSock, message, BUF_SIZE, 0)))
		{
			std::cout << "Message : " << message << std::endl;
			send(hClntSock, message, strLen, 0);
		}

		closesocket(hClntSock);

	}

	closesocket(hServSock);
	WSACleanup();

    return 0;
}

void ErrorHandling( const char* message )
{
	std::cout << "Error : " << message << std::endl;
	exit(1);
}

