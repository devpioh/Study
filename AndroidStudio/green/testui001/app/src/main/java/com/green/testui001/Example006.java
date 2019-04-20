package com.green.testui001;

import android.content.res.Resources;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Example006 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_example006);

        final EditText nameField = (EditText)findViewById(R.id.e006_edit_name);
        final EditText ageField = (EditText)findViewById(R.id.e006_edit_age);
        final EditText adressfield = (EditText)findViewById(R.id.e006_edit_adress);


        Button save = (Button)findViewById(R.id.e006_btn_save);
        Button close = (Button)findViewById(R.id.e006_btn_close);


        save.setOnClickListener( new Button.OnClickListener(){
            @Override
            public void onClick(View v)
            {
                String ageStr = ageField.getText().toString();
                int age = Integer.parseInt(ageStr);

                String message = String.format( "Name:%s, age:%d, adress:%s\n%s",
                        nameField.getText().toString(),
                        age,
                        adressfield.getText().toString(),
                        age > 30 ? "age is over from 30" : "age is low from 30");

                Toast.makeText( getApplicationContext(), message, Toast.LENGTH_SHORT ).show();
            }
        });

        close.setOnClickListener( new Button.OnClickListener(){
            @Override
            public void onClick(View v) {
                finish();
            }
        });
    }
}
