#include<stdio.h>
#include<stdlib.h>

void inputValueWeight(int **arr, int num){
    int i, j;

    for(i = 0; i < num; i++){
        printf("\nEnter Value[%d] : ", i+1);
        scanf("%d", &arr[i][0]);

        printf("\nEnter Weight[%d] : ", i+1);
        scanf("%d", &arr[i][1]);
    }
}

void swap(float *a, float *b){
    *a += *b;
    *b = *a - *b;
    *a -= *b; 
}

void selectionSort(int **arr, int num, float *ratio){
    int i, j;

    for(i = 0; i < num-1; i++){
        for(j = i + 1; j < num; j++){
            if(ratio[i] < ratio[j]){
                swap(&ratio[i], &ratio[j]);
                swap(&arr[i][0], &arr[j][0]);
                swap(&arr[i][1], &arr[j][1]);
            }
        }
    }
}

void ratioOperation(int **arr, int num, float *ratio){
    int i;

    for(i = 0; i < num; i++){
        ratio[i] = arr[i][0] / arr[i][1];
    }

    selectionSort(arr, num, ratio);
}

float *knapsack(int **arr, int num, int size){
    int i, weight = 0;
    float *ratio = (float *)malloc(num * sizeof(float));
    float *taken = (float *)malloc(num * sizeof(float));

    for(i = 0; i < num; i++){
        taken[i] = 0;
    }

    ratioOperation(arr, num, ratio);

    for(i = 0; i < num; i++){
        if(weight + arr[i][1] <= size){
            taken[i] = 1;
            weight += arr[i][1];
        }else{
            taken[i] = (float)((size - weight) / (float)arr[i][1]);
            weight = size;
            break;
        }
    }

    free(ratio);

    return taken;
}

float calcValue(float *result, int num, int **arr){
    float profit = 0;
    int i;

    for(i = 0; i < num; i++){
        if(result[i] > 0){
            profit += (result[i] * arr[i][0]);
        }
    }

    return profit;
}

void main(){
    int size, num, i;

    printf("\nEnter Size of Knapsack : ");
    scanf("%d", &size);

    printf("\nEnter Number of Items : ");
    scanf("%d", &num);

    int **arr = (int **) malloc(num * sizeof(int *));
    for(i = 0; i < num; i++){
        arr[i] = (int *)malloc(2 * sizeof(int));
    }

    inputValueWeight(arr, num);

    float *result = knapsack(arr, num, size);

    printf("\nProfit will be %f\n", calcValue(result, num, arr));

    free(arr);
}