#include <iostream> 
using namespace std; 
  
void cycleSort(int arr[], int n) 
{ 
    int writes = 0; 
  
    for (int cycle_start = 0; cycle_start <= n - 2; cycle_start++) { 
        int item = arr[cycle_start]; 
  
        int pos = cycle_start; 
        for (int i = cycle_start + 1; i < n; i++) 
            if (arr[i] < item) 
                pos++; 
  
        if (pos == cycle_start) 
            continue; 
  
        while (item == arr[pos]) 
            pos += 1; 
  
        if (pos != cycle_start) { 
            swap(item, arr[pos]); 
            writes++; 
        } 
  
        while (pos != cycle_start) { 
            pos = cycle_start; 
  
            for (int i = cycle_start + 1; i < n; i++) 
                if (arr[i] < item) 
                    pos += 1; 
  
            while (item == arr[pos]) 
                pos += 1; 
  
            if (item != arr[pos]) { 
                swap(item, arr[pos]); 
                writes++; 
            } 
        } 
    } 
  
} 
  
int main() 
{ 
    int n;
    cout << "Enter the number of value you want to sort" << endl;
    cin >> n;
    int arr[n];
    cout << "Enter the values" << endl;
    for (int i = 0; i < n; i++)
    {
        cin >> n;
    }
    
    cycleSort(arr, n); 
  
    cout << "After sort : " << endl; 
    for (int i = 0; i < n; i++) 
        cout << arr[i] << " "; 
    return 0; 
} 