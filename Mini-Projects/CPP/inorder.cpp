#include<bits/stdc++.h>
using namespace std;
#define ll long long
struct node
{
    ll int data;
    node* left;
    node * right;
};
node* newnode(ll int data)
{
    node* newnode=new node();
    newnode->data=data;
    newnode->left=NULL;
    newnode->right=NULL;
    //cout<<newnode<<endl;
    return newnode;

}
void inorder(node* root)
{
    if(root==NULL)
{
    return;
}

       inorder(root->left);
       //cout<<root->data<<" ";   //for inorder(print this)

       inorder(root->right);

}
node* inser(node* root, ll int data)
{
    if(root==NULL)
    {
        root=newnode(data);
        //cout<<root<<" new node address"<<endl;
    }
    else if(data<=root->data)
    {
       root->left=inser(root->left,data);
    }
    else{
        root->right=inser(root->right,data);
    }

     return root;
}
ll int findmin(node *root)
{

    while(root->right!=NULL)
    {
        root=root->right;
    }

    return root->data;
}
bool searc(node* root,ll int data)
{
    if(root==NULL)return false;
    else if(root->data==data)return true;
    else if(data<=root->data) return searc(root->left,data);
    else return searc(root->right,data);
}
int findheight( node* root)
{

    if(root==NULL)
    {

        return -1;
    }
   int leftheight=findheight(root->left);
   int rightheight=findheight(root->right);
    return max(leftheight,rightheight)+1;
}
int main()
{

     node* root;
     root=NULL;
     root=inser(root,10);
     root=inser(root,25);
     root=inser(root,15);
     root=inser(root,7);
     root=inser(root,8);
     root=inser(root,5);
     inorder(root);
     cout<<findheight(root);
}
