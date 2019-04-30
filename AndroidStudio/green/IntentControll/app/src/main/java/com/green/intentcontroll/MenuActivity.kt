package com.green.intentcontroll

import android.app.Activity
import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class MenuActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_menu)

        var button = findViewById<Button>(R.id.btn_action)

        button.setOnClickListener{
            var intent = Intent()
            intent.putExtra("name", "pioh")
            setResult(Activity.RESULT_OK, intent)
            finish();
        }
    }
}
