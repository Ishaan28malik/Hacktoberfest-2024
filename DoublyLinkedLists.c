#include<stdio.h>
#include<stdlib.h>
typedef struct Node DLL;
struct Node
{
    int data;
    DLL *next;
    DLL *prev;
}*head=NULL;
int process();
int Read_No_Nodes();
void  Traverse_DLL(DLL *);
void InsertEnd(DLL *,int);
void InsertBegin(DLL *,int);
int Read_Element_to_Insert();
DLL * InsertSpecific(DLL *, int ,int);
DLL * InsertBeforeSpecific(DLL *h, int insertBeforePos, int no);
int insertAfterPos();
int deletepos();

//Delete methods
void deleteEnd(DLL *);
void deleteBegin(DLL *);
void deleteAfterSpecific(DLL *,int);
void deleteSpecific(DLL *, int );

int main()
{
    int n, i, m, s,k,p,d;

    n = Read_No_Nodes(); // Read the number of nodes to be created;

    for(i=0;i<n;i++)
    {
       s = Read_Element_to_Insert();

       InsertEnd(head,s);

    }


    Traverse_DLL(head);


while(1){
        p= process();
switch(p){
    case 1:
        m = insertAtPos();
        k= Read_Element_to_Insert();
        head = InsertBeforeSpecific(head,m,k);
        break;

    case 2:
        m = insertAtPos();
        k= Read_Element_to_Insert();
        head = InsertSpecific(head,m,k);
        break;

    case 3:
        k= Read_Element_to_Insert();
        InsertEnd(head,k);
        break;

    case 4:
        k= Read_Element_to_Insert();
        InsertBegin(head,k);
        break;
    case 5:
         m = deletepos();
         deleteSpecific(head,m);
        break;
    case 6:
        deleteEnd(head);
        break;
    case 7:
        deleteBegin(head);
        break;

    default:
        printf("\n Error 404");
        break;

};


    Traverse_DLL(head);
}
    return 0;
}


int process(){
    int process_No;
    printf("\nSelect any one process from given belove : \n");
    printf(" 1. Insert before \n 2. Insert after \n 3. Insert End \n 4. Insert Begin \n 5. DeleteSpecific \n 6. Delete End \n 7. Delete Begin \n Process : ");
    scanf("%d",&process_No);
    return process_No;

}
    //read nodes
    int Read_No_Nodes(){
int noOfNodes;
printf("\nhow many nodes you want to allocate : ");
scanf("%d",&noOfNodes);
return noOfNodes;

 }
// element to insert in DLL
int Read_Element_to_Insert(){
    int Eleread;
  printf("\n element to insert :");
   scanf("%d",&Eleread);
   return Eleread;
}
int insertAtPos(){
int e;
printf("\nAfter/before which element you want to insert :");
scanf("%d",&e);

return e;
}
int deletepos(){
int e;
printf("\n which element you want to delete :");
scanf("%d",&e);

return e;}

void InsertEnd(DLL *h,int noToinsert){

        DLL *t= h;
    DLL *new_node=(DLL * )malloc(sizeof(DLL));

    new_node->data= noToinsert;
    new_node->next= NULL;
        new_node->prev= NULL;

    if(t==NULL){
            new_node->next = NULL;
        t=new_node;
     head= t;
      }
    else{

 while(t->next!= NULL){
    t = t->next;
    }
    t->next=new_node;
    new_node->prev=t;
    new_node->next = NULL;

    }

    }
void InsertBegin(DLL *h,int noToinsert){

        DLL *t= h;
    DLL *new_node=(DLL * )malloc(sizeof(DLL));

    new_node->data= noToinsert;
    new_node->next= NULL;
        new_node->prev= NULL;

    if(t==NULL){
            new_node->next = NULL;
        t=new_node;
     head= t;
      }
    else{
   t->prev= new_node;
   new_node->next = t;
   t= new_node;
 head= t;

}

}

 void Traverse_DLL(DLL *h){

   DLL *t2= h;
   if(h==NULL)
     printf("\nList is empty");

   else
   {
       printf("\nThe elements in list are...\n");

       while(t2!=NULL)
       {
           printf("%d\n",t2->data);
           t2 = t2->next;
       }
   }

}

//Insert At Specific position
DLL* InsertSpecific(DLL *h, int insertAtPos,int noToinsert){


    DLL *new_node=(DLL * )malloc(sizeof(DLL));

    new_node->data= noToinsert;
    new_node->next= NULL;
        new_node->prev= NULL;

    if(h==NULL){
            printf("Insertion Not possible");
            return h;

    }
    else{
            DLL *temp= h;
  while(temp->data!=insertAtPos && temp!= NULL){
      temp= temp->next;
      }


      new_node->prev=temp;
      new_node->next= temp->next;
      temp->next= new_node;
      new_node->next->prev= new_node;

    }
        return h;
    }


DLL *InsertBeforeSpecific(DLL *h, int insertBeforePos, int no){


    DLL *new_node=(DLL * )malloc(sizeof(DLL));

    new_node->data= no;
    new_node->next= NULL;
        new_node->prev= NULL;

    if(h==NULL){
            printf("Insertion Not possible");
     return h;
    }
    else{
            DLL *temp= h;
  while(temp->data!=insertBeforePos ){
      temp= temp->next;}


      new_node->prev= temp->prev;
      temp->prev->next= new_node;
      new_node->next= temp;
      temp->prev= new_node;
    }

return h;
    }



    // Deleting part from here onwards method to delete
    void deleteEnd(DLL *h){
    DLL *temp = head;
 if(head==NULL){
    printf("deletion not possible");
 }
    else{
        while(temp->next!=NULL){
         temp= temp->next;

        }
        temp->prev->next = NULL;
    }

}


void deleteBegin(DLL *h){
    DLL *temp = head;
 if(head==NULL){
    printf("deletion not possible");
 }
 else if(temp->prev== temp->next){
    temp= NULL;
 }
    else if(temp->prev!=temp->next){
        head= temp->next;
        head->prev= NULL;
    }

}

void deleteSpecific(DLL *h,int desired){

if(head==NULL){
    printf("deletion not possible");
 }
 else{ DLL* temp= head;
       DLL *ptr = temp->next;
    while(temp->next->data!=desired){
        temp= temp->next;
        ptr= ptr->next;
    }
    temp->next= ptr->next;
    ptr->next->prev= temp;
    free(ptr);
 }

}









