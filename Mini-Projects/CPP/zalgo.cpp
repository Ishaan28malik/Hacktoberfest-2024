#include<bits/stdc++.h>
using namespace std;
int main(){
	string str = "pqopqiwpqopi";
	int n = str.length();
	vector<int> v(n, 0);
	for(int i = 1; i < n; i++){
		int j = 0;
		int k = i;
		while(str[j] == str[k]){
			j++;
			k++;
		}
		v[i] = j;
		k = i + 1;
		int k1 = 1;
		bool flag = false;
		while(k1 < j){
			if(v[k1] > (j - k1))
			{
				flag = true;
				break;
			}
			v[k] = v[k1]; 
			k++; k1++;
		}
		if(!flag)
			i = i + j;
		else
			i = i + k1;
	}
	for(int i = 0; i < n; i++){
		cout << str[i] << " ";
	}
	cout << endl;
	for(auto x : v){
		cout << x << " "; 
	}
	return 0;
}