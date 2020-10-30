/*
A Dictionary stores keywords & its meanings. Provide facility for adding new keywords, deleting keywords, updating values of any entry. Provide facility to display whole data sorted in ascending/ Descending order. Also find how many maximum comparisons may require for finding any keyword. Use Binary Search Tree for implementation.
*/

#include <iostream>
#include<string.h>
using namespace std;

struct node{
	char k[20]; //key
	char m[20]; //meaning
	node *lc, *rc;
}*root;

class DictionaryBST{
	public:
		DictionaryBST() //constructor 
		{
			root=0;
		}
		void create();
		int search(char *); //calculate number of comparisons
		void display(node*); //indorder for asc
		void display_rev(node*);//reverse inorder for desc
		int update(char *);
		void del(char *);
		node * del(node *,char *);
		node *min(node*);
};

int main()
{
	char a;
	int ch;
	char x[20];
	DictionaryBST d;

	do
	{
		cout<<"\nMenu\n1.Create\n2.Display\n3.Search\n4.Update\n5.Delete\n6.Add new node\nEnter your choice::";
		cin>>ch;
		switch(ch)
		{
			case 1:d.create();
			break;
			
			case 6:
			cout << "Add new item to BST:";			
			d.create();
			break;
			
			case 2:
			cout<<"Dictionary Contents: ";
			cout<<"\n Ascending order :";
			d.display(root);
			cout<<"\n Descending order :";
			d.display_rev(root);
			break;

			case 3: 
			cout<<"\nEnter Keyword which u want to search:";
			cin>>x;

			if( d.search(x) == 1)
				cout<<"\nKeyword Found";
			else
				cout<<"\nKeyword Not Found";
			break;

			case 4: 
			cout<<"\nEnter Keyword which meaning  want to update:";
			cin>>x;

			if(d.update(x) == 1)
				cout<<"\nMeaning Updated";
			else
				cout<<"\nMeaning Not Found";
			break;

			case 5: 
			cout<<"\nEnter Keyword which meaning  want to delete:";
			cin>>x;
			root = d.del(root,x);
			cout<<"\n Updated DictionaryBSTtionary ::\n";
			d.display(root);
		}//switch
		cout<<"\n Display Main menu (y/n)??";
		cin>>a;
	} while(a=='y');
	return 0;
}//end of main


void DictionaryBST :: display(node *n)//Ascending order display
{
    if(n!=0)
    {
        display(n->lc);
        cout<<"\n Key Word :"<<n->k;
        cout<<"\t Meaning :"<<n->m;
        display(n->rc);
    }
}

void DictionaryBST :: display_rev(node *n) //desc order (reverse inorder)
{
    if(n!=0)
    {
        display_rev(n->rc);
        cout<<"\n Key Word :"<<n->k;
        cout<<"\t Meaning :"<<n->m;
        display_rev(n->lc);
    }
}


void DictionaryBST :: create()
{
	node *temp=0, *r=0; //temp storing node to be added; r is reprenting root
	char ch='y';
	while(ch=='y')
	{
		temp = new node();
		//Node data
		cout<<"\nEnter Keyword: ";
		cin>>temp->k;
		cout<<"\nEnter Meaning: ";
		cin>>temp->m;
		temp->lc = temp->rc = 0;

		//Locate the position for temp
		if(root == 0)
			root = temp; //set new node as root
		else{
			r=root;
			while(1)
			{
				if(strcmp(temp->k,r->k)<0)// new key is less than root
				{					
					if(r->lc==0) //empty subtree
					{
						r->lc = temp; //add new key
						break; //inner while - for traversing the levels
					}
					else
						r=r->lc; 				
				}//end of check in left subtree

				else if(strcmp(temp->k,r->k)>0)
				{
					if( r->rc == 0 ){
						r->rc = temp;
						break;
					}
					else
						r = r->rc;				
				}
			}//inner while(1)
		}//else

		cout<<"Want to add more items(y/n)";
		cin>>ch;
    }//outer while
}//create 

int DictionaryBST::search(char *temp)
{
	node *r;
	r=root;
	int c=0; //count
	while(r != 0)
	{
		c++;
		if(strcmp (temp,r->k) == 0) //Key found
		{
			cout<<"\n No of Comparisons:"<<c;
			return 1;
		}
		else if(strcmp (temp, r->k) < 0)
			r = r->lc;
		else if (strcmp (temp, r->k) > 0)
			r = r->rc;
	}//while
	return -1;  //unsuccessful search
}//search


int DictionaryBST :: update(char *temp)
{
	node *r;
	r = root;

	while(r != 0)
	{
		if(strcmp (temp,r->k) == 0)//Key found for update
		{
			cout<<"\nEnter New Meaning of Keyword "<< r->k;
			cout <<" : ";
			cin>>r->m;
			return 1;
		}
		if(strcmp (temp, r->k) < 0)
			r = r->lc;
		if(strcmp (temp, r->k) > 0)
			r = r->rc;
	}//while
	return -1;  //unsuccessful search
}//update

node* DictionaryBST :: del(node * r,char temp[20])
{
	node *t;

	if(r == 0)
	{
		cout<<"\nElement Not Found";
		return r;
	}

	if (strcmp(temp,r->k) < 0) //node to be deleted is less than root
	{
		r->lc = del(r->lc, temp); //recursive call to del with left child
		return r;
	}
	if (strcmp(temp,r->k) > 0)//node to be deleted is greater than root
	{
		r->rc = del(r->rc, temp);//recursive call to del with right child
		return r;
	}
	
	//code after finding the node to be deleted
	if (r->lc==0 && r->rc==0) // node is leaf node
	{
		t = r;
		delete t;
		return 0;  //bcoz r is a leaf node
	}

	if(r->rc==0) //node to be deleted has only left child
	{
		t = r;
		r = r->lc;
		delete t;
		return r;
	}
	else if(r->lc==0)  //node to be deleted has only right child
	{
		t = r;
		r = r->rc;
		delete t;
		return r;
	}

	//If not the above cases; node to be deleted has two children
	t = min(r->rc); //Find minimum value from right subtree
	strcpy(r->k,t->k); //Replace 
	r->rc = del(r->rc, t->k);
	return r;
}

node * DictionaryBST :: min(node *q)//minimum node
{
	while(q->lc != 0)
	{
		q = q->lc;
	}
	return q;
}
