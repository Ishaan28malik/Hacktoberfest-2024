package com.example.shubh.log;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;


//import org.w3c.dom.Text;

  /*  public class MainActivity extends AppCompatActivity {

        private EditText Name;
        private EditText Password;
        private TextView Info;
        private Button Login;
        private TextView userReg;
        private FirebaseAuth firebaseAuth;

        private int counter = 5;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            Name = (EditText)findViewById(R.id.etName);
            Password = (EditText)findViewById(R.id.etPassword);
            Info = (TextView)findViewById(R.id.tvInfo);
            Login = (Button)findViewById(R.id.btnLogin);
            userReg=(TextView)findViewById(R.id.tvRegister);

            Info.setText("No of attempts remaining: 5");
            firebaseAuth=FirebaseAuth.getInstance();
            FirebaseUser user=firebaseAuth.getCurrentUser();

            if(user != null){
                finish();
                startActivity(new Intent(MainActivity.this, Registration.class));
            }

            userReg.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Intent i=new Intent(MainActivity.this,Registration.class);
                    startActivity(i);
                }
            });

            Login.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    validate(Name.getText().toString(), Password.getText().toString());
                }
            });
        }

        private void validate(String userName, String userPassword){
            if((userName.equals("Admin")) && (userPassword.equals("1234"))){
                Intent intent = new Intent(MainActivity.this, second.class);
                startActivity(intent);
            }else{
                counter--;

                Info.setText("No of attempts remaining: " + String.valueOf(counter));

                if(counter == 0){
                    Login.setEnabled(false);
                }
            }
        }

    }*/
    import android.app.ProgressDialog;
import android.support.annotation.NonNull;

import com.google.android.gms.tasks.OnCompleteListener;
            import com.google.android.gms.tasks.Task;
            import com.google.firebase.auth.AuthResult;

public class MainActivity extends AppCompatActivity {

    private EditText Name;
    private EditText Password;
    private TextView Info;
    private Button Login;
    private int counter = 5;
    private TextView userRegistration;
    private FirebaseAuth firebaseAuth;
    private ProgressDialog progressDialog;
    private TextView forgotPassword;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Name = (EditText)findViewById(R.id.etName);
        Password = (EditText)findViewById(R.id.etUserPassword);
        Info = (TextView)findViewById(R.id.tvInfo);
        Login = (Button)findViewById(R.id.btnLogin);
        userRegistration = (TextView)findViewById(R.id.tvRegister);
        forgotPassword = (TextView)findViewById(R.id.tvForgotPassword);

        Info.setText("No of attempts remaining: 5");

        firebaseAuth = FirebaseAuth.getInstance();
        progressDialog = new ProgressDialog(this);

        FirebaseUser user = firebaseAuth.getCurrentUser();

        if(user != null){
            finish();
            startActivity(new Intent(MainActivity.this, second.class));
        }

        Login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                validate(Name.getText().toString(), Password.getText().toString());
            }
        });

        userRegistration.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(MainActivity.this, Registration.class));
            }
        });

        forgotPassword.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(MainActivity.this, Password.class));
            }
        });
    }

    private void validate(String userName, String userPassword) {

        progressDialog.setMessage("welcome to darshan!");
        progressDialog.show();

        firebaseAuth.signInWithEmailAndPassword(userName, userPassword).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if(task.isSuccessful()){
                    progressDialog.dismiss();
                    //Toast.makeText(MainActivity.this, "Login Successful", Toast.LENGTH_SHORT).show();
                    checkEmailVerification();
                }else{
                    Toast.makeText(MainActivity.this, "Login Failed", Toast.LENGTH_SHORT).show();
                    counter--;
                    Info.setText("No of attempts remaining: " + counter);
                    progressDialog.dismiss();
                    if(counter == 0){
                        Login.setEnabled(false);
                    }
                }
            }
        });


    }

    private void checkEmailVerification(){
        FirebaseUser firebaseUser = firebaseAuth.getInstance().getCurrentUser();
        Boolean emailflag = firebaseUser.isEmailVerified();

        startActivity(new Intent(MainActivity.this, second.class));

//        if(emailflag){
//            finish();
//            startActivity(new Intent(MainActivity.this, second.class));
//        }else{
//            Toast.makeText(this, "Verify your email", Toast.LENGTH_SHORT).show();
//            firebaseAuth.signOut();
//        }
    }

}

