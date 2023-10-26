#include<bits/stdc++.h>
#include<queue>
using namespace std;

struct Process{
    int id, arrival_time, burst_time,leftb_time; 
    int completion_time;
    int wait_time;
    int ta_time;
    int push =0;
};

int main(){
    struct Process p[20], p1[20];
    int n, i, j,time_slice;
    int total_turnaround_time=0, total_wait_time=0;
    int curr_time = 0;
    
    queue<int> q;

    printf("enter the number of processes: ");
    scanf("%d", &n);
    for(i = 0; i < n; i++) {
        printf("enter the id of process: starting from zero");
        scanf("%d", &p[i].id);
        
        printf("enter the arrival time of process: ");
        scanf("%d", &p[i].arrival_time);
        printf("enter the burst time of process: ");
        scanf("%d", &p[i].burst_time);
        printf("\n");
    }
    for(int i=0;i<n;i++){
        p[i].leftb_time = p[i].burst_time;
    }
  printf("Enter the time slice:");
  scanf("%d",&time_slice);
 
  
    for (int i = 0; i < n; i++){
        p1[i] = p[i];
        p1[i].wait_time=0;
        p1[i].ta_time=0;
        
    }
    for (int i=0; i<n; i++){
        for (int j=i; j<n; j++){
            if(p1[i].arrival_time > p1[j].arrival_time){
                struct Process t = p1[i];
                p1[i] = p1[j];
                p1[j] = t;
            }
        }
    }

    q.push(p1[0].id);
    p1[0].push = 1;
   
   while(!q.empty()){
   
        int i = q.front();
       q.pop();
       for(int j =0;j<n;j++){
        if(p1[j].id == i){
           i = j;
           break;
         }
       }
    
       if(p1[i].arrival_time <= curr_time){
        if(p1[i].leftb_time > time_slice){
            p1[i].leftb_time = p1[i].leftb_time - time_slice;
            curr_time = curr_time + time_slice;
              for(int k =0;k<n;k++){
                if(p1[k].arrival_time <= curr_time && p1[k].push ==0) {
                     q.push(p1[k].id);
                     p1[k].push = 1;
                }
              }
            q.push(p1[i].id);
            
        }
        else{
            curr_time = curr_time + p1[i].leftb_time;
            for(int k =0;k<n;k++){
                if(p1[k].arrival_time <= curr_time && p1[k].push ==0) {
                     q.push(p1[k].id);
                     p1[k].push = 1;
                }
              }
            p1[i].completion_time = curr_time;
            p1[i].ta_time = p1[i].completion_time - p1[i].arrival_time;
            p1[i].wait_time = p1[i].ta_time - p1[i].burst_time;
        }
       }
       else {
        int k = p1[i].arrival_time - curr_time;
      
        if(p1[i].leftb_time > time_slice){
            p1[i].leftb_time = p1[i].leftb_time - time_slice;
            curr_time = curr_time + time_slice +k;
            for(int k =0;k<n;k++){
                if(p1[k].arrival_time <= curr_time && p1[k].push ==0) {
                     q.push(p1[k].id);
                     p1[k].push = 1;
                }
              }
            q.push(p1[i].id);
            
        }
        else{
            curr_time = curr_time + p1[i].leftb_time +k;
            for(int k =0;k<n;k++){
                if(p1[k].arrival_time <= curr_time && p1[k].push ==0) {
                     q.push(p1[k].id);
                     p1[k].push = 1;
                }
              }
            p1[i].completion_time = curr_time;
            p1[i].ta_time = p1[i].completion_time - p1[i].arrival_time;
            p1[i].wait_time = p1[i].ta_time - p1[i].burst_time;
        }
       }
    for(int m=0;m<n;m++){
        if(q.empty() && p1[m].push == 0){
            q.push(p1[m].id);
            p1[m].push = 1;
            break;
        }
   }
   }
   
   printf("Id\t AT\t BT\t CT\t TAT\t WT\n");
    for(int i=0;i<n;i++){
        printf("%d\t %d\t %d\t %d\t %d\t %d\n",p1[i].id, p1[i].arrival_time,p1[i].burst_time,p1[i].completion_time,p1[i].ta_time,p1[i].wait_time);
    }
    for (int i = 0; i < n; i++){
        total_turnaround_time += p1[i].ta_time;
        total_wait_time += p1[i].wait_time;
    }
    float avgtat = total_turnaround_time/(float)n;
    float avgwt = total_wait_time/(float)n;

    printf("Average Turn Around Time: %.2f\n", avgtat);
    printf("Average Waiting Time: %.2f\n", avgwt);
    
}