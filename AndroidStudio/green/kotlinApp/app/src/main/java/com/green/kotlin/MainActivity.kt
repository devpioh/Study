package com.green.kotlin

import android.os.Bundle
import android.support.v4.content.ContextCompat
import android.support.v7.app.AppCompatActivity
import android.widget.Button
import android.widget.ImageView

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activiy_main)

       var changeButton = findViewById<Button>(R.id.changeIamge);
        var imageView = findViewById<ImageView>(R.id.imageView);
//        var count     = findViewById<EditText>(R.id.touchCounter);
//        var countClear = findViewById<Button>(R.id.tourchClearButton);

        var drawable = ContextCompat.getDrawable( this, R.drawable.mantaray )

        changeButton.setOnClickListener {

            if( imageView.drawable.equals( drawable ) )
            {
                imageView.setImageResource(R.drawable.mantaray2);
            }
            else
            {
                imageView.setImageResource(R.drawable.mantaray);
            }
        }
    }
}
