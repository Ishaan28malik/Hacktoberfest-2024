package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;

public class railways extends AppCompatActivity {

    private ImageButton img;

    public void init()
    {
        img=(ImageButton)findViewById(R.id.imagerly);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_railways);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        init();
        img.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //String url="https://www.spicejet.com/AllahabadTourism.aspx?gclid=CjwKCAjw85zdBRB6EiwAov3RivkYC33RrZg5DKRgKi0U0fGaQhBTnwzoMd8C4sB2g4JRaTjE7zQowxoC0J8QAvD_BwE";
                // w1.getSettings().setLoadsImagesAutomatically(true);
                String url="https://www.goibibo.com/trains/allahabad-junction-ald/";
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
