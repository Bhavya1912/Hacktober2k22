package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class q3 extends AppCompatActivity {
    TextView receive;
    Button quit, nextQ;
    RadioButton rb;
    RadioGroup radioG;
    TextView tv;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_q2);
        receive = (TextView) findViewById(R.id.textView2);
        nextQ = (Button) findViewById(R.id.button4);
        quit = (Button) findViewById(R.id.button5);
        radioG = (RadioGroup) findViewById(R.id.radioGroup);
        tv = (TextView) findViewById(R.id.textView8);

        String ok = "printf()";
        Intent intent = getIntent();
        String str = intent.getStringExtra("message_key");
        receive.setText(str);
        String n1 = intent.getStringExtra("counter");
        tv.setText(n1);

    }
}
