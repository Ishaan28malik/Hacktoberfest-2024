/*
 You have an unsorted array arr of positive integers and a number s. Find a longest contiguous subarray in arr that has a sum equal to s. Return two integers that represent its inclusive bounds. If there are several possible answers, return the one with the smallest left bound. If there are no answers, return [-1].Your answer should be 1-based, meaning that the first position of the array is 1 instead of 0.
Example
    For s = 12 and arr = [1, 2, 3, 7, 5], the output should be
    findLongestSubarrayBySum(s, arr) = [2, 4].
    The sum of elements from the 2nd position to the 4th position (1-based) is equal to 12: 2 + 3 + 7.
    
    For s = 15 and arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], the output should be
    findLongestSubarrayBySum(s, arr) = [1, 5].
    The sum of elements from the 1st position to the 5th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5.
    
    For s = 15 and arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10], the output should be
    findLongestSubarrayBySum(s, arr) = [1, 8].
    The sum of elements from the 1st position to the 8th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5 + 0 + 0 + 0.
*/

#include<iostream>
using namespace std;

int res[2]={-1,-1};

int* longestSumArray(int arr[], int n, int s)
{
    for(int i=0;i<n-1;i++)
    {
        int sum=arr[i];
        for(int j=i+1;j<n;j++)
        {
            sum=sum+arr[j];
            if(sum<=s)
            {
                if(sum==s)
                {
                    if(j-i>=res[1]-res[0])
                    {
                        res[0]=i;
                        res[1]=j;
                    }
                }
            }
            else
                break;
        }
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,s,*res;
    cin>>n;
    int arr[n];
    cin>>s;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    res=longestSumArray(arr, n, s);
    if(*res!=-1)
        cout<<*res+1<<" "<<*(res+1)+1;
    else
        cout<<"Not found !";
}

