package com.green.testui001;

import android.app.Application;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class Example005 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_example005);


        final EditText nameField = (EditText)findViewById(R.id.field_id);
        final EditText ageField = (EditText)findViewById(R.id.field_age);
        ageField.setText( "age", TextView.BufferType.SPANNABLE);

        Button saveButton = (Button)findViewById(R.id.btn_save);
        saveButton.setText("Save");
        Button closeButton = (Button)findViewById(R.id.btn_close);
        closeButton.setText("Close");


        saveButton.setOnClickListener( new Button.OnClickListener()
        {
            @Override
            public void onClick(View v) {
                String name = nameField.getText().toString();
                name = null == name ? "" : name;
                String age = ageField.getText().toString();
                age = null == age ? "" : age;
                Toast.makeText( getApplicationContext(), "name : " + name + ", age : " + age, Toast.LENGTH_SHORT ).show();
            }
        });

        closeButton.setOnClickListener(new Button.OnClickListener()
        {
            @Override
            public void onClick(View v) {
                finish();
            }
        });
    }
}
