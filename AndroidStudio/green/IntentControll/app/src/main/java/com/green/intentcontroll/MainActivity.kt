package com.green.intentcontroll

import android.app.Activity
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.Toast

class MainActivity : AppCompatActivity() {

    companion object
    {
        val REQUEST_CODE_MENU: Int = 101;
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        var button = findViewById<Button>(R.id.btn_change_activity)

        button.setOnClickListener {
            var intent = Intent(applicationContext, MenuActivity::class.java )
            startActivityForResult( intent, REQUEST_CODE_MENU )
        }
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if( requestCode == REQUEST_CODE_MENU )
        {
            Toast.makeText( applicationContext,
                "Call onActivityResult() - requestCode : $requestCode, resultCode : $resultCode",
                Toast.LENGTH_SHORT ).show()

            if( resultCode == Activity.RESULT_OK )
            {
                var name = data?.getStringExtra("name" ) ?: ""
                Toast.makeText( applicationContext, "CallBack Message : $name", Toast.LENGTH_SHORT).show()
            }
        }
    }
}
