#include<iostream>
using namespace std;

class Node
{
	public:
	int data;
	Node *next;
};

Node *first=NULL;

void create(int *A, int size)
{
	Node *ptr,*current_add;
	first=new Node;
	first->data=A[0];
	first->next=NULL;
	current_add=first;
	
	for(int i=1;i<size;i++)
	{
		ptr=new Node;
		ptr->data=A[i];
		ptr->next=NULL;
		current_add->next=ptr;
		current_add=ptr;
	}
}

void display()
{  
    Node *trev=first;
	while(trev)
	{
		cout<<trev->data<<"->";
		trev=trev->next;
	}
}

int delete_largest_element()
{
    Node *ptr=first;
    if(ptr==NULL || ptr->next==NULL)
    {
        return -1;
    }
    Node *prev_largest=NULL;
    Node *prev=ptr;
    Node *current_largest=ptr;
    Node *head=ptr;
    ptr=ptr->next;

    while(ptr != NULL)
    {
       if(ptr->data > current_largest->data)
       {
           prev_largest=prev;
           current_largest=ptr;
       }
       prev=ptr;
       ptr=ptr->next;
    }
     
     if(current_largest==head)
     {
         head=head->next;
     }
     else
     {
         prev_largest->next=current_largest->next;
         delete current_largest;
     }
}

int main()
{
	/*int size;
	cout<<"How Much Value You Wants Enter ? ";
	cin>>size;*/
	int arr[7]={5,4,7,6,-1,2,8};
	/*for(int i=0;i<size;i++)
	{
	  cin>>arr[i];
	}*/
	create(arr,7);
	cout<<"Original List: ";
    display();
    delete_largest_element();
    cout<<endl<<"Modified List: ";
    display();

}
