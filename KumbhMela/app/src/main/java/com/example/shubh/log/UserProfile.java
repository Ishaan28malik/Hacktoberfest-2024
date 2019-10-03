package com.example.shubh.log;

/*import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class UserProfile extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_profile);
    }
}
*/
public class UserProfile {
    public String userAge;
    public String userEmail;
    public String userName;
    public String comment;

    public UserProfile(){
    }

    public UserProfile(String userAge, String userEmail, String userName,String comment) {
        this.userAge = userAge;
        this.userEmail = userEmail;
        this.userName = userName;
        this.comment=comment;
    }

    public String getUserAge() {
        return userAge;
    }

    public void setUserAge(String userAge) {
        this.userAge = userAge;
    }

    public String getUserEmail() {
        return userEmail;
    }

    public void setUserEmail(String userEmail) {
        this.userEmail = userEmail;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getComment() {return comment;}

    public void setComment(String comment) {this.comment=comment; }
}