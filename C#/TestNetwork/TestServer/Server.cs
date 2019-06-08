using System;
using System.Text;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;


namespace TestNet
{
    public class TestServer
    {
        private Socket mySocket;
        private IPEndPoint endPoint = new IPEndPoint( IPAddress.Any, 42730 );

        private Byte[] buffer = new Byte[1024]; // 1kb
        private Socket clientSocket;    

        // private AsyncCallback connectCallBack = new AsyncCallback( ClientConnectRequest );
        // private AsyncCallback receiveCallBack = new AsyncCallback( ClientReceiver );


        public void Start()
        {
            try
            {
                mySocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.IP);
                mySocket.Bind( endPoint );
                mySocket.Listen(5);
                mySocket.BeginAccept( new AsyncCallback(ClientConnectRequest) , null );

                Console.WriteLine("Server Start");
            }
            catch(Exception e)
            {
                Console.WriteLine( "Error Server Start : " + e.Message );
            }
        }

        public void Stop()
        {
            mySocket.Close();

            if( null != clientSocket )
                clientSocket.Close();
        }


        private void ClientConnectRequest( IAsyncResult result )
        {
            try
            {
                clientSocket = mySocket.EndAccept( result );

                clientSocket.BeginReceive( buffer, 0, buffer.Length, SocketFlags.None, new AsyncCallback( ClientReceiver ) , null);
            }
            catch( Exception e )
            {
                Console.WriteLine( "Error ClientConnectRequest : " + e.Message );
            }
        }

        private void ClientReceiver( IAsyncResult result )
        {
            Int32 receiveByte = clientSocket.EndReceive( result );
            if ( 0 < receiveByte )
            {
                Console.WriteLine( "ReceiveMessage : " + Encoding.Unicode.GetString(buffer) );
            }
        }
    }   
}