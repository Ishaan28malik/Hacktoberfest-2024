/c program to represent each polynomial in single array
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
//Definition of structure for storing polynomial Data
struct term
{
char ch[3];
int terms[3];
int arr[2][10];
}p;
	
FILE*ptr=NULL;
char ch;
int i=0,j=0,t=1;
void create()
{
//	for(i=0;i<3;i++)
//	{
//		fscanf(ptr,"%c",&p.ch[i]);
//		fscanf(ptr,"%d",&p.terms[i]);
//		for(j=0;j<p.terms[i];j++)
//		{
//			fscanf(ptr,"%d",&p.arr[0][j+t]);
//			fscanf(ptr,"%d",&p.arr[1][j+t]);
//			t=j+1;	
//		}	
//	}
//	
		if(ch=='\n'){
            t++;
        }
        if(t%4==1){
            p.ch[i]=ch; // for scaning polynomial's ch
        }
        else if(t%4==2){
            fscanf(ptr,"%d",&p.terms[i]); // for scanning no. of non-zero terms
            i++;
        }
        else if(t%4==3){  // for scanning coefficient and then the exponent
            fscanf(ptr,"%d",&p.arr[0][j]);
            fscanf(ptr,"%d",&p.arr[1][j]);
            j++;

}
};

void output()
{
	for(i=0;i<3;i++)
	{
	    printf("Polynomial = %c\n",p.ch[i]);
		printf("No. of terms- %d\n",p.terms[i]);
		for(j=0;j<p.terms[i];j++)
		{
			printf("%d ",p.arr[0][j+t]);
			printf("%d ",p.arr[1][j+t]);
			t=j+1;	
		}
		printf("\n");
	}
};

  
main()
{
ptr=fopen("DataFileAssign2.txt", "r");//creating buffer
create();
output();
fclose(ptr);	
}
