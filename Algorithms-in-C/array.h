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

#pragma once

#ifdef __cplusplus
extern "C"
{
#endif

#define ARRAY_ERASED -1
#define SUCCESS 0
#define INVALID_POSITION 1
#define POSITION_INIT 2
#define POSITION_NOT_INIT 3
#define POSITION_EMPTY 4
#define ARRAY_FULL 5

    typedef struct CArray
    {
        int *array;
        int size;
    } CArray;

    // +-------------------------------------+
    // |           Returns array             |
    // +-------------------------------------+
    CArray *getCArray(int size);
    CArray *getCopyCArray(CArray *array);

    // +-------------------------------------+
    // |           Input / Output            |
    // +-------------------------------------+
    int insertValueCArray(CArray *array, int position, int value);
    int removeValueCArray(CArray *array, int position);
    int pushValueCArray(CArray *array, int value);
    int updateValueCArray(CArray *array, int position, int value);

    // +-------------------------------------+
    // |               Erase                 |
    // +-------------------------------------+
    int eraseCArray(CArray *array);

    // +-------------------------------------+
    // |             Switching               |
    // +-------------------------------------+
    int switchValuesCArray(CArray *array, int position1, int position2);
    int reverseCArray(CArray *array);

    // +-------------------------------------+
    // |              Sorting                |
    // +-------------------------------------+
    int bubbleSortCArray(CArray *array);
    int selectionSortCArray(CArray *array);
    int insertionSortCArray(CArray *array);
    int blenderCArray(CArray *array);

    // +-------------------------------------+
    // |             Searching               |
    // +-------------------------------------+
    int valueOcurranceCArray(CArray *array, int value);
    CArray *valuePositionsCArray(CArray *array, int value);
    int findMaxCArray(CArray *array);
    int findMinCArray(CArray *array);

    // +-------------------------------------+
    // |              Display                |
    // +-------------------------------------+
    int displayCArray(CArray *array);

#ifdef __cplusplus
}
#endif
