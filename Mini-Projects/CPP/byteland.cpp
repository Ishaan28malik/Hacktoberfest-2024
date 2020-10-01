#include<bits/stdc++.h>
using namespace std;

//this is the solution for the problem on CodeChef called byteland. This is the implementation of the convex hull algorithm.
//Problem Code: ECJAN20I

int t;
int n, k;


struct point
{
	int x, y;
};

int orientation(point p1, point p2, point p3)
{
	int val = (p2.y - p1.y)*(p3.x - p2.x) - (p2.x - p1.x)*(p3.y - p2.y);

	if(val == 0) return 0; //collinear

	return (val > 0)? 1: 2; //clock or counter
}

int convexHull(point points[], int n)
{
	int count = 0;

	//finding the leftmost point
	int l = 0; 
    for (int i = 1; i < n; i++) 
        if (points[i].x < points[l].x) 
            l = i; 

    int p = l, q;

    do
    {
    	count+=1;

    	q = (p+1)%n;

    	for(int i=0; i<n; i++)
    	{
    		if (orientation(points[p], points[i], points[q]) == 2)
    			q = i;
    	}

    	p = q;
    } while (p != l);

    return count;

}

int main()
{

	cin>>t;
	while(t--)
	{
		cin>>n>>k;
		
		point points[n];

		for(int i=0; i<n; i++)
		{
			cin >> points[i].x >> points[i].y;
		}

		int check = convexHull(points, n);

		if(check <= k)
		{
			cout<<"YES"<<endl;
		}

		else
		{
			cout<<"NO"<<endl;
		}
	}
}