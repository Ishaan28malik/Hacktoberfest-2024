/*
Program to reverse each word in a string without any library functions
Author - Muzammil | DarthMuzammil @Github
*/
#include<stdio.h>
//Function to swap two characters
char* swap(char* str, char* str2){
    *str = *str + *str2;
    *str2 = *str - *str2;
    *str = *str - *str2;
    return(NULL);
}

//Function to reverse a string from start position to end position
char* reverse(char* str, int start, int end){
    while(start < end){
        swap(&str[start],&str[end]);
        start++;
        end--;
    }
    return(NULL);
}

//Function that takes string as input and reverses each word
char* parse(char* str){
    int start, end;
    int i = 0; 
    int j =0;
    for( i = 0; ; i++){
        if(str[i] == ' '){    //stop when whitespace is encountered 
            reverse(str, j, (i - 1));
            j = i + 1;
        }
        if(str[i] == '\0'){
            reverse(str, j, (i - 1));
            break;
        }
    }
    return(NULL);
}
int main(){
    char sentence[100];
    gets(sentence);
    parse(sentence);
    printf("\n\n%s\n\n",sentence);
    return 0;
}