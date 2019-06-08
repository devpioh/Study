using System;

namespace TestClient
{
    class Program
    {
        static void Main(string[] args)
        {
            var client = new TestClients();
            client.Start();

            client.Send( "Hello World!!!!!!~~~" );

            client.Stop();
        }
    }
}
