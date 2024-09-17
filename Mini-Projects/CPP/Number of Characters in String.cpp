#include <iostream>
using namespace std;

int main()
{
    string str = "C++ Programming is awesome";
    char checkCharacter = 'a';
    int count = 0; 

    for (int i = 0; i < str.size(); i++)
    {
        if (str[i] ==  checkCharacter)
        {
            ++ count; //innerloop to increase count
        }
    }

    cout << "Number of " << checkCharacter << " = " << count; //printing on console

    return 0;
}
