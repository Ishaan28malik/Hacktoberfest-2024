/*
 * CArray.c
 *
 * Author: Luis Aneuris Tavarez De Jesus
 * Created on 10/08/2021
 *
 *
 * Array Implementations in C
 * Coleccion implemetada en C
 *
 * Compiled in Visual Studio Code
 *
 */

/*
Return Codes

-1 - Array Erased - -1 
0 - Success  - Correcto
1 - Invalid Position - 1- Posicion Invalida
2 - Position already initialized (use update function) - 2-POsition lista para inicializar
3 - Position not initialized (use insert function) - 3-Positio
4 - Position already empty
5 - Array is full

*/

//IMPORT OF PACKAGE OF C
//IMPORTACION DE PAQUETE DE C
#include "carray.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>




void swap(CArray *array, int position1, int position2);


//Function To Create Array
//Funcion para Crear Coleccion
CArray *getCArray(int size)
{
    CArray *array = (CArray *)malloc(sizeof(CArray));
    array->array = (int *)malloc(sizeof(int) * size);
    array->size = size;
    int i;
    for (i = 0; i < size; i++)
    {
        array->array[i] = 0;
    }
    return array;
}


//Function To Insert Element In ARRAY
//Funcion PARA INSERTAR ELEMENTO EN LA Coleccion
int insertValueCArray(CArray *array, int position, int value)
{
    if (position >= 0 && position < array->size)
    {
        if (array->array[position] == 0)
        {
            array->array[position] = value;
            return SUCCESS;
        }
        else
            return POSITION_INIT;
    }
    return INVALID_POSITION;
}
//Function To REMOVE Element In ARRAY
//Funcion PARA REMOVER ELEMENTO EN LA Coleccion

int removeValueCArray(CArray *array, int position)
{
    if (position >= 0 && position < array->size)
    {
        if (array->array[position] != 0)
        {
            array->array[position] = 0;
        }
        else
            return POSITION_EMPTY;
    }
    return INVALID_POSITION;
}
//Function To Push more Element In ARRAY
//Funcion PARA COLOCAR MAS ELEMENTO EN LA Coleccion
int pushValueCArray(CArray *array, int value)
{
    int i;
    int ok = 0;
    for (i = 0; i < array->size; i++)
    {
        if (array->array[i] == 0)
        {
            array->array[i] = value;
            ok = 1;
            break;
        }
    }
    if (ok == 1)
        return SUCCESS;
    else
        return ARRAY_FULL;
}

//Function To Update  Element In ARRAY
//Funcion PARA Actualizar  ELEMENTO EN LA Coleccion
int updateValueCArray(CArray *array, int position, int value)
{
    if (position >= 0 && position < array->size)
    {
        if (array->array[position] != 0)
        {
        }

        else
            return POSITION_NOT_INIT;
    }
    return INVALID_POSITION;
}

//Function To Update  Element In ARRAY
//Funcion PARA Actualizar  ELEMENTO ENLA Coleccion
int eraseCArray(CArray *array)
{
    int i;
    for (i = 0; i < array->size; i++)
    {
        array->array[i] = 0;
    }
    return 0;
}
//Function To Switch  Element In ARRAY
//Funcion PARA Cambiar  ELEMENTO EN LA Coleccion

int switchValuesCArray(CArray *array, int position1, int position2)
{
    if (position1 >= 0 && position1 < array->size && position2 >= 0 &&
        position2 < array->size)
    {
        int temp = array->array[position1];
        array->array[position1] = array->array[position2];
        array->array[position2] = temp;
    }
    return INVALID_POSITION;
}

//Function To REVERSE  ARRAY
//Funcion PARA Intercambiar  ELEMENTO EN LA Coleccion

int reverseCArray(CArray *array)
{
    int i;
    for (i = 0; i < array->size / 2; i++)
    {
        swap(array, i, array->size - i - 1);
    }
    return SUCCESS;
}

//Function To SHOW ELEMENTS IN THE  ARRAY
//Funcion PARA MOSTRAR  ELEMENTO EN LA Coleccion
int displayCArray(CArray *array)
{
    int i;
    printf("\nC ARRAY\n");
    for (i = 0; i < array->size; i++)
    {
        printf("%d ", array->array[i]);
    }
    printf("\n");
    return 0;
}

//Function To BLENDER  ARRAY
//Funcion  PARA GENERAR UN ALEATORIO DE ORDEN  EN LA Coleccion
int blenderCArray(CArray *array)
{
    srand(time(NULL) * array->size);
    int i;
    int total = array->size * 100;
    for (i = 0; i < total; i++)
    {
        swap(array, rand() % array->size, rand() % array->size);
    }
    return 0;
}

//Function To BLENDER  ARRAY
//Funcion  PARA GENERAR UN ALEATORIO DE ORDEN  EN LA Coleccion
CArray *getCopyCArray(CArray *arr)
{
    CArray *array = (CArray *)malloc(sizeof(CArray));
    array->array = (int *)malloc(sizeof(int) * arr->size);
    array->size = arr->size;
    int i;
    for (i = 0; i < arr->size; i++)
    {
        array->array[i] = arr->array[i];
    }
    return array;
}


//Function To swap element  in the ARRAY
//Funcion  intercambiar elemento  EN LA Coleccion
void swap(CArray *array, int position1, int position2)
{
    int temp = array->array[position1];
    array->array[position1] = array->array[position2];
    array->array[position2] = temp;
}



// STRUCTURE OF DATA ARRAY

/*Bubble Sort is the simplest sorting algorithm that 
works by repeatedly swapping the adjacent elements if they are in wrong order.
/*
SPANISH

La ordenación por burbujas es el algoritmo de ordenación más simple que funciona 
intercambiando repetidamente los elementos adyacentes si están en un orden incorrecto.
*/

int bubbleSortCArray(CArray *array)
{
    int i, j;
    for (i = 0; i < array->size - 1; i++)
    {
        for (j = 0; j < array->size - i - 1; j++)
        {
            if (array->array[j] > array->array[j + 1])
            {
                swap(array, j, j + 1);
            }
        }
    }
    return 0;
}


/*
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted. 
2) Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 
Following example explains the above steps: 

SPANISH
El algoritmo de ordenación por selección ordena un array encontrando repetidamente el elemento mínimo (considerando el orden ascendente) de la parte no ordenada y poniéndolo al principio. El algoritmo mantiene dos submatrices en un array dado.
1) La submatriz que ya está ordenada. 
2) La submatriz restante que no está ordenada.
En cada iteración de la ordenación por selección, se escoge el elemento mínimo (considerando el orden ascendente) de la submatriz sin ordenar y se traslada a la submatriz ordenada. 
El siguiente ejemplo explica los pasos anteriores: 

*/
int selectionSortCArray(CArray *array)
{
    int i, j, min;
    for (i = 0; i < array->size - 1; i++)
    {
        min = i;
        for (j = i + 1; j < array->size; j++)
            if (array->array[j] < array->array[min])
                min = j;
        swap(array, min, i);
    }
    return 0;
}
/*
Function to INSERT Element in the Array

SPANISH
Function to Insertar elemento en el Array
*/


int insertionSortCArray(CArray *array)
{
    int i, j, num;
    for (i = 1; i < array->size; i++)
    {
        num = array->array[i];
        j = i - 1;
        while (j >= 0 && array->array[j] > num)
        {
            array->array[j + 1] = array->array[j];
            j--;
        }
        array->array[j + 1] = num;
    }
    return 0;
}

/*
Search element with more Currance in the ARRAY

SPANISH
Buscar el elemento mas repetido dentro de la Colecion
*/
int valueOcurranceCArray(CArray *array, int value)
{
    int i, total = 0;
    for (i = 0; i < array->size; i++)
    {
        if (array->array[i] == value)
            total++;
    }
    return total;
}
/*
Function to Value of element  in The Array

SPANISH
Funcion para obt el elemento Menor en la colecion

*/
CArray *valuePositionsCArray(CArray *array, int value)
{
    int i, j = 0;
    int total = valueOcurranceCArray(array, value);
    CArray *resultArray = getCArray(total);
    for (i = 0; i < array->size; i++)
    {
        if (array->array[i] == value)
        {
            resultArray->array[j] = i;
            j++;
        }
    }
    return resultArray;
}

/*
Function to Search element MIN in The Array

SPANISH
Funcion para buscar el elemento Menor en la colecion

*/
int findMinCArray(CArray *array)
{
    int i;
    int min = array->array[0];
    for (i = 1; i < array->size; i++)
    {
        if (array->array[i] < min)
        {
            min = array->array[i];
        }
    }
    return min;
}

/*
Function to Search element MAX in The Array

SPANISH
Funcion para buscar el elemento mayor en la colecion

*/
int findMaxCArray(CArray *array)
{
    int i;
    int max = array->array[0];
    for (i = 1; i < array->size; i++)
    {
        if (array->array[i] > max)
        {
            max = array->array[i];
        }
    }
    return max;
}


//main to execute anything Function
int main(){
    int result;
    CArray *array = getCArray(5);
    


    // int i;
    // for (i = 0; i < array->size; i++)
    // {
    //     insertValueCArray(array, i, i + 1);
    // }
    
    // result = valueOcurranceCArray(array,3);
    array = valuePositionsCArray(array,1);
    displayCArray(array);

    printf("RESULT : %d  \n",result);
    
    return 0;
}
