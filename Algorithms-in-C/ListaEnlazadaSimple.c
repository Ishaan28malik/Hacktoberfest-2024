#include <stdio.h>
#include <stdlib.h>

typedef struct{
	int dato;
	struct NODO *next;
}NODO;

NODO* CrearNodo(int Dato);
void InsertarNodo(NODO** list, int dato);
void ImprimirLista(NODO *list);
void EliminarNodo(NODO **list);
void InsertarNodoINICIO(NODO** list, int dato);
void EliminarNodoINICIO(NODO **list);

int main()
{
	NODO *list=NULL;
    int A, N;
	
	printf("\nQue quiere hacer?:");
	printf("\nInsertar un numero al final de la fila: (1)");
	printf("\nInsertar un numero al inicio de la fila: (2)");
	printf("\nEliminar un numero al final de la fila: (3)");
	printf("\nEliminar un numero al inicio de la fila: (4)");
	printf("\nimprimir la fila: (5)");
	printf("\nsalir: (6)\n");
	
	do
    {
        printf("\nOpcion:");
        scanf("%d",&A);
        switch(A)
        {
            case 1:
                {
                    printf("\nNumero: ");
                    scanf("%d",&N);
                    InsertarNodo(&list, N);
                    break;
                }
            case 2:
                {
                    printf("\nNumero: ");
                    scanf("%d",&N);
                    InsertarNodoINICIO(&list, N);
                    break;
                }
            case 3:
                {
                    EliminarNodo(&list);
                    break;
                }
            case 4:
                {
                    EliminarNodoINICIO(&list);
                    break;
                }
            case 5:
                {
            ImprimirLista(list);
            break;
            }
        case 6:
            {
                printf("\nLa fila quedo de la siguiente manera:\n");
                ImprimirLista(list);
            }
        default:
            {
                printf("\nEsa opcion no existe. Intenta de nuevo\n");
                break;
            }
        }
    }while(A!=6);
	return 0;
}

NODO* CrearNodo(int Dato)
{
	NODO *ptr;

	ptr=(NODO *)malloc(sizeof(NODO));
	ptr->dato=Dato;
	ptr->next=NULL;

	return ptr;
}

void InsertarNodo(NODO** list, int dato)
{
	NODO *NewNodo;
	NODO *aux;

	NewNodo=CrearNodo(dato);

	//verificar su la llista esta vacia
	if(*list==NULL)
	{
		*list=NewNodo;
	}
	else
	{
		//Si la lista no esá vacia
		aux=*list;
		while(aux->next!=NULL)
			aux=aux->next;
		//Al final del ciclo while anterior, el aputador eux contiene la direccion del ultimo NODO
		aux->next=NewNodo;
	}
}

void ImprimirLista(NODO *list)
{
	NODO *aux;
	if(list==NULL)
		printf("La lista está vacía");
	else
	{
		aux=list;
		do{
			printf("%i\n", aux->dato);
			aux=aux->next;
		}while(aux!=NULL);
	}
}

void EliminarNodo(NODO **list)
{
	NODO *penultimo, *ultimo;

	if(*list==NULL)
	{
		printf("\nPIPI La lista ya esta vacia");
	}
	else
	{
		ultimo=*list;
		if(ultimo->next==NULL)
		{
			*list=NULL;
			free(ultimo);
		}
		else
		{
			while(ultimo->next!=NULL)
			{
				penultimo=ultimo;
				ultimo=ultimo->next;
			}
			penultimo->next=NULL;
			free(ultimo);
		}
	}
}


void InsertarNodoINICIO(NODO** list, int dato)
{
	NODO *NewNodo;
	NODO *aux;

	aux=*list;
	NewNodo=CrearNodo(dato);

	NewNodo->next=aux;

	*list=NewNodo;
}

void EliminarNodoINICIO(NODO **list)
{
	NODO *aux1, *aux2;

	aux1=*list;
	if(*list==NULL)
	{
		printf("\nLa fila esta vacia");
	}
	else
	{
		aux2=aux1->next;
		free(aux1);
		*list=aux2;
	}
}

