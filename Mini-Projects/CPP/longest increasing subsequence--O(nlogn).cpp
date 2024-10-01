#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define w(t)            int t; cin>>t; while(t--)
#define mod 1000000007

int getBestCandidate(map<int,int>&candidates,int v){
	auto it = candidates.lower_bound(v);
	if(it == candidates.begin()){
		return 0;
	}
	it--;
	return it->second;
}

void insert(map<int,int>&candidates,int v,int adv){
	if(candidates[v] >= adv){
		return;
	}

	candidates[v] = adv;
	auto it = candidates.find(v);
	it++;

	while(it != candidates.end() && it->second <= adv){
		auto temp = it;
		it++;
		candidates.erase(temp);
	}
	return;

}

int solve(vector<int>&v,int n){
	int dp[n];

	map<int,int>candidates;
	dp[0] = 1;

	candidates[v[0]] = dp[0];

	for(int i=1;i<n;i++){
		dp[i] = 1 + getBestCandidate(candidates,v[i]);
		insert(candidates,v[i],dp[i]);
	}
	
	return *max_element(dp,dp+n);
}

int main(){
	ios_base:: sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    
    int n;
    cin>>n;
    vector<int>v(n);
    for (int i = 0; i < n; ++i)
    {
    	cin>>v[i];
    }
    cout<<solve(v,n);



    return 0;
}