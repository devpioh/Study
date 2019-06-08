using System;

namespace TestNet
{
    class Program
    {
        static void Main(string[] args)
        {
            var myServer = new TestServer();

            myServer.Start();


            string option = string.Empty;
            while( true )
            {
                if( null != option )
                {
                    if( "quit" == option )
                    {
                        break;
                    }
                }

                option = Console.ReadLine();
            }

            myServer.Stop();
        }
    }
}
