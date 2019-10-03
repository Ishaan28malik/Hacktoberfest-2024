package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;

public class satsang extends AppCompatActivity {

  /*  @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_satsang);
    }*/

    private static ImageButton b1,b2;
    // private static WebView w1;
    private TextView textview;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_satsang);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);


        open();
    }

    public void open()
    {
        b1=(ImageButton)findViewById(R.id.imageButtons);
        b2=(ImageButton)findViewById(R.id.imageButton2s);
        textview=(TextView)findViewById(R.id.textViews);
        // textview.setMovementMethod(new ScrollingMovementMethod());
        // w1=(WebView)findViewById(R.id.webView);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // String url="https://www.tourmyindia.com/kumbhmela/";
                String url="https://www.tourmyindia.com/blog/ardh-kumbh-mela-allahabad/";
                // w1.getSettings().setLoadsImagesAutomatically(true);
                Intent myIntent = new Intent(Intent.ACTION_VIEW);
                myIntent.setData(Uri.parse(url));
                startActivity(myIntent);
            /* w1.getSettings().setJavaScriptEnabled(true);
             w1.setScrollBarStyle(View.SCROLLBARS_INSIDE_OVERLAY);
             w1.loadUrl(url);*/
            }
        });
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // String url="https://www.tourmyindia.com/kumbhmela/";
                String url="https://www.youtube.com/watch?v=iqQ_d1jTvms";
                // w1.getSettings().setLoadsImagesAutomatically(true);
                Intent myIntent = new Intent(Intent.ACTION_VIEW);
                myIntent.setData(Uri.parse(url));
                startActivity(myIntent);
            /* w1.getSettings().setJavaScriptEnabled(true);
             w1.setScrollBarStyle(View.SCROLLBARS_INSIDE_OVERLAY);
             w1.loadUrl(url);*/
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
