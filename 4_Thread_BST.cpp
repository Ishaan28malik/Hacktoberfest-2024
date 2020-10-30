/*
Create inorder threaded binary search tree and perform the traversals 
*/
#include<iostream>
using namespace std;

struct tbt
{
	int data;
	int lbit,rbit;
	struct tbt *left,*right;
	friend class thread;
};


class thread
{
	private:
		tbt *headernode, *root, *temp;
	public:
		thread()
		{
			root=headernode=temp=NULL;
		}
	void create();  //Tree creation
	tbt* createNode(); //Node creation
	void display();
	void insert(tbt*,tbt*);  //Adding the node level wise(root,temp)
	void inorder(tbt*,tbt* ); //Non-recursive in-order
	void preorder(tbt*,tbt* ); //Non-recursive pre-order
 };




tbt * thread::createNode()
{
	tbt* tmpNode =NULL;	
	tmpNode=new tbt;
	tmpNode->left= tmpNode->right=NULL;
	tmpNode->lbit= tmpNode->rbit=1;
	cout<<"\n Enter Data ";
	cin>>tmpNode->data;

	return tmpNode;
}//end of createNode()




void thread::create()  //Create
{
	tbt* temp = createNode();
	if(root==NULL)
	{
		root=temp;
		headernode=new tbt;
		headernode->data = -999;
		headernode->left=root;
		headernode->right = headernode;
		root->left=headernode;
		root->right=headernode;
	}
	else
		insert(root,temp);
}//end of create()



void thread::display()
{
	if(root==NULL)
		cout<<"Tree is Empty";
	else
	{
		cout<<"\n The Tree is : ";
		cout <<"\n Inorder :";
		inorder(root,headernode);
		cout <<"\n Preorder :";
		preorder(root,headernode);

	}
}//display()



void thread::insert(tbt *Lroot,tbt *temp)   //Function creates BST and then add node.
//Paratmeters: Lroot (level wise root) and temp node 
{
	if(temp->data<Lroot->data)//Left Subtree
	{
		if(Lroot->lbit==1)
		{
			temp->left=Lroot->left;
			temp->right=Lroot;
			Lroot->left=temp;
			Lroot->lbit=0;
		}
		else
			insert(Lroot->left,temp);  //Call to Leftsubtree for adding temp
	}//end of check for Left Subtree

	if(temp->data>Lroot->data)//Right Subtree
	{
		if(Lroot->rbit==1)
		{
			temp->right=Lroot->right;
			temp->left=Lroot;
			Lroot->rbit=0;
			Lroot->right=temp;
		}
		else
			insert(Lroot->right,temp);
	}
}//insert()


void thread :: inorder(tbt *temp,tbt *headernode){
	while(temp!=headernode)
	{
		while(temp->lbit==0) { temp=temp->left; } //Left subtree
		cout<<"  "<<temp->data;    //Print data
		while(temp->rbit==1)
		{
			temp=temp->right;   		//Threaded right child
			if(temp==headernode) return;
			cout<<"  "<<temp->data;
		}//inner while(rbit==1)
		temp=temp->right;     			//Right subtree
	}//outer while (temp!=head)
}//inorder()



void thread :: preorder(tbt *temp,tbt *headernode)
{
	while(temp!=headernode)
	{
		cout<<"  "<<temp->data;    //Print data
		while(temp->lbit==0) { temp=temp->left; cout << "  "<<temp->data; } //Left subtree
							
		while(temp->rbit==1)
		{
			temp=temp->right;   		//Threaded right child
			if(temp==headernode)
				return;
		}
		temp=temp->right;     			//Right subtree
	}
}//preorder()

int main()
{
   int choice;
   char ch='y';
   int n;
   thread th;  //object creation
   do
   {
            cout<<"\n\t Threaded Binary Tree";
            cout<<"\n1.Create \n2.Display \n";
            cin>>choice;
            switch(choice)
            {
              case 1:do
                                    {
                                      th.create();
                                       cout<<"\n Enter more data:(y/n) ";
                                       cin>>ch;
                                       }while(ch=='y');

                                    break;
             case 2:
            	 	 	 th.display();
                                    break;

            }
   cout<<"\n\n Do you want to continue with main menu?(y/n)";
   cin>>ch;
   }while(ch=='y');
}//main function


