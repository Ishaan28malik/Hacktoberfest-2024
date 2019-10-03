package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;

public class shahisnan extends AppCompatActivity {

 /*   @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shahisnan);
    }*/

    private  ImageButton b158,b54;
    // private static WebView w1;
    private TextView textview58;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shahisnan);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);


        open();
    }

    public void open()
    {

        b54=(ImageButton)findViewById(R.id.imageButton2sha);
        b158=(ImageButton)findViewById(R.id.imageButtonsha);
        textview58=(TextView)findViewById(R.id.textViewsha);

        b158.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String url="https://www.tourmyindia.com/kumbhmela/bathing-dates.html";

                Intent myIntent = new Intent(Intent.ACTION_VIEW);
                myIntent.setData(Uri.parse(url));
                startActivity(myIntent);
            /* w1.getSettings().setJavaScriptEnabled(true);
             w1.setScrollBarStyle(View.SCROLLBARS_INSIDE_OVERLAY);
             w1.loadUrl(url);*/
            }
        });
        b54.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                 String url="https://www.youtube.com/watch?v=12DaVcxupt8";
                //String url="https://www.fb.com";
                // w1.getSettings().setLoadsImagesAutomatically(true);
                Intent myIntent = new Intent(Intent.ACTION_VIEW);
                myIntent.setData(Uri.parse(url));
                startActivity(myIntent);

            }
        });
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
