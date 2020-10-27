#include<stdio.h>
void main()
{
	int i,j,n=0,temp,pos,pr[10],bt[10],wt[10],tat[10];
	float sum_wt=0,sum_tat=0;
	printf("Enter the number of processes:\n");
	scanf("%d",&n);
	printf("Enter the burst time of each process:\n");
	for(i=0;i<n;i++)
		{
			scanf("%d",&bt[i]);
			pr[i]=i+1;
		}
		printf("Processes\t\tBurst Time\n");
	for(i=0;i<n;i++)
		{
			printf("  %d\t\t\t   %d\n",pr[i],bt[i]);
		}
	//applying selection sort
	 for(i=0;i<n;i++)
    {
        pos=i;
        for(j=i+1;j<n;j++)
        {
            if(bt[j]<bt[pos])
                pos=j;
        }
 
        temp=bt[i];
        bt[i]=bt[pos];
        bt[pos]=temp;
 
        temp=pr[i];
        pr[i]=pr[pos];
        pr[pos]=temp;
    }
    wt[0]=0;
    for(i=0;i<n;i++)
		{
			wt[i+1]=bt[i]+wt[i];
			tat[i]=bt[i]+wt[i];
			sum_wt=sum_wt+wt[i];
			sum_tat=sum_tat+tat[i];	
		}
	printf("Processes\t\tBurst Time\t\tWaiting Time\t\tTurnaround Time\n");
	for(i=0;i<n;i++)
		{
			printf("  %d\t\t\t   %d\t\t\t   %d\t\t\t   %d\n",pr[i],bt[i],wt[i],tat[i]);
		}
	printf("Average Waiting Time:%f\n",sum_wt/n);
	printf("Average Turnaround Time:%f",sum_tat/n);	
}
