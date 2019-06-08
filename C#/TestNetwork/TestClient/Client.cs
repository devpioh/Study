using System;
using System.Text;
using System.Net;
using System.Net.Sockets;

namespace TestClient
{
    public class TestClients
    {
        private Socket clientSock = new Socket( AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.IP );
        private byte[] buffer;

        public bool isConnect { get; set; }
        public void Start()
        {
            try
            {
                clientSock.Connect( "localhost", 42730 );
                isConnect = true;

                Console.WriteLine("Connect Success!!!!");
            }
            catch(Exception e)
            {
                isConnect = false;
                Console.WriteLine("Error Message : " + e.Message );
            }

        }

        public void Stop()
        {
            clientSock.Close();
        }

        public void Send( string message )
        {
            if( isConnect )
            {
                buffer = Encoding.Unicode.GetBytes( message );
                
                clientSock.BeginSend( buffer, 0, buffer.Length, SocketFlags.None, new AsyncCallback(SendCallBack), null );
            }
        }


        private void SendCallBack( IAsyncResult result )
        {
            if( isConnect )
            {
                Int32 sendBytes = clientSock.EndSend( result );

                if( 0 < sendBytes )
                {
                    Byte[] msgByte = new Byte[sendBytes];
                    Array.Copy( buffer, msgByte, sendBytes );

                    Console.WriteLine( "SendMessage : {0}", Encoding.Unicode.GetString( msgByte ) );
                }
            }
        }
    }   
}