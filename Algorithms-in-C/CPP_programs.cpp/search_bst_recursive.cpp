
#include<iostream>
using namespace std;
struct ll{
	int data;
	struct ll* left;
	struct ll* right;
	
};
typedef struct ll node;
node* create()
{
	node *p;
	p=new node;
	cout<<endl<<"enter the data(-1 if you don't want to):";
	cin>>p->data;
	if(p->data==-1)
	{
		return 0;
	}
	cout<<"enter the left child of"<<" "<<p->data;
	p->left=create();
	cout<<"enter the right child of"<<" "<<p->data;
	p->right=create();
	return p;
	
}
node* search_rec(node* root,int key)
{
	if(root==NULL)
	{
		return NULL;
	}
	if(key==root->data)
	{
		return root;
	}
	else if(root->data>key)
	{
		return(search(root->left,key));
	}
	else
	{
		return(search(root->right,key));
	}
}
node* search_iter(node * root, int key)
{
	while(root!=NULL)
	{
		if(key==root->data)
		{
			return root;
		}
		else if(key>root->data)
		{
			root=root->right;
		}
		else
		{
			root=root->left;
		}
	}
	return NULL;
}
void insert(node * root,int key)
{
	node* prev=NULL;
	while(root!=NULL)
	{
		prev=root;
		if(key==root->data)
		{
			cout<<"element cannot be inserted";
			return ;
		}
		else if(key>root->data)
		{
			root=root->right;
		}
		else
		{
			root=root->left;
		}
		node* q;
		q=new node;
		q->data=key;
		q->left=NULL;
		q->right=NULL;
		if(key < prev->data)
		{
			prev->left=q; 
		}
		else
		{
			prev->right=q;
		}
		
	}
}
void inorder(node* root)
{
	if(root==0)
	{
		return;
	}
	inorder(root->left);
	cout<<root->data;
	inorder(root->right);
}

int main()
{
	node* root;
	root=0;
	root=create();
	inorder(root);
	cout<<endl<<"the inorder before insertion is:"<<" ";
	insert(root,8);
	cout<<endl<<"the inorder after insertion is:"<<" ";
	inorder(root);
}
