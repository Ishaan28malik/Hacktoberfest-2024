#include <bits/stdc++.h>
using namespace std;
struct node{
    int data;
    struct node* left;
    struct node* right;
};
struct node* newNode(int x)
{
    struct node* temp=new node;
    temp->data=x;
    temp->left=NULL;
    temp->right=NULL;
    return temp;
};

void inorder(struct node* temp) 
{ 
    if (!temp) 
        return; 
  
    inorder(temp->left); 
    cout << temp->data << " "; 
    inorder(temp->right); 
} 

void insert(struct node* temp,int data)
{
    std::queue<struct node*> q ;
    q.push(temp);
    while(!q.empty())
    {
        struct node* temp=q.front();
        q.pop();
        if(!temp->left)
        {
        temp->left=newNode(data);
        break;
        }
        else
        {
        q.push(temp->left);
        }
        if(!temp->right)
        {
            temp->right=newNode(data);
            break;
        }
        else{
        q.push(temp->right);
        }
    }
}

int main() {
    struct node* root = newNode(10); 
    root->left = newNode(11); 
    root->left->left = newNode(7); 
    root->right = newNode(9); 
    root->right->left = newNode(15); 
    root->right->right = newNode(8); 
  
    cout << "Inorder traversal before insertion:"; 
    inorder(root); 
  
    int key = 12; 
    insert(root, key); 
  
    cout << endl; 
    cout << "Inorder traversal after insertion:"; 
    inorder(root); 
  
    return 0; 
	
}