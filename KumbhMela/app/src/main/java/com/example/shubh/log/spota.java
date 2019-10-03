package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageView;

public class spota extends AppCompatActivity {

   private ImageView i1,i2;

   public void init()
   {
       i1=(ImageView)findViewById(R.id.imgtaxi);
       i2=(ImageView)findViewById(R.id.imgchr);
       getSupportActionBar().setDisplayHomeAsUpEnabled(true);
   }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_spota);

        init();

        i1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String url="https://www.olacab.com";
                Intent myIntent = new Intent(Intent.ACTION_VIEW);
                myIntent.setData(Uri.parse(url));
                startActivity(myIntent);

            }
        });

        i2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String url="http://www.allahabad.gov.in/en/details/anand-bhawan/310030003300";
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
