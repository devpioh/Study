package com.green.broadcastreceiver

import android.content.IntentFilter
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.pedro.library.AutoPermissions
import com.pedro.library.AutoPermissionsListener

class MainActivity : AppCompatActivity()
                    , AutoPermissionsListener
{

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val filter = IntentFilter()
        filter.addAction("android.provider.Telepony.SMS_RECEVIER")
        registerReceiver( SmsReceiver(), filter )

        AutoPermissions.Companion.loadAllPermissions(this, 101)
    }


    override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)

        AutoPermissions.Companion.parsePermissions(this, requestCode, permissions as Array<String>, this)
    }

    override fun onGranted(requestCode: Int, permissions: Array<String>) {
        Toast.makeText( this, "Permission Grant : " + permissions.size, Toast.LENGTH_LONG ).show()
    }

    override fun onDenied(requestCode: Int, permissions: Array<String>) {
        Toast.makeText( this, "Permission Denied : " + permissions.size, Toast.LENGTH_LONG ).show()
    }
}
