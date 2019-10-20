#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"list.h"

void init(list *l1){
	l1->tail = NULL;
	l1->head = NULL;
	l1->count = 0;
}

void insert(list *l1,int pos,int d){
	int i = 0;
	if(l1->count == 0){
		node *temp = (node *)malloc(sizeof(node));
		if(!temp) return;
		l1->count++;
		l1->head = temp;
		l1->tail = temp;
		temp->back = NULL;
		for(i = 0 ; i < pos ; i++){
			node *temp = (node *)malloc(sizeof(node));
			if(!temp) return;
			l1->tail->front = temp;
			temp->back = l1->tail;
			l1->tail = temp;
			l1->count++;
		}
		l1->tail->data = d;	
	}
	else if(pos < l1->count ){
		node *ptr = l1->head;
		for(i = 0 ; i < pos;i++){
			ptr = ptr->front;
		}
		ptr->data = d;
	}
	else if(pos == l1->count - 1){
		l1->tail->data = d;
	}
	else if(pos > l1->count - 1){
		int f = pos - l1->count + 1;
		for(i = 0 ; i  < f; i++){
			node *temp = (node *)malloc(sizeof(node));
			if(!temp) return;
			l1->tail->front = temp;
			temp->back = l1->tail;
			l1->tail = temp;
			l1->count++;
		
		}
		l1->tail->data = d;
	}

}


void traverse(list *l1){
	int i;
	node *ptr = l1->head;
	for(i = 0 ; i  < l1->count;i++){
		printf("%d ",ptr->data);
		ptr = ptr->front;
	}

}


void sort(list *l1){
	int i,j;
	int temp;
	node *ptr = l1->head;
	node *ptr1 = NULL;
	for(i = 0 ; i < l1->count;i++ ){
		ptr1 = ptr->front;
		for(j = i+1 ; j < l1->count ;j++){
			if(ptr1->data > ptr->data){
				temp = ptr->data;
				ptr->data = ptr1->data;
				ptr1->data = temp;	
			}
		ptr1 = ptr1->front;
		}
	ptr = ptr->front;
	}


}

void rev(list *l1){
	node *ptr = l1->tail;
	int i = 0;
	int arr[l1->count + 1];
	for(i = 0 ; i < l1->count; i++){
		arr[i] = ptr->data;
		ptr = ptr->back;
	}
	ptr = l1->head;
	for(i = 0 ; i < l1->count ;i++){
		ptr->data = arr[i];
		ptr = ptr->front;
	}



}

void concat(list *l1,list *l2){
	node *ptr = l1->tail;
	node *ptr1 = l2->head;
	ptr->front = ptr1;
	ptr1->back = ptr;
	for(int i = 0 ; i < l2->count ;i++){
		l1->tail = l1->tail->front;
	}
	l1->count = l1->count + l2->count;

}

void remdup(list *l1){
	node *ptr = l1->head;
	int i;
	node *pt2 = NULL;
	node *del;
	for(i = 0 ; i < l1->count ;i++){
		pt2 = ptr->front;
		for(int j = i+1 ; j <l1->count ;j++){
			if(pt2->data == ptr->data){
				del = pt2;
				pt2->back->front = pt2->front;
				free(del);
				pt2 = pt2->front;
				l1->count--;
			}
			else
				pt2 = pt2->front;
		}
		ptr = ptr->front;
	}

}


int main(){
	list l1;
	init(&l1);
	for(int i = 0; i < 5 ; i++){
		insert(&l1,i,3);
	}
	insert(&l1,5,2);
	insert(&l1,6,7);
	list l2;
	init(&l2);
	int k = 0;
	for(int i = 5 ;i < 10 ;i++,k++){
		insert(&l2,k,i);
	}
	//sort(&l1);
	//rev(&l1);
	//concat(&l1,&l2);
	remdup(&l1);
	traverse(&l1);


	return 0;
}
