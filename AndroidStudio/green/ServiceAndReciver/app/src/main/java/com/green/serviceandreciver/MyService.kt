package com.green.serviceandreciver

import android.app.Service
import android.content.Intent
import android.os.IBinder
import android.util.Log
import java.lang.Exception

class MyService : Service() {


    private val tag : String = "MyService"

    override fun onBind(intent: Intent): IBinder {
        TODO("Return the communication channel to the service.")
    }

    override fun onCreate() {

        Log.d(tag, "onCreate()" )
        super.onCreate()
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int
    {
        Log.d(tag, "onStartCommand()" )

        if( null == intent )
            return Service.START_STICKY
        else
            ProcessService(intent)

        return super.onStartCommand(intent, flags, startId)
    }

    override fun onDestroy() {
        Log.d(tag, "onDestroy()" )
        super.onDestroy()
    }

    private fun ProcessService(intent: Intent)
    {
        val command = intent.getStringExtra("command")
        val name = intent.getStringExtra("name")

        Log.d( tag, "command : $command, name : $name")

        for( i in 1..5 )
        {
            try {
                Thread.sleep(1000)
            }
            catch (e:Exception)
            {
                Log.e(tag, "Error : $e")
            }

            Log.d(tag, "Waiting.... $i Seceonds." )
        }
    }
}

