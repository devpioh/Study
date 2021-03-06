// Chapter01-Client-HelloWorld.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//

#include "stdafx.h"

void ErrorMessage(const char* error);

int main( int argc, char* argv[] )
{
	WSADATA wsaData;
	SOCKET hSocket;
	SOCKADDR_IN serverAddr;

	char message[30];
	int strlen = 0;
	int readLen = 0;
	int index = 0;

	if (3 != argc)
	{
		std::cout << "Usage : %s <IP> <port>" << std::endl;
		exit(1);
	}

	// init socket
	if (0 != WSAStartup(MAKEWORD(2, 2), &wsaData))
		ErrorMessage("WSAStartup() Error!");

	// make socket
	hSocket = socket(PF_INET, SOCK_STREAM, 0);
	if (INVALID_SOCKET == hSocket)
		ErrorMessage("socket() Error!");

	// connect socket
	memset(&serverAddr, 0, sizeof(serverAddr));
	serverAddr.sin_family = AF_INET;
	serverAddr.sin_addr.s_addr = inet_addr(argv[1]);//inet_pton(argv[1]);
	serverAddr.sin_port = htons(atoi(argv[2]));

	if (SOCKET_ERROR == connect(hSocket, (SOCKADDR*)&serverAddr, sizeof(serverAddr)))
		ErrorMessage("connect() Error!");

	// recieve message
	//strlen = recv(hSocket, message, sizeof(message) - 1, 0);
	while (readLen = recv(hSocket, &message[index++], 1, 0))
	{
		if (-1 == readLen)
			ErrorMessage("ReadError!!!");

		strlen += readLen;
	}


	if (-1 == strlen)
		ErrorMessage("read() Error!");

	//print server message
	std::cout << "server Message : " << message << std::endl;
	std::cout << "Function read call count : " << strlen << std::endl;

	closesocket(hSocket);
	WSACleanup();

    return 0;
}

void ErrorMessage(const char* message)
{
	std::cout << message << std::endl;
}

