/* A manu based program to perform following operations on linear array.

1)insert an element at kth position
2)delete an element at kth position
3)traverse an array element.  */

#include<stdio.h>
#include<stdlib.h>

int position,val,n,i;
int a[100];

void insert();
void delete();
void traverse();


int main()
{
    printf("Enter size of array: ");
    scanf("%d",&n);
 
    printf("Enter the array elements:\n");
    for(i=0;i<n;i++)
    {
        scanf("%d", &a[i]);
    }

   
    
    int choice;  

    do{
        printf("\n----Choose the desired operation----\n");
        printf("1.insert element\n");
        printf("2.delete element\n");
        printf("3.traverse through array\n");
         printf("4.To exit\n");
        printf("\n Enter your choice:\n");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
            insert();
            break;

            case 2:
            delete();
            break;

            
            case 3:
            traverse();
            break;

            case 4:
            exit(0);
            break;
                        
            default:
            printf("\nInvalid choice:\n");
            break;

        }
        
    }while(choice!=3);

return 0;
}
    void insert()   //inserting an element in to an array 
    {         
        printf("\nEnter the position for the new element:\t");         
        scanf("%d",&position);         
        printf("\nEnter the element to be inserted :\t");         
        scanf("%d",&val);         
        for(i=n-1;i>=position;i--)
            {
                a[i+1]=a[i];
            }
            a[position]=val;
            n=n+1;


        printf("The new array is:\t");  
        for(i=0;i<n;++i){
            printf("%d",a[i]);
        } 
         
    }//end of insert()  

    void delete()      //deleting an array element
    {
        printf("\nEnter the position of the element to be deleted:\t");
        scanf("%d",&position);
        val=a[position];
        for(i=position;i<n-1;i++)
            {
                a[i]=a[i+1];
            }
        n=n-1;
        printf("\nThe deleted element is =%d",val);
        printf("And the array is\n");
        for(i=0;i<n;++i){
            printf("%d",a[i]);
        }
    } //end of delete   


    void traverse()   //traversing through an array
    {
        printf("the array elements are:\n");
        for(i=0;i<n;++i){
            printf("%d",a[i]);
        }
    }// end of traverse

  
