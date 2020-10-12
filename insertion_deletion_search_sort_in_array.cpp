#include<stdio.h>
void main()
{
	printf("Enter no of elements to be entered into the array");
	int r,i8,i7,temp;
	scanf("%d",&r);
	int *arr =(int *)malloc(r*sizeof(int));
	int i;
	for(i=0;i<r;i++)
	{
		scanf("%d",&arr[i]);
	}
	printf("Enter 1 for insertion \n Enter 2 for searching \n Enter 3 for deleting any element of an array \n Enter 4 for sorting the array");
	int a;
	scanf("%d",&a);
	switch(a)
	
	{
		case 1:
			printf("Enter the indec and element to be inserted ");
			int i1,e1;
			scanf("%d %d",&i1,&e1);
			arr[i1]=e1;
			int i2;
			for(i2=0;i2<r;i2++)
			{
				printf("%d ",arr[i2]);
			}
	    case 2:
	    	printf("Enter element to be searched ");
	    	int i3,i4;
	    	scanf("%d",&i3);
	    	for(i4=0;i4<r;i4++)
	    	{
	    		if(*(arr+i4)==i3)
	    		{
	    			printf("Element found at index %d ",i4);
				}
			}
	    case 3:
	    	printf("Enter element to be deleted ");
	    	int e2;
	    	scanf("%d",&e2);
	    	int i41;
	    	for(i41=0;i41<r;i41++)
	    	{
	    		if(arr[i41]==e2)
	    		{
	    			int i5,i6;
	    			
	    			
	    			for(i5=i41;i5<r-1;i5++)
	    			{
	    				arr[i5]=arr[i5+1];
					}
				    
					for(i6=0;i6<r-1;i6++)
					{
							printf("%d",arr[i6]);
					}
				
				}
			}
		case 4:
			
			
			
			
			for(i7=0;i7<r;i7++)
			{
				for(i8=i7+1;i8<r;i8++)
				{
					if(arr[i7]>arr[i8])
					{
						temp=arr[i7];
						arr[i7]=arr[i8];
						arr[i8]=temp;
					}
				}
			}
			printf("Sorted array is : ");
			int i9;
			for(i9=0;i9<r;i9++)
			{
				printf("%d\n",arr[i9]);
				
			}
			
	
	}
	
}
