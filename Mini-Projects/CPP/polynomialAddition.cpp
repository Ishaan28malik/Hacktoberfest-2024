#include<iostream>
#include<bits/stdc++.h>

using namespace std;

class polynomialAddition
{
	public:
		struct node
		{
			int data;
			int exp;
			struct node *next;
		};
		struct node *head=NULL, *newNode, *temp;
		
		~polynomialAddition();
		
		void create();
		void traverse();
		void operator +(polynomialAddition);
};

polynomialAddition::~polynomialAddition()
{
	struct node *temp1;
	temp = head;
	while(temp != NULL)
	{
		temp1 = temp -> next;
		delete(temp);
		temp = temp1;
	}
}

void polynomialAddition::create()
{
	cout << "\n------------ CREATING NEW POLYNOMIAL ------------\n";
	head = NULL;
	char ch='y';
	while(ch == 'y')
	{
		newNode = (struct node *)malloc(sizeof(struct node));
		cout << "Enter the exponent of x : ";
		cin >> newNode -> exp;
		cout << "Enter the coefficient of x^" << newNode -> exp << " : ";
		cin >> newNode -> data;
		if(head == NULL || head -> exp <= newNode -> exp)
		{
			newNode -> next = head;
			head = newNode;
		}
		else
		{
			temp = head;
			while(temp -> next != NULL && temp -> next -> exp > newNode -> exp)
			{
				temp = temp -> next;
			}
			newNode -> next = temp -> next;
			temp -> next = newNode;
		}
		cout << "\nDo you want to enter more terms? y/n: ";
		cin >> ch;
	}
	traverse();
}

void polynomialAddition::traverse()
{
		temp = head;
		cout << endl << "POLYNOMIAL: ";
		while(temp != NULL)
		{
			cout << temp -> data << "x^" << temp -> exp;
			temp = temp -> next;
			if(temp != NULL)
				cout << " + ";
		}
		cout << endl;
}

void polynomialAddition::operator + (polynomialAddition ob2)
{
	cout << "\n------------ RESULT ------------\n";
	
	polynomialAddition ob3;
	struct node *temp1, *temp2, *temp3=NULL;
	temp1 = this -> head;
	temp2 = ob2.head;
	ob3.head = NULL;
	do
	{
		newNode = (struct node *)malloc(sizeof(struct node));
		newNode -> next = NULL;
		if(ob3.head == NULL)
		{
			temp3 = ob3.temp = newNode;
			ob3.head = temp3;
		}
		else
		{
			temp3 -> next = newNode;
			temp3 = newNode;
		}
		if(temp1 -> exp > temp2 -> exp)
		{
			temp3 -> data = temp1 -> data;
			temp3 -> exp = temp1 -> exp;
			temp1 = temp1 -> next;
		}
		else if(temp1 -> exp < temp2 -> exp)
		{
			temp3 -> data = temp2 -> data;
			temp3 -> exp = temp2 -> exp;
			temp2 = temp2 -> next;
		}
		else
		{
			temp3 -> data = temp1 -> data + temp2 -> data;
			temp3 -> exp = temp1 -> exp;
			temp1 = temp1 -> next;
			temp2 = temp2 -> next;
		}
		
	}while(temp1 && temp2);
	
	while(temp1 || temp2)
	{
		newNode = (struct node *)malloc(sizeof(struct node));
		newNode -> next = NULL;
		temp3 -> next = newNode;
		temp3 = newNode;
		if(temp1)
		{
			temp3 -> exp = temp1 -> exp;
			temp3 -> data = temp1 -> data;
			temp1 = temp1 -> next;
		}
		if(temp2)
		{
			temp3 -> exp = temp2 -> exp;
			temp3 -> data = temp2 -> data;
			temp2 = temp2 -> next;
		}
	}
	//this -> traverse();
	//ob2.traverse();
	
	ob3.traverse();
}

int main()
{
	int choice, ch;
	polynomialAddition ob1, ob2;
	cout << "\n=========== ADDITION OF TWO POLYNOMIALS ===========\n";
	
	ob1.create();
	ob2.create();
	ob1 + ob2;
	
	cout << "\n########### EXITING... ###########\n";
	cout << "\n########### MEMORY IS FREED ###########\n";
	return 0;
}