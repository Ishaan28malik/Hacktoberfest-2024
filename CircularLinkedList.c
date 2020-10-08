#include<stdio.h>
#include<stdlib.h>
typedef struct Node CLL;
struct Node
{
    int data;
    CLL *next;

}*head=NULL;

int Read_No_Nodes();
void addEnd(struct Node *, int);
void addBegin(struct Node *,int);
void  Traverse_CLL(struct Node *);
void InsertAfterSpecific(struct Node *,int ,int );
int Read_Element_to_Insert();
int insertAtPos();
int process();

//Delete process are mentioned from here
int deletepos();
void deleteEnd(CLL *);
void deleteBegin(CLL *);
void deleteAfterSpecific(CLL *,int);
void deleteSpecific(CLL *,int);


int main(){

int s,p,m,n;
 n = Read_No_Nodes();
   for(int i=0;i<n;i++)
    {
       s = Read_Element_to_Insert();
         addEnd(head,s);

     }

Traverse_CLL(head);
while(1){
       p= process();
   switch(p){

   case 1:
        m=insertAtPos();
        s = Read_Element_to_Insert();
        InsertAfterSpecific(head,m ,s);
        break;

   case 2:
        s = Read_Element_to_Insert();
        addEnd(head,s);
        break;

    case 3:
        s = Read_Element_to_Insert();
        addBegin(head,s);
        break;
    case 4:
        deleteBegin(head);
        break;
    case 5:
        deleteEnd(head);
        break;
    case 6:
        m= deletepos();
        deleteAfterSpecific(head,m);
        break;
    case 7:
         m= deletepos();
         deleteSpecific(head,m);
         break;

   };
    Traverse_CLL(head);
}
return 0;
}
int insertAtPos(){
int e;
printf("\nAfter which element you want to insert :");
scanf("%d",&e);

return e;
}
  int Read_No_Nodes(){
int noOfNodes;
printf("\n how many nodes you want to allocate : ");
scanf("%d",&noOfNodes);
return noOfNodes;

 }
int Read_Element_to_Insert(){

 int element;
 printf("\n  Element to insert : ");
 scanf("%d",&element);
 return element;

}
int process(){
    int process_No;
    printf("\n Select any one process from given belove type serial no. in input : \n");
    printf(" \n 1. Insert after \n 2. Insert End \n 3. Insert Begin \n 4. Delete Begin \n 5. Delete End \n 6. Delete AfterSpecific \n 7. Delete Specific \n Process : ");
    scanf("%d",&process_No);
    return process_No;

}
int deletepos(){
int e;
printf("\n  After(in case delete after), which element you want to delete :");
scanf(" %d",&e);

return e;}
void addEnd(struct Node *h, int data)
{
 struct Node *temp= (struct Node *)malloc(sizeof(struct Node));
 temp->next= NULL;
 temp->data= data;
if (head== NULL)
	{
	  head = temp;
	  temp->next = temp;
	}
	else{
        CLL *ptr= head;

        while(ptr->next!=head){
        ptr= ptr->next;
        }

       ptr-> next=temp;
       temp->next = h;
    }


}

void addBegin(struct Node *h, int data){
    struct Node *temp= (struct Node *)malloc(sizeof(struct Node));
    temp->next= NULL;
 temp->data= data;
 CLL *ptr= h;

if (head== NULL)
	{
	  head = temp;
	  temp->next =temp;
	}
	else{

        while(ptr->next!=h){
            ptr=ptr->next;
        }
        temp->next=head;
        head= temp;
        ptr->next= head;
	}
}
//Transversing
 void Traverse_CLL(CLL *h){
    CLL *ptr= h;
CLL *temp = ptr->next;
if(ptr==NULL)
    printf("LIST is empty.\n");
else if(temp== head){
     printf("\n  The elements in list are...\n");
     printf("  %d\n",ptr->data);
}
    else{
        printf("\n  The elements in list are...\n");
        while(temp!=h){
            printf("  %d\n",ptr->data);

            ptr=ptr->next;
            temp=ptr;

        }

    }

}

void InsertAfterSpecific(struct Node *h,int desired,int data){
         if(head == NULL){
      printf("Insertion Not possible");
        }
else{
      struct Node *temp= (struct Node *)malloc(sizeof(struct Node));
      temp->next= NULL;
      temp->data= data;
        CLL *ptr= h;
    while(ptr->data!=desired && ptr->next!=head){
        ptr = ptr->next;}
        if(ptr!=head){temp->next= ptr->next;
        ptr->next= temp;
        }
        else{
            printf("Element Not Found..\n");
        }

}
}

void deleteBegin(CLL *h){

  CLL *temp = h;
if(head==NULL){
    printf(" deletion not possible \n");
 }
 else if(temp->next==head){
    head= NULL;
 }
else{   while(temp->next!= head){
    temp=temp->next;
}
       head= head->next;
       temp->next= head;
}

}

void deleteEnd(CLL *h){

  CLL *temp = h;
if(head==NULL){
    printf(" deletion not possible \n");
 }
 else if(temp->next==head){
    head= NULL;
 }
else{   while(temp->next->next!= head){
    temp=temp->next;
}

       temp->next= head;
}

}

void deleteAfterSpecific(CLL *h,int desired){
   CLL *temp = h;
if(head==NULL){
    printf(" deletion not possible .\n");
 }
 else if(temp->next==head){
     printf(" deletion not possible cause there is only one element .\n");
 }
 else{
    while(temp->data!=desired && temp->next!= head){
        temp= temp->next;
    }
    temp->next= temp->next->next;
 }
 }

 void deleteSpecific(CLL *h,int desired){
     CLL *temp = h;
 if(head==NULL){
    printf(" deletion not possible .\n");
 }
 else{
    while(temp->next->data!= desired){
        temp= temp->next;
    }

     temp->next= temp->next->next;
 }
 }






