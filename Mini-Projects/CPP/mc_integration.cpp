#include <iostream>
#include <cmath>

using namespace std;

#define R 1.0f

// PUT YOUR ONE-DIMENSIONAL FUNCTION HERE
float f(float x)
{
    float val = 9*tan(x) + 2*pow(x,3) + 7;
    return val;
}

int main()
{
    long long samples = 10000; // NUMBER OF SAMPLES
    float a, b;
    cout << "Enter the limits :" << endl;
    cin >> a >> b;
    float S = 0.0f; // INTEGRATION RESULT
    for(long long i = 0; i < samples; i++)
    {
        float r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);
        float x = a + r*(b-a);
        float fx = f(x);
        S += fx * (b-a);
    }
    
    cout << "MC Integration of f(x) from a to b is : " << S/samples << endl;
}