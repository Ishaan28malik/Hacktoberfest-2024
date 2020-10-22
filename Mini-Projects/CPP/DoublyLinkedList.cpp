#include<iostream>

using namespace std;

class node
{
  public:
  int data;
  node* next;
  node* prev;
};
void print(node* n)
{
  if(n==NULL)
  cout<<"Nothing in the list\n";
  else
  {
  while(n!=NULL)
  {
    cout<<n->data<<" ";
    n = n->next;
  }
  cout<<"\n";
}
}
node* pushfront(node *head,int data)
{
  if(head == NULL)
  {
    node* new_node= new node();
    new_node->data = data;
    new_node->next = NULL;
    new_node->prev = NULL;
    return new_node;
  }
  else
  {
    node* new_node= new node();
    head->prev = new_node;
    new_node->data = data;
    new_node->next = head;
    return new_node;
  }
}
node* pushlast(node *head,int data)
{
  if(head == NULL)
  {
    cout<<"Nothing in the list.Try Pushing in the front\n";
    return 0;
  }
  else
  {
    while(head->next!=NULL)
    {
      head = head->next;
    }
    node* new_node= new node();
    head->next = new_node;
    new_node->data = data;
    new_node->next = NULL;
    new_node->prev = head;
    return 0;
  }
}
node* pushmiddle(node *n,int data,int position)
{
  long count=1;
  while(n->next!=NULL)
  {
    n = n->next;
    count++;
    if(position==count)
      break;
  }
  if(n == NULL)
  {
    cout<<"Nothing in the list.Try Pushing in the front\n";
    return 0;
  }
  else if(position>count)
  {
  cout<<"No such node is present\n";
  }
  else
  {
    node* new_node= new node();
    new_node->data = data;
    new_node->next = n;
    new_node->prev = n->prev;
    n->prev->next = new_node;
    n->prev = new_node;
  }
  return 0;
}
node* popfront(node* n)
{
  if(n == NULL)
  {
    cout<<"Nothing in the list.Try Pushing in the front\n";
    return 0;
  }
  else
  {
    node* temp = n;
    n = n->next;
    n->prev = NULL;
    delete(temp);
    return n;
  }
}
node* poplast(node* n)
{
  if(n == NULL)
  {
    cout<<"Nothing in the list.Try Pushing in the front\n";
    return 0;
  }
  else
  {
    while(n->next->next!=NULL)
    {
      n = n->next;
    }
    node* temp = n->next;
    n->next = NULL;
    delete(temp);
    return 0;
  }
}
node* popmiddle(node* n,int position)
{
  long count=1;
  while(n->next!=NULL)
  {
    n = n->next;
    count++;
    if(position==count)
      break;
  }
  if(n == NULL)
  {
    cout<<"Nothing in the list.Try Pushing in the front\n";
    return 0;
  }
  else if(position>count)
  {
  cout<<"No such node is present\n";
  return 0;
  }
  else
  {
    node* todel = n;
    n->prev->next=n->next;
    n->next->prev=n->prev;
    delete(todel);
    return 0;
  }
}
int main()
{
  node* head = NULL;
  bool a = true;
  while(a)
  {
    long ch,data,Position;
    cout<<"1-PushFront\n";
    cout<<"2-PushMiddle\n";
    cout<<"3-PushLast\n";
    cout<<"4-PopFront\n";
    cout<<"5-PopMiddle\n";
    cout<<"6-PopLast\n";
    cout<<"7-Print List\n";
    cout<<"Enter your choice:";
    cin>>ch;
    switch (ch) {
      case 1:
             cout<<"\nEnter Data to be pushed:\n";
             cin>>data;
             head = pushfront(head,data);
             break;
      case 2:
             cout<<"\nEnter the Data and the Position:";
             cin>>data>>Position;
             pushmiddle(head,data,Position);
             break;
      case 3:
            cout<<"\nEnter Data to be pushed:\n";
            cin>>data;
            pushlast(head,data);
            break;
      case 4:
              head = popfront(head);
              cout<<"\nPopped front\n";
              break;
      case 5:
              cout<<"\nEnter the Position:";
              cin>>Position;
              popmiddle(head,Position);
              cout<<"\n Poped at "<<Position;
              break;
      case 6:
              poplast(head);
              cout<<"\n Poped at Last";
              break;
      case 7:
              cout<<"\nPrinting The List\n";
              print(head);
              break;
      default:
              cout<<"Wrong choice\n";
              a = false;
    }
  }
}
