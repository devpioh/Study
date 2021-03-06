// Chapter01-Server-Helloworld.cpp: 콘솔 응용 프로그램의 진입점을 정의합니다.
//

#include "stdafx.h"
void ErrorHandling(const char* error);

int main( int argc, char *argv[] )
{

	WSADATA wsaData;
	SOCKET hServerSock;
	SOCKET hclntSock;
	SOCKADDR_IN servAddr;
	SOCKADDR_IN clntAddr;

	int szClntAddr;
	char message[] = "HelloWorld!";

	if (2 != argc)
	{
		std::cout << "Usage : %s <port>" << std::endl;
		exit(1);
	}

	// init Socket version
	if (0 != WSAStartup(MAKEWORD(2, 2), &wsaData))
		ErrorHandling("WSAStartup() Error!");

	// make socket
	hServerSock = socket(PF_INET, SOCK_STREAM, 0);
	if (INVALID_SOCKET == hServerSock)
		ErrorHandling( "socket() Error!" );

	// bind socket
	memset(&servAddr, 0, sizeof(SOCKADDR_IN));
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servAddr.sin_port = htons(atoi(argv[1]));
	
	if (SOCKET_ERROR == bind(hServerSock, (SOCKADDR*)&servAddr, sizeof(servAddr)))
		ErrorHandling("bind() Error!");

	//linsten client
	if (SOCKET_ERROR == listen(hServerSock, 5))
		ErrorHandling("listen() Error!");

	// accept clinet
	szClntAddr = sizeof(clntAddr);
	hclntSock = accept(hServerSock, (SOCKADDR*)&clntAddr, &szClntAddr);
	if (INVALID_SOCKET == hclntSock)
		ErrorHandling("accept() Error!");

	send(hclntSock, message, sizeof(message), 0);
	closesocket(hclntSock);
	closesocket(hServerSock);
	WSACleanup();		

    return 0;
}

void ErrorHandling(const char *Error)
{
	std::cout << Error << std::endl;
}



