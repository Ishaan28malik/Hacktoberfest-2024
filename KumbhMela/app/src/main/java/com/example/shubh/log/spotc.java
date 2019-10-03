package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageView;

public class spotc extends AppCompatActivity {

    private ImageView v1,v2;

    public void init()
    {
        v1=(ImageView)findViewById(R.id.imagexx);
        v2=(ImageView)findViewById(R.id.imageyy);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_spotc);

        init();

        v1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String url="https://www.olacab.com";
                Intent myIntent = new Intent(Intent.ACTION_VIEW);
                myIntent.setData(Uri.parse(url));
                startActivity(myIntent);

            }
        });

        v2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String url="http://www.allahabad.gov.in/en/details/all-saint%E2%80%99s-cathedral/310030003500";
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
