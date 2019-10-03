package com.example.shubh.log;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

/*public class usercomment extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_usercomment);
    }
}*/
public class usercomment
{
    public String comment;

    public usercomment(){}

    public usercomment(String comment)
    {
        this.comment=comment;
    }

    public  String getusercomment() {
        return comment;
    }

    public void setusercomment(String comment)
    {
        this.comment=comment;
    }
}