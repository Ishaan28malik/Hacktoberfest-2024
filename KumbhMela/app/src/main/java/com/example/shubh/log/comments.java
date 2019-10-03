package com.example.shubh.log;

import android.app.ProgressDialog;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;

public class comments extends AppCompatActivity {

    ListView listView;
    DatabaseReference admi;
    ProgressDialog progressDialog;
    ArrayList<String> inf;
    Button btn;
    EditText comm;
    Query m;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_comments);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        inf = new ArrayList<>();
        listView = findViewById(R.id.list);
        btn = (Button) findViewById(R.id.btcom);

        comm = (EditText) findViewById(R.id.etcomment);
        admi = FirebaseDatabase.getInstance().getReference("chat");
       // m=admi.child("chat");
        progressDialog = new ProgressDialog(this);
        progressDialog.setMessage("Loading...");
        progressDialog.show();
        final ArrayAdapter<String> arrayAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, inf);
        listView.setAdapter(arrayAdapter);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                addcom();

            }
        });

    /*    final ValueEventListener chatlistener=new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                DataSnapshot abc=dataSnapshot.child("chat");
                Iterable<DataSnapshot> chatchild=abc.getChildren();
                for(DataSnapshot x: chatchild){
                    String value= x.getValue(String.class);
                    inf.add(value);
                    arrayAdapter.notifyDataSetChanged();
                    progressDialog.dismiss();
                }

            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        };*/


/*m.addChildEventListener(new ChildEventListener() {
    @Override
    public void onChildAdded(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {
        String value= dataSnapshot.getValue(String.class);
        inf.add(value);
        arrayAdapter.notifyDataSetChanged();
        progressDialog.dismiss();
    }

    @Override
    public void onChildChanged(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {

    }

    @Override
    public void onChildRemoved(@NonNull DataSnapshot dataSnapshot) {

    }

    @Override
    public void onChildMoved(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {

    }

    @Override
    public void onCancelled(@NonNull DatabaseError databaseError) {

    }
});

*/admi.addChildEventListener(new ChildEventListener() {
    @Override
    public void onChildAdded(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {
        String value= dataSnapshot.getValue(String.class);
        inf.add(value);
        arrayAdapter.notifyDataSetChanged();
        progressDialog.dismiss();

    }

    @Override
    public void onChildChanged(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {

    }

    @Override
    public void onChildRemoved(@NonNull DataSnapshot dataSnapshot) {

    }

    @Override
    public void onChildMoved(@NonNull DataSnapshot dataSnapshot, @Nullable String s) {

    }

    @Override
    public void onCancelled(@NonNull DatabaseError databaseError) {

    }
});

     /*   admi.addChildEventListener(new ChildEventListener() {
            @Override
            public void onChildAdded(DataSnapshot dataSnapshot, String s) {


            }

            @Override
            public void onChildChanged(DataSnapshot dataSnapshot, String s) {

            }

            @Override
            public void onChildRemoved(DataSnapshot dataSnapshot) {

            }

            @Override
            public void onChildMoved(DataSnapshot dataSnapshot, String s) {

            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });*/
    }

    @Override
    protected void onStart() {
        super.onStart();




    }

    public void Navigation(View view){
        startActivity(new Intent(this,second.class));
    }
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {

        switch (item.getItemId()){
            case android.R.id.home:
                onBackPressed();
        }
        return super.onOptionsItemSelected(item);
    }

    public void addcom(){
        String comment=comm.getText().toString().trim();

        if(!TextUtils.isEmpty(comment)){
            String id=admi.push().getKey();
            //String id="chat";

          //  com obj=new com(comment);

            admi.child(id).setValue(comment);
            comm.setText("");

        }else{
            Toast.makeText(comments.this,"enter valid comment",Toast.LENGTH_SHORT).show();
        }
    } }

