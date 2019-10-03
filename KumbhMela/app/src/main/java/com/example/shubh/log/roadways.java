package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;

public class roadways extends AppCompatActivity {

    private ImageButton imr;

    public void init()
    {
        imr=(ImageButton)findViewById(R.id.imageroad);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_roadways);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        init();
        imr.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // w1.getSettings().setLoadsImagesAutomatically(true);
                String url="https://www.justdial.com/Allahabad/Uttar-Pradesh-Roadways-in-Civil-Lines";
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
