# include <stdio.h> 
  
/* Function to print reverse of the passed string */
void reverse(char *str) 
{ 
   if (*str) 
   { 
       reverse(str+1); 
       printf("%c", *str); 
   } 
} 
  
/* Driver program to test above function */
int main() 
{ 
   char a[50]; 
   printf("Enter a string : ");
   scanf("%s",&a);
   reverse(a); 
   printf("\n");
   return 0; 
} 
