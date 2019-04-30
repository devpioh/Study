package com.green.kotlinApp2

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.MotionEvent

class Secondary_Activity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_secondary)

    }

    override fun onTouchEvent(event: MotionEvent?): Boolean
    {
        if( event?.action == MotionEvent.ACTION_DOWN )
        {
            Log.e("activity_secondary", "OnAction Down")

            var intent: Intent = Intent(this, MainActivity::class.java)

            startActivity(intent)
        }


        return super.onTouchEvent(event)
    }
}
