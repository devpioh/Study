package com.green.serviceandreciver

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText

class MainActivity : AppCompatActivity() {

    private var editText: EditText? = null

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        editText = findViewById<EditText>(R.id.editText)

        findViewById<Button>(R.id.button).setOnClickListener {
            var name = editText?.text?.toString() ?: ""

            var data = Intent( applicationContext, MyService::class.java ).apply {
                putExtra("command", "show")
                putExtra("name", name)
            }

            startService(data)
        }
    }
}
