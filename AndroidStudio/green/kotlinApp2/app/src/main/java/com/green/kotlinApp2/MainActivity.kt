package com.green.kotlinApp2

import android.content.Context
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.text.TextWatcher
import android.util.Log
import android.view.MotionEvent
import android.view.View

class MainActivity : AppCompatActivity()
{

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

    }

    override fun onTouchEvent(event: MotionEvent?): Boolean
    {
        if( MotionEvent.ACTION_DOWN == event?.action )
        {

            Log.e("activity_main", "OnAction Down")

            var intent :Intent = Intent( this, Secondary_Activity::class.java);

            startActivity( intent );
        }

        return super.onTouchEvent(event);
    }
}
