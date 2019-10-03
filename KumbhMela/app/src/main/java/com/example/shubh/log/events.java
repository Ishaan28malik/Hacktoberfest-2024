package com.example.shubh.log;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class events extends AppCompatActivity {

   /* @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_events);
    }*/

    public Button b1,b2,b3,b4;
    public TextView t1;

    /* public void fun();
     {
         t1=(TextView)findViewById(R.id.textView);
         b1=(Button)=findViewById(R.id.button2);
         b2=(Button)=findViewById(R.id.button3);
         b3=(Button)=findViewById(R.id.button4);
         b4=(Button)=findViewById(R.id.button5);
     }*/
    public void init()
    {
        // b1=(Button)findViewById(R.id.button);
        t1=(TextView)findViewById(R.id.textView);
        b1=(Button)findViewById(R.id.button2);
        b2=(Button)findViewById(R.id.button3);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        b3=(Button)findViewById(R.id.button4);
        b4=(Button)findViewById(R.id.button5);
        b1.setOnClickListener(new View.OnClickListener(){
                                  @Override
                                  public void onClick(View v) {
                                      Intent i = new Intent(events.this,shahisnan.class);

                                      startActivity(i);
                                  }



                              }
        );
        b2.setOnClickListener(new View.OnClickListener(){
                                  @Override
                                  public void onClick(View v) {
                                      Intent i = new Intent(events.this,akharas.class);

                                      startActivity(i);
                                  }



                              }
        );
        b3.setOnClickListener(new View.OnClickListener(){
                                  @Override
                                  public void onClick(View v) {
                                      Intent i = new Intent(events.this,satsang.class);

                                      startActivity(i);
                                  }



                              }
        );
        b4.setOnClickListener(new View.OnClickListener(){
                                  @Override
                                  public void onClick(View v) {
                                      Intent i = new Intent(events.this,camp.class);

                                      startActivity(i);
                                  }



                              }
        );
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_events);
        init();
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {

        switch (item.getItemId()){
            case android.R.id.home:
                onBackPressed();
        }
        return super.onOptionsItemSelected(item);
    }

}
