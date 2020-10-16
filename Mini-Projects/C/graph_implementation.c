/**
* This is a Implementation of Undirected Graph in C using Both BFS (Breadth First Search) & DFS(Depth First Search).
*
*/


#include<stdio.h>
#include<stdlib.h>
#define SIZE 40

struct node{
 int vertex;
 struct node* next;
};

//Creating a Node
struct node* createNode(int v){
struct node* newNode = malloc( sizeof( struct node ) );
newNode->vertex = v;
newNode->next = NULL;
return newNode;
};

struct Graph{
 int numVertices;
 struct node** adjLists;
 int* visited;
};

//Creating a Graph
struct Graph* createGraph(int vertices){
 struct Graph* graph = malloc( sizeof( struct Graph ) );
 graph->numVertices = vertices;

 graph->adjLists = malloc( vertices * sizeof( struct node* ));
 graph->visited = malloc( vertices * sizeof(int) );

 for( int i = 0; i < vertices; i++){
    graph->adjLists[i] = NULL;
    graph->visited[i] = 0;
 }
 return graph;
}

// Adding a Edge in a Graph
void addEdge(struct Graph* graph, int src, int dest){
 //Adding edge from source to destination
 struct node* newNode = createNode(dest);
 newNode->next = graph->adjLists[src];
 graph->adjLists[src] = newNode;

 //Adding edge from destination to source
 newNode = createNode( src );
 newNode->next = graph->adjLists[dest];
 graph->adjLists[dest] = newNode;
}

struct queue{
 int items[SIZE];
 int front;
 int rear;
};

// Creating a Queue
struct queue* createQueue(){
 struct queue* q = malloc( sizeof( struct queue) );
 q->front = -1;
 q->rear = -1;
 return q;
};

//Adding Elements into a Queue
void enqueue( struct queue* q, int value ){
 if( q->rear == SIZE - 1 )
    printf("Queue is Full !!!");
 else{
    if( q->front == -1)
        q->front = 0;
    q->rear++;
    q->items[ q->rear ] = value;
 }
}

// Check weather a queue is empty
int isEmpty( struct queue* q ){
    if( q->rear == -1 )
        return 1;
    else
        return 0;
}

//Removing Elements From Queue
int dequeue( struct queue* q ){
 int item;
 if( isEmpty( q ) ){
    printf("Queue is Empty");
    item = -1;
 } else {
  item = q->items[q->front];
  q->front++;
  if( q->front > q->rear ){
//    printf("Resetting Queue");
    q->front = q->rear = -1;
  }
 }
 return item;
}

// Print the queue
void printQueue( struct queue* q ){
    int i = q->front;
    if( isEmpty(q) ){
        printf("Queue is Empty");
    }else{
        printf("\nQueue Front: ");
        for( i = q->front; i < q->rear ; i++){
            printf("%d", q->items[i]);
        }
    }
}

// Breadth First Search Algorithm
void BFS( struct Graph* graph, int startVertex ){
 struct queue* q = createQueue();

 graph->visited[ startVertex ] = 1;
 enqueue( q, startVertex );

 while ( !isEmpty(q) ){
//    printQueue( q );
    int currentVertex = dequeue( q );
    printf("Visited : %d \n", currentVertex);

    struct node* temp = graph->adjLists[currentVertex];

    while( temp ){
        int adjVertex = temp->vertex;

        if( graph->visited[adjVertex] == 0 ){
            graph->visited[adjVertex] = 1;
            enqueue( q, adjVertex );
        }
        temp = temp->next;
    }
 }
}

//Depth First Search Algorithm
void DFS(struct Graph* graph, int vertex){
 struct node* adjList = graph->adjLists[vertex];
 struct node* temp = adjList;

 graph->visited[vertex] = 1;
 printf("Visited %d \n", vertex);

 while( temp != NULL){
    int connectedVertex = temp->vertex;

    if( graph->visited[connectedVertex] == 0 ){
        DFS(graph , connectedVertex);
    }
    temp = temp->next;
 }
}

// It is the main calling function.
int main(){
 int vertices=0,  edges = 0, src = 0 , dest = 0;
 printf("Enter the Number of Vertices:");
 scanf("%d", &vertices );
 struct Graph* graph =  createGraph(vertices);
 printf("Enter the Number of Edges in a Graph: ");
 scanf("%d", &edges );

 for( int i = 0 ; i < edges ; i++ ){
    printf("Enter the Source and Destination of Edge %d :", i+1);
    scanf("%d%d", &src, &dest);
    addEdge( graph , src , dest);
 }

 printf("\n<!-------Using Breadth First Search-------!>\n");
 BFS( graph, 0);

 for( int i = 0; i < vertices; i++ ){
    graph->visited[i] = 0;
 }

 printf("\n<!-------Using Deapth First Search-------!>\n");
 DFS(graph, 2);

 return 0;
}
