package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class Question extends AppCompatActivity {
    TextView receive;
    Button quit, nextQ;
    RadioButton rb;
    RadioGroup radioG;
    TextView tv;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_question);
        receive = (TextView)findViewById(R.id.textView2);
        nextQ = (Button)findViewById(R.id.button4);
        quit = (Button)findViewById(R.id.button5);
        radioG = (RadioGroup)findViewById(R.id.radioGroup);
        tv = (TextView)findViewById(R.id.textView8);
        int num = Integer.parseInt(tv.getText().toString());

        String ok = "printf()";
        Intent intent = getIntent();
        String str = intent.getStringExtra("message_key");
        receive.setText(str);

        quit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent i = new Intent(getApplicationContext(),MainActivity.class);
                startActivity(i);
            }
        });

        nextQ.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int num = Integer.parseInt(tv.getText().toString());
                int temp = num;
                int radioID = radioG.getCheckedRadioButtonId();
                rb = findViewById(radioID);
                if(rb.getText().toString().equals(ok)){
                    Toast.makeText(getApplicationContext(), "Correct", Toast.LENGTH_SHORT).show();
                    num+=1;
                    String n = String.valueOf(num);
                    Intent i = new Intent(getApplicationContext(),q2.class);
                    i.putExtra("counter","" + n);
                    startActivity(i);
                }
                else{
                    String n = String.valueOf(temp);
                    Toast.makeText(getApplicationContext(), "Wrong ", Toast.LENGTH_SHORT).show();
                    Intent i = new Intent(getApplicationContext(),q2.class);
                    i.putExtra("counter","" + n);
                    startActivity(i);
                }

            }
        });

    }
}
