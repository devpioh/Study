package com.green.kotlinApp2

import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.util.Log
import android.view.GestureDetector
import android.view.MotionEvent
import android.view.View
import android.widget.TextView

class D0420_EventListener : AppCompatActivity()
{
    companion object
    {
        var textView: TextView? = null;
        fun PrintStr( message:String? ) = textView?.append( if(null!=message) message + "\n" else "" );
    }

    class Dectect : GestureDetector.OnGestureListener
    {
        override fun onDown(e: MotionEvent?): Boolean {

//            Log.d("test", "Call OnDown()");
            D0420_EventListener.PrintStr( "Call Listener onDown()" );
            return true;
        }

        override fun onShowPress(e: MotionEvent?) {
//            Log.d("test", "Call onShwoPress()" );
            D0420_EventListener.PrintStr( "Call Listener onShowPress()" );
        }

        override fun onSingleTapUp(e: MotionEvent?): Boolean {
//            Log.d("test", "Call onSingleTapUp()");
            D0420_EventListener.PrintStr( "Call Listener onSingleTapUp()" );
            return true;
        }

        override fun onScroll(e1: MotionEvent?, e2: MotionEvent?, distanceX: Float, distanceY: Float): Boolean {
//            Log.d("test", "Call onScroll()");
            D0420_EventListener.PrintStr( "Call Listener onScroll()" );
            return true;
        }

        override fun onLongPress(e: MotionEvent?) {
//            Log.d( "test", "Call onLongPress()" );
            D0420_EventListener.PrintStr( "Call Listener onLongPress()" );
        }

        override fun onFling(e1: MotionEvent?, e2: MotionEvent?, velocityX: Float, velocityY: Float): Boolean {
//            Log.d("test", "onFling");
            D0420_EventListener.PrintStr( "Call Listener onFling()" );
            return true;
        }
    }

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_d0420_eventeistener)

        D0420_EventListener.textView = findViewById<TextView>( R.id.t0420_log );
        var blueView = findViewById<View>(R.id.v0420_blue);
        var redView = findViewById<View>(R.id.v0420_red);
        var detector = GestureDetector(this, Dectect() );

        blueView.setOnTouchListener( object : View.OnTouchListener {
                override fun onTouch(v: View?, event: MotionEvent?): Boolean {

                    var curX = event?.x ?: 0;
                    var curY = event?.y ?: 0;

                    when(event?.action)
                    {
                        MotionEvent.ACTION_DOWN -> Log.d("test", "onPress  curX -> $curX, curY -> $curY");
                        MotionEvent.ACTION_MOVE -> Log.d("test", "onMove  curX -> $curX, curY -> $curY");
                        MotionEvent.ACTION_UP -> Log.d("test", "onRelease  curX -> $curX, curY -> $curY");
                        else -> Log.d("test", "event is null");
                    }

                    return true;
                }
            });

        redView?.setOnTouchListener { v, event -> detector.onTouchEvent(event); }
    }


}
