#include<iostream>
using namespace std;
#include<string.h>
#define MAX 10

class Hashing 
{
    char Name[20];
    char Mobile[10];
    int chain;
    
    public:
    Hashing();
    void Accept();
    void Display();
    int Hash(char[]);
    int Empty(int,Hashing[]);
    void chainingWithReplacement(Hashing[]);
    void chainingWithoutReplacement(Hashing[]);
};

int main()
{
    int choice,ch;
    char Answer;
    Hashing Student[MAX],Student1[MAX];
    Hashing h;
    do
    {
        cout<<"\nSelect:\n1.Chaining without replacement\n2.Chaining with replacement\n3:Exit";
        cout<<"\nEnter choice:";
        cin>>choice;
        switch(choice)
        {
            case 1://WITHOUT REPLACEMENT
            do
            {
                h.chainingWithoutReplacement(Student);
                cout<<"\nDo you want to continue?\n1.Yes\n2.No  ";
                cin>>ch;
                while(ch>2 || ch<1)
                {
                    cout<<"\nWrong choice!Please re-enter: ";
                    cin>>ch;
                }
            }
            while(ch!=2);    
	        break;

            case 2://WITH REPLACEMENT
            do
            {
                h.chainingWithReplacement(Student1);
                cout<<"\nDo you want to continue?\n1.Yes\n2.No  ";
                cin>>ch;
                while(ch>2 || ch<1)
                {
                    cout<<"\nWrong choice!Please re-enter: ";
                    cin>>ch;
                }
            }
            while (ch!=2);        
        }
    }
    while(choice!=3);
}

Hashing::Hashing()
{
    Name[0]='\0';
    chain=-1;
    strcpy(Mobile,"-1");
}

void Hashing::Accept()
{
    int i,flag=0;
    do
    {
        cout<<"\nEnter student Name: ";
        cin>>Name;
        for(i=0;i<strlen(Name);i++)
        {
            flag=0;
            if(isalpha(Name[i])==0)
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
            cout<<"\nInvalid name entered! ";
    }
    while(flag!=0);
	
    do
    {
        flag=0;
        cout<<"\nEnter Mobile Number: ";
        cin>>Mobile;
        if(strlen(Mobile)!=10 || Mobile[0]<'6')  
            flag=1;

        else
        {
            for(i=0;i<strlen(Mobile);i++)
            {
                flag=0;
                if(isalpha(Mobile[i])!=0)
                {
                    flag=1;
                    break;
                }
            }
        }

        if(flag==1)
            cout<<"\nInvalid phone number entered! ";
    }
    while(flag!=0);
}
void Hashing::Display()
{ 
    cout<<"\t\t"<<Name<<"\t\t"<<Mobile<<"\t"<<chain;
}

int Hashing::Hash(char Key[])
{
    int n;
    n=Key[9]-'0';
    return n%MAX;
}

int Hashing::Empty(int Location,Hashing Student[])
{
    int i=Location;
    do
    {  
        i++; 
        i=i%MAX;
    } 
    while(strcmp(Student[i].Mobile,"-1")!=0 && i!=Location);
    return i;
}

void Hashing::chainingWithoutReplacement(Hashing Student[])
{
    int i=0,Location,Pos=-1,flag=0;
    char Answer;
    Hashing data;
    cout<<"\nHash Key\tName\tMobile No\tchain";
    for(i=0;i<MAX;i++)
    { 
        cout<<"\n"<<i<<"   ";
        Student[i].Display(); 
    }
    cout<<"\nEnter Data: ";
    data.Accept();
    Location=Hash(data.Mobile);
    
    if(strcmp(Student[Location].Mobile,"-1")==0)//Location Available
        Student[Location]=data;
    
    //LOCATION NOT EMPTY
    else
    {
        Pos=Empty(Location,Student);
        if(Pos==Location)
	          cout<<"Hash Table Full\n";
        else 
        { 
            if(Hash(Student[Location].Mobile)==Hash(data.Mobile))
            {
                i=Location;
                while(Student[i].chain!=-1)  
                    i=Student[i].chain;
                Student[Pos]=data ;
                Student[i].chain=Pos;
            }
            else
            {
                i=Location+1;
                while((i%MAX)!=Location)
                { 
	                i=i%MAX;
        	        if(Hash(Student[i].Mobile) == Hash(data.Mobile))
	                { 
                        flag=1;  
                        break;
                    }
	                i++;
                }
                if(flag!=1) 
                    Student[Pos]=data;
                else
	            {
	                while(Student[i].chain!=-1)  
                        i=Student[i].chain;
	                Student[Pos]=data;  
                    Student[i].chain=Pos;
	            }
            }
        }
    }
    cout<<"\nHash Key\tName\tMobile No\tchain";
    for(i=0;i<MAX;i++)
    {  
        cout<<"\n"<<i<<"   ";
        Student[i].Display(); 
    }
}

void Hashing::chainingWithReplacement(Hashing Student[])
{
	int Pos,T,i=0,j,Location;
	Hashing data;
	cout<<"\nHash Key\tStudent Name\t\tMobile No\tchain";
	
	for(i=0;i<MAX;i++)
	{ 
		cout<<"\n"<<i<<"   ";
		Student[i].Display(); 
	}
	
	cout<<"\n\nEnter Data : ";
	data.Accept();
	
	Location=Hash(data.Mobile);
	if(strcmp(Student[Location].Mobile,"-1")==0)
		Student[Location]=data;
	else
	{
		Pos=Empty(Location,Student);
		
		if(Pos==Location) 
			cout<<"\nHash Table Full!\n";
		else
		{
			if(Location==Hash(Student[Location].Mobile))
			{
				i=Location;
				
				while(Student[i].chain!=-1)  
					i=Student[i].chain;
					
				Student[Pos]=data;
				Student[i].chain=Pos;
			}
			else
			{
				i=Hash(Student[Location].Mobile);
				
				while(i!=Location)
				{ 
					j=i;
					i=Student[i].chain;
				}
				
				Student[Pos] = Student[Location];
				Student[j].chain = Pos;
				Student[Location] = data;
			}
		}
	}
	
	cout<<"\nHash Key\tStudent Name\t\tMobile No\t\tchain";
	for(i=0;i<MAX;i++)
	{ 
		cout<<"\n"<<i<<"   ";
		Student[i].Display();
	}
}
