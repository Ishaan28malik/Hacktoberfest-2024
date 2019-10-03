package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;

public class history extends AppCompatActivity {

  /*  @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_history);
    }*/
  private static ImageButton b1;
    // private static WebView w1;
    public TextView textview;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_history);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);


        open();
    }

    public void open()
    {
        b1=(ImageButton)findViewById(R.id.imageButton);
        textview=(TextView)findViewById(R.id.textView);
        // textview.setMovementMethod(new ScrollingMovementMethod());
        // w1=(WebView)findViewById(R.id.webView);
        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // String url="https://www.tourmyindia.com/kumbhmela/";
                String url="https://www.amarujala.com/dropped/history-of-kumbh-mela-1";
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
