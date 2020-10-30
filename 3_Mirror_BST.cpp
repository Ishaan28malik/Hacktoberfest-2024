/*
Create Binary Search tree and find its mirror image. Print original & new tree level wise. Find height & print leaf nodes
*/

#include<iostream>

using namespace std;

struct bstNode
{
	int data;
	struct bstNode *left,*right;
}*root;


class bstMirror
{
	public:
		bstMirror()
		{
			root=NULL;
		}

	bstNode* createNode(int); //Node creation
	bstNode* insert(bstNode*,int);  //Adding the node level wise
	void inorder(bstNode*); 
	void inorder_leaf(bstNode*); 

	void mirror(bstNode*);  
	void level(bstNode*);	  
	void printLevel(bstNode*, int);
	int height(bstNode* ); 
 };


bstNode* bstMirror::createNode(int data) 
{
	bstNode* tmpNode =NULL;	
	tmpNode=new bstNode;
	tmpNode->left= tmpNode->right=NULL;
	tmpNode->data = data;

	return tmpNode;
}//createNode

bstNode* bstMirror::insert(bstNode* root,int data) 
{
	if(root == NULL) 
		root = createNode(data);
	if(data<root->data)
	{ 
		root->left = insert(root->left,data);
	}
	else if(data>root->data)
	{	
		root->right = insert(root->right,data);
	}
	return root;
}//insert node

void bstMirror::inorder(bstNode *temp)
{
	if (temp != NULL)
	{
		inorder(temp->left);
		cout<<temp->data<<"  ";
		inorder(temp->right);        
	}
}//inorder

void bstMirror::inorder_leaf(bstNode *temp)
{
	if (temp != NULL)
	{
		inorder_leaf(temp->left);
		if(temp->left==NULL && temp->right==NULL)  //temp is a leaf node
			cout<<temp->data<<"  ";
		inorder_leaf(temp->right);        
	}
}//inorder for printing leaf node

int bstMirror::height(bstNode *temp)
{
	int lt,rt;
	
	if(temp == NULL)
		return 0;
	else
	{
		lt=height(temp->left);
		rt=height(temp->right);
		return max(lt, rt) + 1;
	}
	
}//height

void bstMirror::mirror(bstNode *node)  //same as postorder
{ 
	if (node==NULL)  
		return;   
	else 
	{ 
		bstNode* temp;       
		mirror(node->left); 
		mirror(node->right); 

		temp = node->left; 
		node->left  = node->right; 
		node->right = temp; 
	} 
}//mirror  

void bstMirror::printLevel(bstNode *root, int level)
{
	if (root == NULL)
		return;
	else if (level==1)
	{
		cout<<root->data<<endl; 
		return;
	}
	else if (level > 1)
	{
		printLevel(root->left,level-1);
		printLevel(root->right,level-1);
	}
}//printLevel


void bstMirror::level(bstNode *root)
{
	int h = height(root);

	for(int i=1;i<=h;i++)
		printLevel(root,i);
}//level

int main() 
{
	bstMirror bm;
	char ch='y';
	char ch_ins = 'y';
	int data,h,choice;
	while(ch=='y' || ch=='Y')
	{
		cout<<"1. Insert element"<<endl;
		cout<<"2. Display Binary Tree"<<endl;
		cout<<"3. Height of Binary Tree"<<endl;
		cout<<"4. Mirror image of Binary Tree"<<endl;
		cout<<"5. Display original and mirror image Levelwise"<<endl;	
		cout<<"6. Display Leaf Nodes"<<endl;
		cout<<"Enter your choice"<<endl;
		cin>>choice;
		switch(choice)
		{
			case 1:
				do{

					cout<<"Enter the data value :";
					cin>>data;
					root = bm.insert(root,data);
					cout <<"Do you want to add more data(y/n)? ";
					cin >> ch_ins;
				}while(ch_ins=='y');
				break;
			case 2:
				bm.inorder(root);
				cout<<endl;
				break;
			case 3:
				h = bm.height(root);
				cout<<endl<<"The height of the binary tree is : "<<h<<endl;
				break;
			case 4:
				cout<<"The mirror image of the binary tree is : "<<endl;	
				bm.mirror(root);
				bm.inorder(root);
				cout<<endl;
				break;
			case 5:
				cout<<endl<<"The levelwise display is : "<<endl;
				bm.level(root);		
				
				cout<<endl<<"The levelwise display of mirror image is : "<<endl;
				bm.mirror(root);
				bm.level(root);	
				break;
			case 6:
				bm.inorder_leaf(root);
				cout<<endl;
				break;
			default:
				cout<<"Wrong Choice"<<endl;
		}
		cout<<"Do you want to continue with main menu (y/n)? ";
		cin>>ch;
	}	
	
	return 0; 
}
