#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ii vector<long long>

vector<vector<ii> > tree(100001,vector<ii>(3,ii(3))) ;

ll r,n,q;

vector<ii> multiply(vector<ii> a,vector<ii> b){
    vector<ii> C(3,vector<ll> (3));
    for(ll i=1;i<3;i++){
        for(ll j=1;j<3;j++){
            for(ll k=1;k<3;k++){
                C[i][j]+=(a[i][k]*b[k][j])%r;
                C[i][j]%=r;
            }
        }
    }
    return C;
}

void Build(vector<vector<ii> > a,ll si,ll ei,ll index){
    if(si>ei)
    return;
    if(si==ei){

        tree[index]=a[si];
        return;
    }

    ll mid=(si+ei)/2;
    Build(a,si,mid,2*index);
    Build(a,mid+1,ei,2*index+1);
    tree[index]=multiply(tree[2*index],tree[2*index+1]);

}
vector<ii> X (3,vector<ll>(3)) ;
vector<ii> query(ll si,ll ei,ll l,ll r,ll index){
    // No Overlap
    if(r<si||l>ei||si>ei){
        return X;
    }
    // Complete Overlap
    if(l<=si&&r>=ei){
        return tree[index];
    }
    ll mid=(si+ei)/2;
    vector<ii> left=query(si,mid,l,r,2*index);
    vector<ii> right=query(mid+1,ei,l,r,2*index+1);
    return multiply(left,right);

}

int main() {


    for(ll i=1;i<3;i++){
        for(ll j=1;j<3;j++){
            if(i==j)
            X[i][j]=1;
            else
            X[i][j]=0;
        }
    }
    cin>>r>>n>>q;
    vector<vector<ii> > a(n+1,vector<ii>(3,ii(3)));
    for(ll i=1;i<=n;i++){

        for(ll j=1;j<3;j++){
            for(ll k=1;k<=2;k++){
                cin>>a[i][j][k];
            }
        }

    }

    Build(a,1,n,1);

    while(q--){
        ll l,r;
        cin>>l>>r;
        vector<ii> C(3,vector<ll>(3)) ;
        C=query(1,n,l,r,1);
        for(ll i=1;i<=2;i++){
            for(ll j=1;j<=2;j++){
                cout<<C[i][j]<<" ";
            }
            cout<<endl;
        }
        cout<<endl;
    }


	return 0;
}
