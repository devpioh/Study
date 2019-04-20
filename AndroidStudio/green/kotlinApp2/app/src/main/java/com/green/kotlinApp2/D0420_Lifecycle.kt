package com.green.kotlinApp2

import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.widget.Toast

class D0420_Lifecycle : AppCompatActivity()
{

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_orientation)

        showToast( "Call ------------ onCreate()" );
    }

    override fun onStart() {
        super.onStart()

        showToast( "Call ------------ onStart()" );
    }

    override fun onStop() {
        super.onStop()

        showToast( "Call ------------ onStop()" );
    }

    override fun onDestroy() {
        super.onDestroy()

        showToast( "Call ------------ onDestroy()" );
    }


    fun showToast(message:String?) = Toast.makeText(this, message, Toast.LENGTH_LONG ).show();
}
