package com.example.shubh.log;

import android.app.ProgressDialog;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.w3c.dom.Text;

public class fback extends AppCompatActivity {

    private EditText feed,newcomment;
    private Button send;
    private FirebaseAuth firebaseAuth;
    private FirebaseUser firebaseUser;
    private ProgressDialog progressDialog;
    private FirebaseDatabase firebaseDatabase;
    private TextView naym,emyl,ayg;
   // String age,email,password,name;


    public void init()
    {
        feed=(EditText)findViewById(R.id.etfback);
        send=(Button)findViewById(R.id.buttonsnd);
        naym=(TextView)findViewById(R.id.tvnamm);
        emyl=(TextView)findViewById(R.id.tvemyl);
        ayg=(TextView)findViewById(R.id.tvayg);
        progressDialog = new ProgressDialog(this);
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_fback);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        init();

        firebaseAuth=FirebaseAuth.getInstance();
        firebaseUser=FirebaseAuth.getInstance().getCurrentUser();
        firebaseDatabase=FirebaseDatabase.getInstance();

        final DatabaseReference databaseReference = firebaseDatabase.getReference(firebaseAuth.getUid());

databaseReference.addValueEventListener(new ValueEventListener() {
    @Override
    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
        //usercomment uscomment=dataSnapshot.getValue(usercomment.class);
        UserProfile userprofile=dataSnapshot.getValue(UserProfile.class);
        //feed.setText(uscomment.getusercomment());
        feed.setText(userprofile.getComment());
        naym.setText(userprofile.getUserName());
        ayg.setText(userprofile.getUserAge());
        emyl.setText(userprofile.getUserEmail());

       //  String email = userprofile.getUserEmail();
      //   String name1=userprofile.getUserName();




        /* save.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {*/




               // UserProfile userProfile = new UserProfile(age, email, name,com);

             //   databaseReference.setValue(userProfile);
    }

    @Override
    public void onCancelled(@NonNull DatabaseError databaseError) {

        Toast.makeText(fback.this, databaseError.getCode(), Toast.LENGTH_SHORT).show();

    }
});

        send.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

               // UserProfile userprofile=dataSnapshot.getValue(UserProfile.class);

                String comment=feed.getText().toString().trim();
                String name = naym.getText().toString().trim();
                String age=ayg.getText().toString().trim();
                String email=emyl.getText().toString().trim();




                // UserProfile uscomment=new UserProfile(comment);
                UserProfile userProfile = new UserProfile(age, email, name ,comment);

                databaseReference.setValue(userProfile);

                finish();

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
