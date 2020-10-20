#include <bits/stdc++.h>

using namespace std;

long long helper(long long start, long long end, long long N, long long &ans){
	// cout << "start: "<<start << '\n';
	// cout << "end "<<end << '\n';
	
	if (start > end)
	{
		return ans;
	}

	long long n = N;

	long long mid = (start+end)/2;
	//cout << "mid; "<<mid << '\n';
	long long k =  mid;
	//cout << k << '\n';

	long long sharma = 0, singh = 0;

	while(n>=k && n>0){
		sharma += k;
		n = n-k;
		singh += (n)/10;
		n = n-(n)/10;
	}

	sharma += n;
	//  cout << "sharma: " <<sharma<< '\n';
	// cout <<"singh: "<<singh  << '\n';

	
	// cout << sharma << '\n';
	// cout << N/2 << '\n';
	if (2*sharma<N)	
	{
		return helper(mid+1, end, N, ans);
	}else{
		ans = k;
		//cout <<"here "<<mid  << '\n';
		return helper(start, mid-1, N, ans);
		
	}


}


int main( int argc , char ** argv )
{
	ios_base::sync_with_stdio(false) ; 
	cin.tie(NULL) ; 
	
	long long n;
	cin>>n;

	cout << helper(1, n, n, n) << '\n';


	return 0 ; 



}
