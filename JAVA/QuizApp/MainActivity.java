package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    TextView title;
    Button start, about;
    EditText editText = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        title = (TextView) findViewById(R.id.textView);
        start = (Button) findViewById(R.id.button);
        about = (Button) findViewById(R.id.button2);
        editText = (EditText) findViewById(R.id.edit);

        about.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(getApplicationContext(), AboutAct.class);
                startActivity(i);
            }
        });

        start.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String ed_text = editText.getText().toString().trim();

                if (ed_text.isEmpty() || ed_text.length() == 0 || ed_text.equals("") || ed_text == null) {
                    Toast.makeText(getApplicationContext(), "First Enter your name to start a quiz.", Toast.LENGTH_SHORT).show();
                } else {
                    Intent intent = new Intent(getApplicationContext(), Question.class);
                    intent.putExtra("message_key","Hello, " + ed_text);
                    startActivity(intent);
                }


            }
        });
    }
}