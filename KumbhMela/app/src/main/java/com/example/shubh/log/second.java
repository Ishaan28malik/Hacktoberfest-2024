package com.example.shubh.log;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
        import android.os.Bundle;
        import android.util.Log;
        import android.view.Menu;
        import android.view.MenuItem;
        import android.view.View;
        import android.widget.Button;
        import android.widget.TextView;
        import android.widget.Toast;

import com.github.clans.fab.FloatingActionButton;
import com.github.clans.fab.FloatingActionMenu;
import com.google.firebase.auth.FirebaseAuth;
        import com.google.firebase.auth.FirebaseUser;
        import com.google.firebase.database.DataSnapshot;
        import com.google.firebase.database.DatabaseError;
        import com.google.firebase.database.DatabaseReference;
        import com.google.firebase.database.FirebaseDatabase;
        import com.google.firebase.database.ValueEventListener;

public class second extends AppCompatActivity {

    private FirebaseAuth firebaseAuth;
    private FloatingActionButton bhistory,bevent,bhot,breach,btour;
    private Button logout,fb,b,bn;
    FloatingActionMenu materialDesignFAM;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);


        firebaseAuth = FirebaseAuth.getInstance();
        materialDesignFAM = (FloatingActionMenu) findViewById(R.id.material_design_android_floating_action_menu);
        bhistory=(FloatingActionButton)findViewById(R.id.bthistory);
        bevent=(FloatingActionButton)findViewById(R.id.buttoneve);
        bhot=(FloatingActionButton)findViewById(R.id.bthotel);
        breach=(FloatingActionButton)findViewById(R.id.btreach);
        btour=(FloatingActionButton)findViewById(R.id.btour);
        fb=(Button)findViewById(R.id.buttonfb);
        b=(Button)findViewById(R.id.button);
        bn=(Button)findViewById(R.id.buttonnot);

        logout = (Button)findViewById(R.id.btnLogout);
        bn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent lo=new Intent(second.this,notifications.class);
                startActivity(lo);
            }
        });
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent p=new Intent(second.this,comments.class);
                startActivity(p);
            }
        });
        bhistory.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(second.this,history.class);
                startActivity(i);
            }
        });

        bevent.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent k=new Intent(second.this,events.class);
                startActivity(k);
            }
        });
        bhot.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent k=new Intent(second.this,hotel.class);
                startActivity(k);
            }
        });
        breach.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent q=new Intent(second.this,travel.class);
                startActivity(q);
            }
        });
        btour.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent l=new Intent(second.this,tourism.class);
                startActivity(l);
            }
        });





        logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final String a="8947913485";
                Intent callIntent = new Intent(Intent.ACTION_DIAL);
                callIntent.setData(Uri.parse("tel:"+a));
                startActivity(callIntent);
            }
        });
        fb.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i=new Intent(second.this,fback.class);
                startActivity(i);
            }
        });
    }

    private void Logout(){
        firebaseAuth.signOut();
        finish();
        startActivity(new Intent(second.this, MainActivity.class));
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {

        switch(item.getItemId()){
            case R.id.logoutMenu:{
                Logout();
                break;
            }
            case R.id.profileMenu: {
                startActivity(new Intent(second.this, ProfileActivity.class));
                break;
            }
            case R.id.refreshMenu:{
                startActivity(new Intent(second.this,second.class));
                break;
            }
            case R.id.emergencyMenu:{
                startActivity(new Intent(second.this,Emergency.class));
                break;
            }
            case R.id.aboutMenu:{
                startActivity(new Intent(second.this,About.class));
                break;
            }

        }
        return super.onOptionsItemSelected(item);
    }
}