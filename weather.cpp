////predict the weather tomorrow//////sunny -> cloudy -> rainy /////////

#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{
    string s;
    cin>>s;
    string str[3]={"Sunny","Cloudy","Rainy"};
    
    if(s==str[0])
     cout<<str[1]<<endl;
     
    if(s==str[1])
     cout<<str[2]<<endl;
     
    if(s==str[2])
     cout<<str[0]<<endl;
    
    
    return 0;
}
