#include <stdio.h>

void findWaitingTime(int processes[], int n, int bt[], int wt[])
{
    wt[0] = 0;

    for (int i = 1; i < n; i++)
        wt[i] = bt[i - 1] + wt[i - 1]; // waiting_time[current_process] = burst_time[prev_process] + waiting_time[prev_process]
}

void findTurnAroundTime(int processes[], int n, int bt[], int wt[], int tat[])
{
    for (int i = 0; i < n; i++)
        tat[i] = bt[i] + wt[i]; // turn_around_time[current_process] = burst_time[current_process] + waiting_time[current_process]
}

void findavgTime(int processes[], int n, int bt[])
{
    int wt[n], tat[n], total_wt = 0, total_tat = 0;

    findWaitingTime(processes, n, bt, wt); // function to find waiting time for all processes

    findTurnAroundTime(processes, n, bt, wt, tat); // function to find turnaround time for all processes

    printf("\n\nProcesses\tBurst time\tWaiting time\tTurn around time\n");

    for (int i = 0; i < n; i++)
    {
        total_wt = total_wt + wt[i];
        total_tat = total_tat + tat[i];
        printf(" %d ", (i + 1));
        printf("\t\t%d ", bt[i]);
        printf("\t\t%d", wt[i]);
        printf("\t\t%d\n", tat[i]);
    }
    int s = (float)total_wt / (float)n;
    int t = (float)total_tat / (float)n;
    printf("Average waiting time = %d", s);
    printf("\n");
    printf("Average turn around time = %d ", t);
}

int main()
{
    int processes[] = {1, 2, 3}; // process ids
    int n = sizeof processes / sizeof processes[0];

    int burst_time[] = {10, 5, 8}; // burst time of all process ids

    findavgTime(processes, n, burst_time);
    return 0;
}
