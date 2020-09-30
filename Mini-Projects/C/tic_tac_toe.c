#include<stdio.h>
#include <stdlib.h>
int arr[9];//declared globally to use the array in print function
void print(){
    printf("\t\tPlayer 1:\'X\'\tPlayer 2:\'O\'");
    printf("\n\n");
    printf("\t\t\t  %c | %c  | %c  \n",arr[0],arr[1],arr[2]);
    printf("\t\t\t----+----+----\n");
    printf("\t\t\t  %c | %c  | %c  \n",arr[3],arr[4],arr[5]);
    printf("\t\t\t----+----+----\n");
    printf("\t\t\t  %c | %c  | %c  \n",arr[6],arr[7],arr[8]);
}
int main(){
    int i,j,k,l,c,value,ct=0,result=0,index=0,player;
    for(i=0;i<9;i++)//initializing an array
    {
        arr[i]=' ';
    }
    printf("Enter 1 for Multi Players and 2 for Single Player  ");//ask user for mode
    scanf("%d",&c);
    if(!(c==1||c==2))//if user enter wrong mode
    {
        printf("Try Entering Correct Input");
        return 0;
    }
    for(ct=0;ct<9;){
        if((ct%2==0)||(c==1&&ct%2!=0))
        print();
        if(ct%2==0){
            player=1;
            value='X';
        }
        else{
            player=2;
            value='O';
        }
        if(c==1||((c==2)&&ct%2==0))//ask input only if it is multi mode or user turn in single mode
        {
            printf("Move for player %d (1-9)",player);
            scanf("%d",&index);
            if (index<1 || index>9) {
            printf("Allowed index is 1 to 9!!\n");
            continue;
            }
            if (arr[index - 1] == 'X'||arr[index - 1] == 'O') {
            printf("Position Already occupied!!\n");
            continue;
            }
        }
        else//generate random integer as input
        {
             for(;1;){
                    index = rand()%9+1;
                    if (!(arr[index - 1] == 'X'||arr[index - 1] == 'O'))
                    break;
                }
        }
        arr[index-1]=value;
        ct++;//increment the counter here as it allows the index after index is valid
        if(((arr[0]==value)&&(arr[1]==value)&&(arr[2]==value))||((arr[3]==value)&&(arr[4]==value)&&(arr[5]==value))||((arr[6]==value)&&(arr[7]==value)&&(arr[8]==value)))//Horizontal win
        {
           print();
           printf("Player %d is the winner. Congrats!!\n",player);
           return 0;
        }
        if(((arr[0]==value)&&(arr[3]==value)&&(arr[6]==value))||((arr[1]==value)&&(arr[4]==value)&&(arr[7]==value))||((arr[2]==value)&&(arr[5]==value)&&(arr[8]==value)))//vertical win
        {
            print();
           printf("Player %d is the winner. Congrats!!\n",player);
           return 0;
        }
        if ((arr[0] == value && arr[4] == value && arr[8] == value) ||(arr[2] == value && arr[4] == value && arr[6] == value)) //diagonally winner
        {
            print();
           printf("Player %d is the winner. Congrats!!\n",player);
           return 0;
        }
    }
    printf("Match Draw");
    return 0;
}


