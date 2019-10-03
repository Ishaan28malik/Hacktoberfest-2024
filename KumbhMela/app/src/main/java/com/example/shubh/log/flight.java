package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;

public class flight extends AppCompatActivity {

    private ImageButton flight;
    public  void init()
    {
        flight = (ImageButton) findViewById(R.id.imgflight);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_flight);
        init();
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        flight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String url="https://www.spicejet.com/AllahabadTourism.aspx?gclid=CjwKCAjw85zdBRB6EiwAov3RivkYC33RrZg5DKRgKi0U0fGaQhBTnwzoMd8C4sB2g4JRaTjE7zQowxoC0J8QAvD_BwE";
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
