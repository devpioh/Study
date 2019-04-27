package com.green.kotlinApp2

import android.content.DialogInterface
import android.os.Bundle
import android.support.v7.app.AlertDialog
import android.support.v7.app.AppCompatActivity
import android.widget.Button
import android.widget.Toast

class UITest_Activity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_uitest)

        var button:Button = findViewById<Button>( R.id.btn_utilitytest );

        button.setOnClickListener{
            var builder = AlertDialog.Builder(this );
            builder.setTitle("Alert Message")
            builder.setMessage("Hello World")

            builder.setPositiveButton("yes", object: DialogInterface.OnClickListener{
                override fun onClick(dialog: DialogInterface?, which: Int) {
                    Toast.makeText(this@UITest_Activity, "onClick MessageBox", Toast.LENGTH_LONG).show()
                }
            })

            builder.setNegativeButton( "no", object: DialogInterface.OnClickListener{
                override fun onClick(dialog: DialogInterface?, which: Int) {
                }
            })

            builder.show();
        }
    }
}
