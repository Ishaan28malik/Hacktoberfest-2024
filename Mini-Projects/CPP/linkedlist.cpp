/////Menu Driven Program


#include <iostream>

using namespace std;

struct node{
    public:
        int data;
        node *next;
};
node *head = NULL;
node *tail =NULL;
void addnode(int n)
{
    node *tmp = new node;
    
    tmp->data = n;
    tmp->next = NULL;
    if (head == NULL)
    {
        head = tmp;
        tail = tmp;
    }
    else
    {
        tail->next = tmp;
        tail = tmp;
    }
}
void display()
{
    node *ptr;
    ptr = head;
    while (ptr!=NULL)
    {
        cout<<ptr->data<<" ";
        ptr = ptr->next;
    }
    cout<<"\n";
}
void insertbeg(int n)
{
    node *tmp = new node;
    tmp->data = n;
    tmp->next = NULL;
    
    if (head == NULL)
    {
        head = tmp;
    }
    else{
        tmp->next = head;
        head = tmp;
        
    }
}
void insertmid(int n, int after)
{
    node *p,*temp;
    node *tmp = new node;
    tmp->data = n;
    tmp->next = NULL;
    
    p=head;
    while(p!=NULL)
    {
        if(p->data==after)
        {
            temp= p->next;
            p->next = tmp;
            tmp->next = temp;
        }
        p = p->next;
    }
}
void deletebeg()
{
    node *tmp;
    tmp=head;
    head = tmp->next;
    delete tmp;
}
void deleteend()
{
    node *prevnode,*tmp;
    tmp = head;
    
    while(tmp->next!=NULL)
    {
        prevnode = tmp;
        tmp = tmp->next;
    }
    if (tmp == head)
    {
        head == NULL;
        free(tmp);
    }
    else
    {
        prevnode->next = NULL;
        free(tmp);
    }
}
void search(int n)
{
    node *p;
    p=head;
    int count=0;
    while(p!=NULL)
    {   
        count = count+1;
        if (p->data==n)
        {
            cout<<"\nElement is present at position:"<<count;
        }
        p=p->next;
    }
}
void deletespec(int pos)
{
    node *nextnode,*tmp;
    int i=1;
    tmp = head;
    while(i<pos-1)
    {
        tmp = tmp->next;
        i++;
    }
    nextnode = tmp->next;
    tmp->next = nextnode->next;
    free(nextnode);
}
int main()
{   
    
    cout<<"Choose the option:\n";
    cout<<"1.Create Node\n";
    cout<<"2.Insert Element at beginning:\n";
    cout<<"3.Insert Element after specific Element:\n";
    cout<<"4.Delete first node\n";
    cout<<"5.Delete Element at specific position:\n";
    cout<<"6.Delete last node\n";
    cout<<"7.Search element:\n";
    cout<<"8.Display\n";
    cout<<"9.Exit\n";
    
    int key,num,pos;
    cin>>key;
    
    while(key!=9)
    {
        switch(key)
        {
            case 1:
                cout<<"Enter the element:\n";
                cin>>num;
                addnode(num);
                break;
            case 2:
                cout<<"Enter the element:\n";
                cin>>num;
                insertbeg(num);
                break;
            case 3:
                cout<<"Enter the element and the element after which you want to insert:\n";
                cin>>num>>pos;
                insertmid(num, pos);
                break;
            case 4:
                deletebeg();
                break;
            case 5:
                cout<<"Enter the position:\n";
                cin>>num;
                deletespec(num);
                break;
            case 6:
                deleteend();
                break;
            case 7:
                cout<<"Enter the element to be searched:\n";
                cin>>num;
                search(num);
                break;
            case 8:
                display();
                break;
            default:
                cout<<"Enter a valid choice:\n";
                
        }
        cout<<endl;
        cout<<"Choose the option:\n";
        cout<<"1.Create Node\n";
        cout<<"2.Insert Element at beginning:\n";
        cout<<"3.Insert Element after specific Element:\n";
        cout<<"4.Delete first node\n";
        cout<<"5.Delete Element at specific position:\n";
        cout<<"6.Delete last node\n";
        cout<<"7.Search element:\n";
        cout<<"8.Display\n";
        cout<<"9.Exit\n";
        cin>>key;
    }
    
    
    return 0;
}
