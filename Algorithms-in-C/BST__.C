#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

typedef struct Node
{
	int data;
	struct Node *left;
	struct Node *right;
}node;

node *getnode(int);
node *bst_insert(node *,int);
node *bst_del(node *,int);
void postorder(node *);
void inorder(node *);
void preorder(node *);
node *inorder_succ(node *);

void main()
{
	node *root=NULL,*nn;
	int ch,data;
	do
	{
		clrscr();
		printf("\n\t ****MENU****");
		printf("\n (1)Insert in BST");
		printf("\n (2)Delete from BST");
		printf("\n (3)Preorder traversal of BST");
		printf("\n (4)Inorder traversal of BST");
		printf("\n (5)Postorder traversal of BST");
		printf("\n (6)Exit");
		printf("\n Enter your choice(1..6) : ");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1://insertion
				printf("\n Enter the data to be inserted : ");
				scanf("%d",&data);
				root=bst_insert(root,data);
				break;
			case 2://deletion
				printf("\n Enter the data to be deleted : ");
				scanf("%d",&data);
				root=bst_del(root,data);
				break;
			case 3://preorder
				preorder(root);
				getch();
				break;
			case 4://inorder
				inorder(root);
				getch();
				break;
			case 5://post order
				postorder(root);
				getch();
				break;
			case 6://exit
				exit(0);
		}
	}while(1);
}

node *getnode(int data)
{
	node *nn;
	nn=(node *)malloc(sizeof(node));
	nn->data=data;
	nn->left=NULL;
	nn->right=NULL;
	return nn;
}

node *bst_insert(node *root,int data)
{
	if(root==NULL)
	{
		root=getnode(data);
		return root;
	}
	if(root->data > data)
		root->left=bst_insert(root->left,data);
	else if(root->data < data)
		root->right=bst_insert(root->right,data);
	else
		printf("\n DUPLICATE DATA NOT ALLOWED!!");
	return root;
}

void preorder(node *root)
{
	if(root==NULL)
		return;
	printf("%d ",root->data);
	preorder(root->left);
	preorder(root->right);
}

void inorder(node *root)
{
	if(root==NULL)
		return;
	inorder(root->left);
	printf("%d ",root->data);
	inorder(root->right);
}

void postorder(node *root)
{
	if(root==NULL)
		return;
	postorder(root->left);
	postorder(root->right);
	printf("%d ",root->data);
}

node *bst_del(node *root,int data)
{
	node *temp;
	if(root==NULL)
		return root;
	if(data<root->data)
		root->left=bst_del(root->left,data);
	else if(data>root->data)
		root->right=bst_del(root->right,data);
	else
	{
		if(root->left==NULL)
		{
			temp=root->right;
			free(root);
			return temp;
		}
		else if(root->right==NULL)
		{
			temp=root->left;
			free(root);
			return temp;
		}
		temp=inorder_succ(root->right) ;
		root->data=temp->data;
		root->right=bst_del(root->right,temp->data);
	}
	return root;
}

node *inorder_succ(node *root)
{
	while(root->left!=NULL)
		root=root->left;
	return root;
}

