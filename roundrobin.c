#include<stdio.h>

void swap(int a[], int j,int k){

    int temp;
    temp=a[j];
    a[j]=a[k];
    a[k]=temp;
}

void main(){
int p[10],b[10],a[10],i,j,c,n,gantt[10][20],ready[10][20],q,flag=1,sum=0,wt[20],tt[20],count=0,s,m;
printf("enter number of processes :");
scanf("%d",&n);
printf("enter time quantum :");
scanf("%d",&q);
for(i=0;i<n;i++)
{
    printf("enter process number :");
    scanf("%d",&p[i]);
    printf("enter arrival time for p%d :",p[i]);
    scanf("%d",&a[i]);
    printf("enter burst time for p%d :",p[i]);
    scanf("%d",&b[i]);
    printf("\n");
}
for(i=0;i<n;i++)
{
    sum=sum+b[i];
}
for(i=0;i<n;i++)
{
    for(j=0;j<n-i-1;j++)
    {
        if(a[j]>a[j+1])
        {
            swap(a,j,j+1);
            swap(b,j,j+1);
            swap(p,j,j+1);
        }
    }
}


int t=0,k=0;          //p[]  //gantt[]
gantt[0][k]=p[t];
c=0;              //r[]
for(j=1;j<n;j++)
{
    if(a[j]<=b[t])
    {
        ready[0][c]=p[j];
        ready[1][c]=b[j];
        c++;
        }
    }



if(b[0]>=q)
{
    gantt[1][k]=q;
    if(b[0]>q){
    ready[0][c]=p[0];
    ready[1][c]=b[0]-q;
    c++;
    }
}
else
{
    gantt[1][k]=b[0];
}
i=0;
while(i<20)
{

    flag=1;
    if(ready[1][i]>=q)
    {
        k++;
        gantt[0][k]=ready[0][i];
        gantt[1][k]=gantt[1][k-1]+q;

        for(j=0;j<n;j++)
        {
            if(gantt[1][k]>=a[j] && a[j]>gantt[1][k-1])
            {
                ready[0][c]=p[j];
                ready[1][c]=b[j];
                c++;
            }
        }
        if(ready[1][i]>q){
        ready[0][c]=ready[0][i];
        ready[1][c]=ready[1][i]-q;
        c++;
        }
    }
    else
    {   if(ready[1][i]<q)
        {
            if(ready[1][i]>0)
            {
                k++;
                gantt[0][k]=ready[0][i];
                gantt[1][k]=gantt[1][k-1]+ready[1][i];

                for(j=0;j<n;j++)
                {
                    if(gantt[1][k]>=a[j] && a[j]>gantt[1][k-1])
                    {
                        ready[0][c]=p[j];
                        ready[1][c]=b[j];
                        c++;
                    }
                }
            }
        }
    }
    i++;
    if(gantt[1][k]==sum)
    {
        break;
    }

}
printf("Gantt chart:-\n|");
for(i=0;i<k+1;i++){
    printf("  p%d\t|",gantt[0][i]);

}
printf("\n");
printf("0");
for(i=0;i<k+1;i++){
     printf("\t%d ",gantt[1][i]);
}

printf("\nReady queue:-\n|");
for(i=0;i<c;i++){
    printf("   p%d\t|",ready[0][i]);

}printf("\n");
for(i=0;i<c;i++){
    printf("    %d\t",ready[1][i]);

}
m=0; //tt
for(i=0;i<n;i++)
{
    count=0;
    s=0;
    for(j=0;j<k+1;j++)
    {
        if(gantt[0][j]==p[i])
        {
            count++;
        }
    }
    for(j=0;j<k+1;j++)
    {
        if(gantt[0][j]==p[i])
        {
            s++;
            if(s==count){
                tt[m]=gantt[1][j]-a[i];
                wt[m]=tt[m]-b[i];

                m++;
            }
        }
    }
}
float att=0,awt=0;
printf("\n-----------------------------------------------------------------------\nprocess id\tarrival time\tburst time\tturnaround time\t\twaiting time");
for(i=0;i<n;i++)
{
    printf("\n%d\t\t%d\t\t%d\t\t%d\t\t\t%d",p[i],a[i],b[i],tt[i],wt[i]);
    att=att+tt[i];
    awt=awt+wt[i];

}
printf("\nAverage turnaround time=%.3f",att/n);
printf("\nAverage waiting time=%.3f\n",awt/n);


}













