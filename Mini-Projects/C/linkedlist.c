#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int data;
  struct node *next;
} node;
typedef node *list;

void init(list*);
void append(list*, int);
void traverse(list);
void search(list, int);
int length(list);
void insertBegin(list*, int);
void insertAtPosition(list*, int, int);
void deleteBegin(list*);
void deleteAtPosition(list*, int);
void deleteEnd(list*);

int main() {
	list l1;
	int j , n, index, pos, ele;
	init(&l1);
	printf("Enter number of elements in list:");
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		printf("Enter number %d: ", i + 1);
		scanf("%d", &j);
		append(&l1, j);
	}
	traverse(l1);
	printf("Operations on Linked List\n");
	printf("1: Insert a node\n");
	printf("2: Delete a node\n");
	printf("3: Search for an element\n");
	printf("4: Length of list\n");
	printf("5: Exit\n");
	do {
		printf("Select an operation to perform on linked list: ");
		scanf("%d", &index);
		switch(index) {
			case 1: printf("Enter position at which node is to be entered: ");
					scanf("%d", &pos);
					printf("Enter element to be inserted: ");
					scanf("%d", &ele);
					insertAtPosition(&l1, pos, ele);
					traverse(l1);
					break;
			case 2: printf("Enter position at which node is to be deleted: ");
					scanf("%d", &pos);
					deleteAtPosition(&l1, pos);
					traverse(l1);
					break;
			case 3: printf("Enter element to be searched in linked list: ");
					scanf("%d", &ele);
					search(l1, ele);
					break;
			case 4: printf("Length of list: %d\n", length(l1));
					break;
			case 5: exit(0);
					break;
			default: printf("Invalid Choice entered");
		}
	} while(index);
	return 0;
}

void init(list *l) {
	*l = NULL;
	return;
}

void append(list *l, int data) {
	node *newnode, *q;
	newnode = (node *)malloc(sizeof(node));
	if(newnode) {
		newnode -> data = data;
		newnode -> next = NULL;
	}
	else
		return;
	if(*l == NULL) {
		*l = newnode;
		return;
	}
	q = *l;
	while(q -> next)
		q = q -> next;
		q -> next = newnode;
	return;
}

void traverse(list l) {
	node *p = l;
	if(p == NULL) {
		printf("List is empty\n");
		return;
	}
	printf("Linked List: ");
	while(p){
		printf("%d ", p -> data);
		p = p -> next;
	}
	printf("\n");
	return;
}

int length(list l) {
	int len = 0;
	node *p = l;
	if(p == NULL) {
		len = 0;
		return len;
	}
	while(p) {
		len = len + 1;
		p = p -> next;
	}
	return len;
}

void search(list l, int ele) {
	node *p = l;
	int i = 0;
	while(p) {
		if(p -> data == ele) {
			printf("%d is at position %d in the linked list\n", ele, i);
			return;
		}
		p = p -> next;
		i = i + 1;
	}
	if(i >= length(l)) {
		printf("Element not found in list\n");
	}
	return;
}

void insertBegin(list *l, int data) {
	node *newnode;
	newnode = (node *)malloc(sizeof(node));
	if(newnode) {
		newnode -> data = data;
		newnode -> next = NULL;
	}
	else
    	return;
    newnode -> next = *l;
    *l = newnode;
    return;
}

void insertAtPosition(list *l,int index, int data) {
	node *newnode, *q;
	int j = 0;
	newnode = (node *)malloc(sizeof(node));
	if(newnode) {
		newnode -> data = data;
		newnode -> next = NULL;
	}
	else
    	return;
	if(index == 0) {
    	insertBegin(l, data);
    	return;
    }
    if(index >= length(*l)) {
    	append(l, data);
    	return;
    }
    else {
    q = *l;
    while(j < index - 1) {
      q = q -> next;
      j = j + 1;
    }
    newnode -> next = q -> next;
    q -> next = newnode;
    return;
  }
}

void deleteBegin(list *l) {
   	node *p;
  	p = *l;
  	if(p == NULL) {
  		return;
  	}
  	*l = p->next;
  	free(p);
  	return;
}

void deleteEnd(list *l) {
  	node *p, *q;
  	p = *l;
  	q = NULL;
  	if(p == NULL) {
  		return;
  	}
  	while (p->next) {
    	q = p;
    	p = p->next;
  	}
  	q->next = NULL;
  	free(p);
  	return;
}

void deleteAtPosition(list *l, int index) {
	node *p, *q;
	p = *l;
	q = NULL;
	int j = 0;
	if(p == NULL) {
  		return;
    }
	if(index == 0) {
		deleteBegin(l);
		return;
	}
	if(index >= length(*l)) {
		deleteEnd(l);
		return;
	}
	else {
		while(j < index) {
			q = p;
			p = p -> next;
      		j = j + 1;
		}
		q -> next = p -> next;
		free(p);
		return;
	}
}