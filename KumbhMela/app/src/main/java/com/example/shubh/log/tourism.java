package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class tourism extends AppCompatActivity {

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
        b3=(Button)findViewById(R.id.button4);
        b4=(Button)findViewById(R.id.button5);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        b1.setOnClickListener(new View.OnClickListener(){
                                  @Override
                                  public void onClick(View v) {
                                      Intent i = new Intent(tourism.this,spota.class);

                                      startActivity(i);
                                  }



                              }
        );
        b2.setOnClickListener(new View.OnClickListener(){
                                  @Override
                                  public void onClick(View v) {
                                      Intent i = new Intent(tourism.this,spotb.class);

                                      startActivity(i);
                                  }



                              }
        );
        b3.setOnClickListener(new View.OnClickListener(){
                                  @Override
                                  public void onClick(View v) {
                                      Intent i = new Intent(tourism.this,spotc.class);

                                      startActivity(i);
                                  }



                              }
        );
        b4.setOnClickListener(new View.OnClickListener(){
                                  @Override
                                  public void onClick(View v) {
                                      /*Intent i = new Intent(tourism.this,spotd.class);

                                      startActivity(i);*/

                                      String url="http://www.allahabad.gov.in/en/destination";
                                      Intent myIntent = new Intent(Intent.ACTION_VIEW);
                                      myIntent.setData(Uri.parse(url));
                                      startActivity(myIntent);
                                  }



                              }
        );
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tourism);
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
