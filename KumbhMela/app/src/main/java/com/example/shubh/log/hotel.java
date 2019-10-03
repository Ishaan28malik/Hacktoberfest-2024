package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;

public class hotel extends AppCompatActivity {

    // these are the global variables
    Spinner classSpinner,classSpinner1,classSpinner2,classSpinner3;
    // string variable to store selected values
    String selectedClass, selectedDiv;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hotel);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        classSpinner = (Spinner) findViewById(R.id.classSpinner);
        classSpinner1=(Spinner)findViewById(R.id.classSpinner2) ;
        classSpinner2=(Spinner)findViewById(R.id.classSpinner3) ;
        classSpinner3=(Spinner)findViewById(R.id.spinner4) ;
       //divSpinner = (Spinner) findViewById(R.id.divSpinner);

        // Class Spinner implementing onItemSelectedListener
        classSpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener()
        {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id)
            {
                String selectedClass = parent.getItemAtPosition(position).toString();
                switch (selectedClass)
                {
                    case "Book a room":
                        // assigning div item list defined in XML to the div Spinner
                       /* divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_1)));*/
                        String url="https://www.oyorooms.com/19353-budget-oyo-12244-hotel-jk-palace-allahabad";
                        // w1.getSettings().setLoadsImagesAutomatically(true);
                        Intent myIntent = new Intent(Intent.ACTION_VIEW);
                        myIntent.setData(Uri.parse(url));
                        startActivity(myIntent);

                        break;

                    case "Show on Map":
                        /*divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_2)));*/
                        Intent myIntent1 = new Intent(hotel.this,map.class);
                        //myIntent.setData(Uri.parse(url));
                        startActivity(myIntent1);

                        break;

                    case "Book a Taxi":
                       /* divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_3)));*/
                        String url1="https://www.olacabs.com/";
                        // w1.getSettings().setLoadsImagesAutomatically(true);
                        Intent myIntent4 = new Intent(Intent.ACTION_VIEW);
                        myIntent4.setData(Uri.parse(url1));
                        startActivity(myIntent4);
                        break;

                    case "Call":
                        /*divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_4)));*/
                        final String a="8947913485";
                        Intent callIntent = new Intent(Intent.ACTION_DIAL);
                        callIntent.setData(Uri.parse("tel:"+a));
                        startActivity(callIntent);

                        break;
                }

                //set divSpinner Visibility to Visible
                //divSpinner.setVisibility(View.VISIBLE);
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent)
            {
                // can leave this empty
            }
        });
        classSpinner1.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener()
        {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id)
            {
                String selectedClass = parent.getItemAtPosition(position).toString();
                switch (selectedClass)
                {
                    case "Book a room":
                        // assigning div item list defined in XML to the div Spinner
                       /* divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_1)));*/
                        String url="https://www.oyorooms.com/2105-budget-oyo-1671-hotel-sundaram-allahabad";
                        // w1.getSettings().setLoadsImagesAutomatically(true);
                        Intent myIntent = new Intent(Intent.ACTION_VIEW);
                        myIntent.setData(Uri.parse(url));
                        startActivity(myIntent);

                        break;

                    case "Show on Map":
                        /*divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_2)));*/
                        Intent myIntent5 = new Intent(hotel.this,maptwo.class);
                        //myIntent.setData(Uri.parse(url));
                        startActivity(myIntent5);
                        break;

                    case "Book a Taxi":
                       /* divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_3)));*/
                        String url2="https://www.olacabs.com/";
                        // w1.getSettings().setLoadsImagesAutomatically(true);
                        Intent myIntent2 = new Intent(Intent.ACTION_VIEW);
                        myIntent2.setData(Uri.parse(url2));
                        startActivity(myIntent2);
                        break;

                    case "Call":
                        /*divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_4)));*/
                        final String a="8947913485";
                        Intent callIntent = new Intent(Intent.ACTION_DIAL);
                        callIntent.setData(Uri.parse("tel:"+a));
                        startActivity(callIntent);

                        break;
                }

                //set divSpinner Visibility to Visible
                //divSpinner.setVisibility(View.VISIBLE);
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent)
            {
                // can leave this empty
            }
        });
        classSpinner2.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener()
        {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id)
            {
                String selectedClass = parent.getItemAtPosition(position).toString();
                switch (selectedClass)
                {
                    case "Order online":
                        // assigning div item list defined in XML to the div Spinner
                       /* divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_1)));*/
                        String url="https://www.zomato.com/allahabad/black-out-restaurant-katra";
                        // w1.getSettings().setLoadsImagesAutomatically(true);
                        Intent myIntent = new Intent(Intent.ACTION_VIEW);
                        myIntent.setData(Uri.parse(url));
                        startActivity(myIntent);

                        break;

                    case "Show on Map":
                        /*divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_2)));*/

                        // w1.getSettings().setLoadsImagesAutomatically(true);
                       Intent myIntent9 = new Intent(hotel.this,mapthree.class);
                        //myIntent.setData(Uri.parse(url));
                        startActivity(myIntent9);
                        break;

                    case "Book a Taxi":
                       /* divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_3)));*/
                        String url7="https://www.olacabs.com/";
                        // w1.getSettings().setLoadsImagesAutomatically(true);
                        Intent myIntent7 = new Intent(Intent.ACTION_VIEW);
                        myIntent7.setData(Uri.parse(url7));
                        startActivity(myIntent7);
                        break;

                    case "Call":
                        /*divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_4)));*/
                        final String a="8947913485";
                        Intent callIntent = new Intent(Intent.ACTION_DIAL);
                        callIntent.setData(Uri.parse("tel:"+a));
                        startActivity(callIntent);

                        break;
                }

                //set divSpinner Visibility to Visible
                //divSpinner.setVisibility(View.VISIBLE);
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent)
            {
                // can leave this empty
            }
        });
        classSpinner3.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener()
        {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id)
            {
                String selectedClass = parent.getItemAtPosition(position).toString();
                switch (selectedClass)
                {
                    case "Order online":
                        // assigning div item list defined in XML to the div Spinner
                       /* divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_1)));*/
                        String url="https://www.zomato.com/allahabad/el-chico-restaurant-civil-lines";
                        // w1.getSettings().setLoadsImagesAutomatically(true);
                        Intent myIntent = new Intent(Intent.ACTION_VIEW);
                        myIntent.setData(Uri.parse(url));
                        startActivity(myIntent);

                        break;

                    case "Show on Map":
                        /*divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_2)));*/

                        // w1.getSettings().setLoadsImagesAutomatically(true);
                        Intent myIntent4 = new Intent(hotel.this,mapfour.class);
                        //myIntent.setData(Uri.parse(url));
                        startActivity(myIntent4);
                        break;

                    case "Book a Taxi":
                       /* divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_3)));*/
                        String url6="https://www.olacabs.com/";
                        // w1.getSettings().setLoadsImagesAutomatically(true);
                        Intent myIntent6 = new Intent(Intent.ACTION_VIEW);
                        myIntent6.setData(Uri.parse(url6));
                        startActivity(myIntent6);
                        break;

                    case "Call":
                        /*divSpinner.setAdapter(new ArrayAdapter<String>(MainActivity.this,
                                android.R.layout.simple_spinner_dropdown_item,
                                getResources().getStringArray(R.array.items_div_class_4)));*/
                        final String a="8947913485";
                        Intent callIntent = new Intent(Intent.ACTION_DIAL);
                        callIntent.setData(Uri.parse("tel:"+a));
                        startActivity(callIntent);

                        break;
                }

                //set divSpinner Visibility to Visible
                //divSpinner.setVisibility(View.VISIBLE);
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent)
            {
                // can leave this empty
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


