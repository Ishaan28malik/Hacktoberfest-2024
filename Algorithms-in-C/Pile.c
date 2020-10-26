/*
 Estructuras de datos abstractas
 Fila
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int *data;
	unsigned int Id_Front; // Frente de la Fila
	unsigned int Id_End; // Ultimo dato de la Fila
	unsigned int Size; // Tamano de la Fila
	unsigned int NumElemEnFila; // Numero de elementos en la Fila
}FILA;

FILA* CrearFila(unsigned int Tam);
char Enqueue(FILA *p, int *dato);
char Dequeue(FILA *p, int *dato); // Sacar elemento del frente
char FrontofQueue(FILA *p, int *dato); // Muestra el dato del frente
char IsEmpty(FILA *p); // Fila vacia.
char IsFull(FILA *p); 
void FreeFila(FILA *p); 
unsigned int SizeofQueue(FILA *p); // Numero de elementos en la fila
void MostrarFila(FILA *p); 

int main ()
{
	FILA  *fila1;
	int d, bandera = 1, op, nD;
	printf("Tamanio de la Fila:\n");
	scanf("%i", &nD);
	fila1 = CrearFila(nD);
	while(bandera != 0){
		printf("Seleccione una opcion\n");
		printf("1.- Enqueue\n");
		printf("2.- Dequeue\n");
		printf("3.- Front of queue\n");
		printf("4.- Size of queue\n");
		printf("5.- Mostrar fila\n");
		printf("6.- Exit\n");
		scanf("%i", &op);
		switch (op){
			case 1:
				printf("Dato a ingresar en la Fila:\n");
				scanf("%i", &d);
				if(!Enqueue(fila1, &d))
					printf("Fila llena, %i no se ingreso el en la Fila.\n", d);
				break;
			case 2:
				if(!Dequeue(fila1, &d))
					printf("Fila vacia, no se obtuvo el dato.\n");
				break;
			case 3:
				if(!FrontofQueue(fila1, &d))
					printf("Fila vacia..\n");
				else
					printf("El dato del frente es %i\n", d);
				break;
			case 4:
				printf("Numero de elementos en la Fila: %i\n", SizeofQueue(fila1));
				break;
			case 5:
				MostrarFila(fila1);
				break;
			default:
				break;
		}
		printf("Realizar otra accion? SI[ 1 ] NO [ 0 ]\n");
		scanf("%i", &bandera);
		system("cls");
	}
	FreeFila(fila1);
	printf("\n");
	return 0;
}

unsigned int SizeofQueue(FILA *p){
	return p->NumElemEnFila;
}

char FrontofQueue(FILA *p, int *dato){
	if(!IsEmpty(p)){
		*dato = *(p->data+p->Id_Front);
		return 1;
	}else
		return 0;
}

void MostrarFila(FILA *p){
	int i, id; 
	i=(int) (p->Id_End-1);
	for(id=0; id<p->NumElemEnFila; id++){
            if(i==-1)
                i=p->Size-1;
            printf("%d ",*(p->data + i));
            i--;
	}
	printf("\n");
}

void FreeFila(FILA *p){
	free(p->data);
	free(p);
}

char IsFull(FILA *p){
	if(p->NumElemEnFila == p->Size)
		return 1;
	else
		return 0;
}

char IsEmpty(FILA *p){
	if(p->NumElemEnFila == 0)
		return 1;
	else
		return 0;
}

char Enqueue(FILA *p, int *dato){
	if(!IsFull(p)){
		if(p->Id_End==p->Size)
			p->Id_End = 0;
		*(p->data + p->Id_End) = *dato;
		p->Id_End++;
		p->NumElemEnFila++;
		return 1;
	}
	else{
		return 0;
	}
}
char Dequeue(FILA *p, int *dato){
	if(!IsEmpty(p)){
		*dato = *(p->data + p->Id_Front);
		p->Id_Front++;
		p->NumElemEnFila--;
		if(p->Id_Front==p->Size)
                  p->Id_Front=0;
		return 1;
	}else
		return 0;
}

FILA* CrearFila(unsigned int Tam){
	FILA *ptr;
	ptr = (FILA *) malloc(sizeof(FILA));
	if(ptr == NULL){
		printf("\nError al reservar memoria para la Fila...");
		exit(0);
	}
	ptr->Id_Front = 0; 
	ptr->Id_End = 0;
	ptr->Size = Tam;
	ptr->NumElemEnFila = 0;
	ptr->data = (int *) malloc (sizeof(int)*Tam);
	if( ptr->data == NULL){
		printf("\nError al reservar memoria para datos de la Fila...");
		exit(0);
	}
	return ptr;
}

