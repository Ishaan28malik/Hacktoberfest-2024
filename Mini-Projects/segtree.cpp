#include <iostream>
#include<climits>
using namespace std;

int query(int *tree,int ss,int se,int qs,int qe,int index){
   /* ///Complete Overlap
    if(ss>=qs && se<=qe){
        return tree[index];
    }

    //No Overlap
    if(qe<ss || qs>se){
        return INT_MAX;
    }

    //Partial Overlap - Call both sides and update the current ans
    int mid = (ss+se)/2;
    int leftAns = query(tree,ss,mid,qs,qe,2*index);
    int rightAns  = query(tree,mid+1,se,qs,qe,2*index+1);
    return min(leftAns,rightAns);
    */

}


void buildTree(int *a,int s,int e,int *tree,int index){

    if(s==e){
        tree[index] = a[s];
        return ;
    }

    //Rec case
    int mid = (s+e)/2;
    buildTree(a,s,mid,tree,2*index);
    buildTree(a,mid+1,e,tree,2*index+1);
    tree[index] = min(tree[2*index],tree[2*index+1]);

    return;
}

int main() {

    int a[] = {1,3,2,-5,6,4};
    int n = sizeof(a)/sizeof(int);

    int *tree = new int[4*n+1];

    buildTree(a,0,n-1,tree,1);

    //Let print the tree
    for(int i=1;i<=13;i++){
        cout<<tree[i]<<" ";
    }

    int l,r;
    cin>>l>>r;
    cout<< query(tree,0,n-1,l,r,1);



    return 0;
}
