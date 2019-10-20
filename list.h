typedef struct node{
	int data;
	struct node* front;
	struct node* back;
}node;

typedef struct list{
	node *head;
	node *tail;
	int count;
}list;
void init(list *);
void insert(list *,int ,int);
void traverse(list *);
void del(list *,int);
void sort(list *);
void rev(list *);
void concat(list *,list *);
void unon(list *,list *);
void remdup(list *);
