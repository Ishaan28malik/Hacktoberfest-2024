### Searching and Sorting - In Algorithms

Here we gonna learn about searching and sorting algorithms. below everything is categorized by type of algorithm. Hope you will find it useful.
### Searching

Searching Algorithms are designed to check for an element or retrieve an element from any data structure where it is used. Given below is explanation of some of the most common searching algorithms.
#### Linear Search

Linear Search sequentially checks each element of the list until a match is found or the whole list has been searched.

A simple approach is to do a linear search, i.e      
- Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
- If x matches with an element, return the index.
- If x doesn’t match with any of elements, return -1.

```cpp
int search(int arr[], int n, int x)
{
    int i;
    for (i = 0; i < n; i++)
        if (arr[i] == x)
            return i;
    return -1;
}
```

![Linear Search](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Linear_Search.png?raw=true)         

> Note-But in case we wanna make Linear Search more efficient we can also use Divide_and_Conquer and then we gonna do a linear search.     

- Time Complexity: $O(n)$
- Space Complexity: $O(1)$

[More Detail on Linear Search](https://www.geeksforgeeks.org/linear-search/)     

#### Binary Search

*Binary Search* is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).       

**Binary Search Algorithm:** The basic steps to perform Binary Search are:   

- Begin with the mid element of the whole array as search key.
- If the value of the search key is equal to the item then return index of the search key.
- Or if the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
- Otherwise, narrow it to the upper half.
- Repeatedly check from the second point until the value is found or the interval is empty.

![Binary Search](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Binary_Search.jpg?raw=true)      

**Step-by-step Binary Search Algorithm:** We basically ignore half of the elements just after one comparison.
   
1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half.
4. Else (x is smaller) recur for the left half.

There is two *Types of Binary Search* also one is Recursive and other is Iterative both of then uses some process as above but there is just a bit of diferent in code.     

- **Recursive Binary Search:** A recursive binary search function. It returns location of x in given array arr[l..r] is present, otherwise -1.     

```cpp
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x)
            return mid;
        
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);
        
        return binarySearch(arr, mid + 1, r, x);
    }
    return -1;
}
```
    Auxiliary Space : O(log n) | Time Complexity : O(log n)

- **Iterative Binary Search:** A Iterative binary search check covers all cases, so need to check for *mid = low - (high-low)/2*     

```cpp
int binarySearch(vector<int> v, int To_Find)
{
    int lo = 0, hi = v.size() - 1;
    int mid;
    while (hi - lo > 1) {
        int mid = (hi + lo) / 2;
        if (v[mid] < To_Find) {
            lo = mid + 1;
        }
        else {
            hi = mid;
        }
    }
    if (v[lo] == To_Find) {
        cout << "Found"
             << " At Index " << lo << endl;
    }
    else if (v[hi] == To_Find) {
        cout << "Found"
             << " At Index " << hi << endl;
    }
    else {
        cout << "Not Found" << endl;
    }
}
```   

- Time Complexity: $O(log n)$ 
- Auxiliary Space: $O(1)$  

[More Detail on Binary Search](https://www.geeksforgeeks.org/binary-search/)    
#### Jump Search

Let’s consider the following array: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610). The length of the array is 16. The Jump search will find the value of 55 with the following steps assuming that the block size to be jumped is 4. 
- Step 1: Jump from index 0 to index 4; 
- Step 2: Jump from index 4 to index 8; 
- Step 3: Jump from index 8 to index 12; 
- Step 4: Since the element at index 12 is greater than 55, we will jump back a step to come to index 8. 
- Step 5: Perform a linear search from index 8 to get the element 55.

![Jump Search](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Jump_Search.jpg?raw=true)

[More Detail on Jump Search](https://www.geeksforgeeks.org/jump-search/)

- **Time Complexity**
    - **Average Case:** The jump sort algorithm runs $n/m$ times where $n$ is the number of elements, and m is the block size. Linear search requires$ m-1$ comparisons making the total time expression $n/m + m-1$. The most optimal value of $m$ minimizing the time expression is $√n$, making the time complexity $n/√n + √n$, i.e. $√n$. The time complexity of the Jump Search Algorithm is $O(√n)$.
    - **Best Case:** The best-case time complexity is $O(1)$. It occurs when the element to be searched is the first element present inside the array.
    - **Worst-Case:** The worst-case occurs when we do $n/m$ jumps, and the last value we checked is greater than the element we are searching for, and $m-1$ comparisons are performed for linear search. The worst-case time complexity is $O(√n)$.
- **Space Complexity:** This algorithm’s space complexity is $O(1)$ because it doesn’t require any data structure other than temporary variables.
#### Interpolation Search

Interpolation similar to binary search but it uses better way to find mid element and *Interpolation search works better than Binary Search for a Sorted and Uniformly Distributed array.*

Interpolation constructs new data points within the range of a discrete set of known data points. Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.       

The idea of formula is to return higher value of pos when element to be searched is closer to arr[hi] and smaller value when closer to arr[lo]. 

**What is Uniformly Distributed Array?**   

*Here is simple Explanation of Uniformly Distributed Array.*     

Usually an array is considered as uniformly distributed when the difference between the elements are equal or almost same. Example 1: 1,2,3,4,5,6 (Difference is 1)     

Example 2: 10,20,31,40,55,60,73,80(Here the difference between the two adjacent elements are almost close to 10).    

Interpolation search is to be used when the given array is both sorted and uniformly distributed to have log(log n) time complexity.    

```cpp
To find the position to be searched, it uses the following formula: 
pos = lo + (x - arr[lo]) *(hi - lo)/(arr[hi] - arr[lo])

arr[] ==> Array where elements need to be searched
x     ==> Element to be searched
lo    ==> Starting index in arr[]
hi    ==> Ending index in arr[]
```      

![Interpolation Search](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Interpolation_Search_Formula.png?raw=true)        

*The formula for pos can be derived as follows.*      

```cpp
General equation of line : y = m*x + c.
y is the value in the array and x is its index.

Now putting value of lo,hi and x in the equation
arr[hi] = m*hi+c ----(1)
arr[lo] = m*lo+c ----(2)
x = m*pos + c     ----(3)

m = (arr[hi] - arr[lo] )/ (hi - lo)

subtracting eqxn (2) from (3)
x - arr[lo] = m * (pos - lo)
lo + (x - arr[lo])/m = pos
pos = lo + (x - arr[lo]) *(hi - lo)/(arr[hi] - arr[lo])
```

**Algorithm**  

*The rest of the Interpolation algorithm is the same except for the above partition logic.* 
- **Step1:** In a loop, calculate the value of “pos” using the probe position formula. 
- **Step2:** If it is a match, return the index of the item, and exit. 
- **Step3:** If the item is less than arr[pos], calculate the probe position of the left sub-array. Otherwise, calculate the same in the right sub-array. 
- **Step4:** Repeat until a match is found or the sub-array reduces to zero.       

*Below is the implementation of the algorithm.*

```cpp
// If x is present in arr[0..n-1], then returns
// index of it, else returns -1.
int interpolationSearch(int arr[], int lo, int hi, int x)
{
    int pos;
  
    // Since array is sorted, an element present
    // in array must be in range defined by corner
    if (lo <= hi && x >= arr[lo] && x <= arr[hi]) {
  
        // Probing the position with keeping
        // uniform distribution in mind.
        pos = lo
              + (((double)(hi - lo) / (arr[hi] - arr[lo]))
                 * (x - arr[lo]));
  
        // Condition of target found
        if (arr[pos] == x)
            return pos;
  
        // If x is larger, x is in right sub array
        if (arr[pos] < x)
            return interpolationSearch(arr, pos + 1, hi, x);
  
        // If x is smaller, x is in left sub array
        if (arr[pos] > x)
            return interpolationSearch(arr, lo, pos - 1, x);
    }
    return -1;
}
```    
- **Time Complexity:** 
    - **Average Case:** The algorithm’s average-case time complexity is of the order of $O(log(logn))$. It happens when all the elements inside the array are uniformly distributed.
    - **Best Case:** The best-case occurs when the element we are searching for is the first element probed by interpolation search. The best-case time complexity of the algorithm is $O(1)$.
    - **Worst-Case:** The worst-case occurs when the numerical values of the targets increase exponentially. The worst-case time complexity of the algorithm is $O(n)$.
- **Space Complexity:** This algorithm’s space complexity is $O(1)$ because it doesn’t require any data structure other than temporary variables.

[More Details On Interpolation Search](https://www.geeksforgeeks.org/interpolation-search/)
#### Exponential Search

**Exponential search involves two steps:**     
- Find range where element is present   
- Do Binary Search in above found range.   

**How to find the range where element may be present?**   

The idea is to start with subarray size 1, compare its last element with x, then try size 2, then 4 and so on until last element of a subarray is not greater.       

Once we find an index i (after repeated doubling of i), we know that the element must be present between i/2 and i (Why i/2? because we could not find a greater value in previous iteration)       

*Given below are the implementations of above steps.*

```cpp
// Returns position of first occurrence of
// x in array
int exponentialSearch(int arr[], int n, int x)
{
    // If x is present at first location itself
    if (arr[0] == x)
        return 0;
  
    // Find range for binary search by repeated doubling
    int i = 1;
    while (i < n && arr[i] <= x)
        i = i*2;
  
    //  Call binary search for the found range.
    return binarySearch(arr, i/2, 
                            min(i, n-1), x);
}
  
// A recursive binary search function. It returns
// location of x in  given array arr[l..r] is
// present, otherwise -1
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l)
    {
        int mid = l + (r - l)/2;
  
        // If the element is present at the middle itself
        if (arr[mid] == x)
            return mid;
  
        // If element is smaller than mid, then it
        // can only be present n left subarray
        if (arr[mid] > x)
            return binarySearch(arr, l, mid-1, x);
  
        // Else the element can only be present
        // in right subarray
        return binarySearch(arr, mid+1, r, x);
    }
  
    // We reach here when element is not present in array
    return -1;
}
```

- **Time Complexity :** O(Log n) 
- **Auxiliary Space :** The above implementation of Binary Search is recursive and requires O(Log n) space. With iterative Binary Search, we need only O(1) space.


**Applications of Exponential Search:**     

- Exponential Binary Search is particularly useful for unbounded searches, where size of array is infinite.
- It works better than Binary Search for bounded arrays, and also when the element to be searched is closer to the first element.

[More Details on Exponential Search on GeeksforGeeks](https://www.geeksforgeeks.org/exponential-search/)
[More Details on Exponential Search on Delftstack](https://www.delftstack.com/tutorial/algorithm/exponential-search/)
#### Ternary Search

*Ternary search* is a decrease(by constant) and conquer algorithm that can be used to find an element in an array. It is similar to binary search where we divide the array into two parts but in this algorithm, we divide the given array into three parts and determine which has the key (searched element). We can divide the array into three parts by taking mid1 and mid2 which can be calculated as shown below. Initially, l and r will be equal to 0 and n-1 respectively, where n is the length of the array.     

It is same as the binary search. The only difference is that, it reduces the time complexity a bit more. Its time complexity 
is O(log n base 3) and that of binary search is O(log n base 2).         

    mid1 = l + (r-l)/3 
    mid2 = r – (r-l)/3     

**Steps to perform Ternary Search:**     
    
    Note: Array needs to be sorted to perform ternary search on it.

**1.** First, we compare the key with the element at mid1. If found equal, we return mid1.    
**2.** If not, then we compare the key with the element at mid2. If found equal, we return mid2.    
**3.** If not, then we check whether the key is less than the element at mid1. If yes, then recur to the first part.   
**4.** If not, then we check whether the key is greater than the element at mid2. If yes, then recur to the third part.   
**5.** If not, then we recur to the second (middle) part.    

**Recursive Implementation of Ternary Search**

```cpp
int ternarySearch(int l, int r, int key, int ar[])
{
    if (r >= l) {
 
        // Find the mid1 and mid2
        int mid1 = l + (r - l) / 3;
        int mid2 = r - (r - l) / 3;
 
        // Check if key is present at any mid
        if (ar[mid1] == key) {
            return mid1;
        }
        if (ar[mid2] == key) {
            return mid2;
        }
 
        // Since key is not present at mid,
        // check in which region it is present
        // then repeat the Search operation
        // in that region
        if (key < ar[mid1]) {
 
            // The key lies in between l and mid1
            return ternarySearch(l, mid1 - 1, key, ar);
        }
        else if (key > ar[mid2]) {
 
            // The key lies in between mid2 and r
            return ternarySearch(mid2 + 1, r, key, ar);
        }
        else {
 
            // The key lies in between mid1 and mid2
            return ternarySearch(mid1 + 1, mid2 - 1, key, ar);
        }
    }
 
    // Key not found
    return -1;
}
```    

- Time Complexity:  O(log<sub>3</sub>n)     
- Auxiliary Space: O(log<sub>3</sub>n)    

**Iterative Approach of Ternary Search**    

```cpp
int ternarySearch(int l, int r, int key, int ar[])
 
{
    while (r >= l) {

        // Find the mid1 and mid2
        int mid1 = l + (r - l) / 3;
        int mid2 = r - (r - l) / 3;
 
        // Check if key is present at any mid
        if (ar[mid1] == key) {
            return mid1;
        }
        if (ar[mid2] == key) {
            return mid2;
        }
 
        // Since key is not present at mid,
        // check in which region it is present
        // then repeat the Search operation
        // in that region
 
        if (key < ar[mid1]) {
 
            // The key lies in between l and mid1
            r = mid1 - 1;
        }
        else if (key > ar[mid2]) {
 
            // The key lies in between mid2 and r
            l = mid2 + 1;
        }
        else {
 
            // The key lies in between mid1 and mid2
            l = mid1 + 1;
            r = mid2 - 1;
        }
    }
 
    // Key not found
    return -1;
}
```

- Time Complexity:  O(log<sub>3</sub>n), where n is the size of the array.     
- Auxiliary Space: O(1)    

**Binary search Vs Ternary Search:** [https://www.geeksforgeeks.org/binary-search-preferred-ternary-search/](https://www.geeksforgeeks.org/binary-search-preferred-ternary-search/)

[More Details on the Ternary Search on geeksforgeeks](https://www.geeksforgeeks.org/ternary-search/)   
[More Details on the Ternary Search on iq.opengenus](https://iq.opengenus.org/ternary-search-algorithm/)   

#### Fibonacci Search 

Its is better explained in [Delftstack](https://www.delftstack.com/tutorial/algorithm/fibonacci-search/).

### Sorting

A Sorting Algorithm is used to arranging the data of list or array into some specific order. It can be numerical or lexicographically order. Given below is explanation of some of the most common searching algorithms.   

There are two different categories in sorting. They are: 

- **Internal Sorting:** When all data is placed in memory, then sorting is called internal sorting.   
- **External Sorting:** When all data that needs to be sorted cannot be placed in memory at a time, the sorting is called External Sorting. External Sorting is used for massive amount of data. Merge Sort and its variations are typically used for external sorting. Some external storage like hard-disk, CD, etc is used for external storage.    

#### Selection Sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.       

- The subarray which is already sorted.    
- Remaining subarray which is unsorted.   

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.     

**How does selection sort work?**     

*Selection sort algorithm starts by comparing first two elements of an array and swapping if necessary, i.e., if you want to sort the elements of array in ascending order and if the first element is greater than second then, you need to swap the elements but, if the first element is smaller than second, leave the elements as it is. Then, again first element and third element are compared and swapped if necessary. This process goes on until first and last element of an array is compared. This completes the first step of selection sort.*    

Selection sort algorithm starts by comparing first two elements of an array and swapping if necessary, i.e., if you want to sort the elements of array in ascending order and if the first element is greater than second then, you need to swap the elements but, if the first element is smaller than second, leave the elements as it is. Then, again first element and third element are compared and swapped if necessary. This process goes on until first and last element of an array is compared. This completes the first step of selection sort.        

*Lets consider the following array as an example: **arr[ ] = {20, 12, 10, 15, 2}***      

![Selection Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Selection_Sort.jpg?raw=true)

**Approach:**    
- Initialize minimum value(min_idx) to location 0
- Traverse the array to find the minimum element in the array
- While traversing if any element smaller than min_idx is found then swap both the values.
- Then, increment min_idx to point to next element
- Repeat until array is sorted

```cpp
//Swap function
void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
void selectionSort(int arr[], int n)
{
    int i, j, min_idx;
 
    // One by one move boundary of
    // unsorted subarray
    for (i = 0; i < n-1; i++)
    {
       
        // Find the minimum element in
        // unsorted array
        min_idx = i;
        for (j = i+1; j < n; j++)
        if (arr[j] < arr[min_idx])
            min_idx = j;
 
        // Swap the found minimum element
        // with the first element
        swap(&arr[min_idx], &arr[i]);
    }
}
```
- **Time Complexity:**  *O(n<sup>2</sup>) as there are two nested loops(One loop to select an element of Array one by one & Another loop to compare that element with every other Array element)*.    
- **Auxiliary Space:** *O(1) as the only extra memory used is for temporary variable while swapping two values in Array.*     

[More Details on Selection Sort](https://www.geeksforgeeks.org/selection-sort/)
#### Bubble Sort

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for *large data sets as its average and worst case time complexity is quite high*.     

**How Bubble Sort Works?**      

Consider an array arr[] = **[ 6, 2, 8, 4, 10 ]**

Bubble sort starts with very first two elements, comparing them to check which one is greater swap if needed and then move to next two elements and compare them and swap if needed and so on until its done with all the elements.

![Bubble Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Bubble_Sort.png?raw=true)

Following are the implementations of Bubble Sort.    

```cpp
// A function to implement bubble sort
void bubbleSort(int arr[], int n)
{
    int i, j;
    for (i = 0; i < n - 1; i++)
 
        // Last i elements are already
        // in place
        for (j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
}
```    
   
**Optimized Implementation of Bubble Sort:**   
*The above function always runs O(n^2) time even if the array is sorted. It can be optimized by stopping the algorithm if the inner loop didn’t cause any swap.*    

Below is the implementation for the above approach:    
```cpp
// An optimized version of Bubble Sort
void bubbleSort(int arr[], int n)
{
   int i, j;
   bool swapped;
   for (i = 0; i < n-1; i++)
   {
     swapped = false;
     for (j = 0; j < n-i-1; j++)
     {
        if (arr[j] > arr[j+1])
        {
           swap(arr[j], arr[j+1]);
           swapped = true;
        }
     }
 
     // IF no two elements were swapped
     // by inner loop, then break
     if (swapped == false)
        break;
   }
}
```   

- Time Complexity: O(N<sup>2</sup>)  
- Auxiliary Space: O(1)  

**Worst Case Time Analysis:**   
- **Worst and Average Case Time Complexity:** O(N<sup>2</sup>). The worst case occurs when an array is reverse sorted.  

- **Best Case Time Complexity:** O(N). The best case occurs when an array is already sorted.  

- **Auxiliary Space:** O(1)   

[More Details on Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/)
#### Insertion Sort

*Insertion sort* is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.    

**How Insertion Sort Works?**     

*To sort an array of size N in ascending order:*    
- Iterate from arr[1] to arr[N] over the array.    
- Compare the current element (key) to its predecessor.    
- If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.   

![Insertion Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Insertion_Sort.jpg?raw=true)

Below is the implementation of Insertion Sort.    

```cpp
// Function to sort an array using insertion sort
void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
 
        // Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
```
- Time Complexity: O($N^2$) 
- Auxiliary Space: O(1)   

**More Variations of Insertion Sort:**   

- *Binary Insertion Sort(where Binary Search is used to reduce time to find the proper location to insert the selected item at each iteration)*: [https://www.geeksforgeeks.org/binary-insertion-sort/](https://www.geeksforgeeks.org/binary-insertion-sort/)     
- *Insertion Sort in Linked List:* [https://www.geeksforgeeks.org/insertion-sort-for-singly-linked-list/](https://www.geeksforgeeks.org/insertion-sort-for-singly-linked-list/)   


[More Details on Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)   
#### Merge Sort

*Merge Sort* is a *Divide and Conquer* algorithm. It divides the input array into two halves, calls itself for the two halves, and then it merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.    

**Pseudocode :**   

```cpp
•    Declare left variable to 0 and right variable to n-1 
•    Find mid by medium formula. mid = (left+right)/2
•    Call merge sort on (left,mid)
•    Call merge sort on (mid+1,rear)
•    Continue till left is less than right
•    Then call merge function to perform merge sort.
```   

![Merge Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Merge_Sort.png?raw=true)          

Below is the implementation of Merge Sort.    

```cpp
// Merges two subarrays of array[].
// First subarray is arr[begin..mid]
// Second subarray is arr[mid+1..end]
void merge(int array[], int const left, int const mid, int const right)
{
    auto const subArrayOne = mid - left + 1;
    auto const subArrayTwo = right - mid;
 
    // Create temp arrays
    auto *leftArray = new int[subArrayOne],
         *rightArray = new int[subArrayTwo];
 
    // Copy data to temp arrays leftArray[] and rightArray[]
    for (auto i = 0; i < subArrayOne; i++)
        leftArray[i] = array[left + i];
    for (auto j = 0; j < subArrayTwo; j++)
        rightArray[j] = array[mid + 1 + j];
 
    auto indexOfSubArrayOne = 0, // Initial index of first sub-array
        indexOfSubArrayTwo = 0; // Initial index of second sub-array
    int indexOfMergedArray = left; // Initial index of merged array
 
    // Merge the temp arrays back into array[left..right]
    while (indexOfSubArrayOne < subArrayOne && indexOfSubArrayTwo < subArrayTwo) {
        if (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]) {
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
        }
        else {
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
        }
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // left[], if there are any
    while (indexOfSubArrayOne < subArrayOne) {
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
        indexOfSubArrayOne++;
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // right[], if there are any
    while (indexOfSubArrayTwo < subArrayTwo) {
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
        indexOfSubArrayTwo++;
        indexOfMergedArray++;
    }
}
 
// begin is for left index and end is
// right index of the sub-array
// of arr to be sorted */
void mergeSort(int array[], int const begin, int const end)
{
    if (begin >= end)
        return; // Returns recursively
 
    auto mid = begin + (end - begin) / 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}
```    

- Time Complexity: O(n logn), in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and takes linear time to merge two halves and has a recurrence relation *T(n) = 2T(n/2) + θ(n)* can solved using Recurrence Tree method or the Master method.   
- Auxiliary Space: O(n) as in merge sort all elements are copied into an auxiliary array so N auxiliary space is required for merge sort.  

[More Details on Merge Sort](https://www.geeksforgeeks.org/merge-sort/)     
#### Heap Sort

Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the minimum element and place the minimum element at the beginning. We repeat the same process for the remaining elements.   

**Prerequisite for Heap Sort**

**1. What is Binary Heap?**    

Let us first define a Complete Binary Tree. A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.    

A Binary Heap is a Complete Binary Tree where items are stored in a special order such that the value in a parent node is greater(or smaller) than the values in its two children nodes. The former is called max heap and the latter is called min-heap. The heap can be represented by a binary tree or array.     

**2. Why array based representation for Binary Heap :** It is easy to represent in array in case of *Complete Binary Tree* and the array-based representation is space-efficient. If the parent node is stored at index $I$, the left child can be calculated by $(2 * I + 1)$ and the right child by $(2 * I + 2)$ (assuming the indexing starts at 0).       

**3. How to “heapify” a tree :** The process of reshaping a binary tree into a Heap data structure is known as ‘heapify’. A binary tree is a tree data structure that has two child nodes at max. If a node’s children nodes are ‘heapified’, then only ‘heapify’ process can be applied over that node. A heap should always be a complete binary tree.    

```cpp
// Algorithm for Heapify
heapify(array)
 Root = array[0]

   Largest = largest( array[0] , array [2 * 0 + 1]. array[2 * 0 + 2])
if(Root != Largest)
 Swap(Root, Largest)
```    

[Heapify Algorithms Brief Details](https://www.geeksforgeeks.org/building-heap-from-array/)      

**Heap Sort Algorithm for sorting in increasing order:**   
- Build a max heap from the input data. 
- At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of the tree. 
- Repeat step 2 while the size of the heap is greater than 1.  

*So, Basically we make a binary tree with the given unordered array and make it max heap and convert it back to array or given data structure*    

![Heap Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Heap_Sort.png?raw=true)   

*Below is Code Implementation*

```cpp
// To heapify a subtree rooted with node i
// which is an index in arr[]. 
// n is size of heap
void heapify(int arr[], int n, int i)
{
    
  // Initialize largest as root
    int largest = i; 
    
  // left = 2*i + 1
    int l = 2 * i + 1; 
    
  // right = 2*i + 2
    int r = 2 * i + 2; 
  
    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;
  
    // If right child is larger than largest 
    // so far
    if (r < n && arr[r] > arr[largest])
        largest = r;
  
    // If largest is not root
    if (largest != i) {
        swap(arr[i], arr[largest]);
  
        // Recursively heapify the affected 
        // sub-tree
        heapify(arr, n, largest);
    }
}
  
// Main function to do heap sort
void heapSort(int arr[], int n)
{
    
    // Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
  
    // One by one extract an element 
    // from heap
    for (int i = n - 1; i > 0; i--) {
        
        // Move current root to end
        swap(arr[0], arr[i]);
  
        // call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
}
```   

- **Time Complexity:** *O(n logn)*, 
    - *Time complexity of heapify is O(Logn).* 
    - *Time complexity of createAndBuildHeap() is O(n)* 
    - *And, hence the overall time complexity of Heap Sort is O(nLogn).*

[More Details on Heap Sort](https://www.geeksforgeeks.org/heap-sort/)
#### QuickSort

QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.   
- Always pick first element as pivot.
- Always pick last element as pivot (implemented below)
- Pick a random element as pivot.
- Pick median as pivot.

*The key process in **quickSort** is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.*     

![Quick Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Quick_Sort_Partition.png?raw=true)

**Partitioning Algorithm:** There is lots of Partition work best for this Sort. Start from the leftmost element and keep track of index of smaller (or equal to) elements as i. While traversing, if we find a smaller element, we swap current element with arr[i]. Otherwise we ignore current element.   

Below is the code implementation of Quick Sort.    

**Implementation of QuickSort using last element as pivot:**   

```cpp
 
/* This function takes last element as pivot, places the pivot element at its correct position in sorted
array, and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot */
int partition_last_element(int arr[], int low, int high)
{
    int pivot = arr[high]; // pivot
    int i = (low - 1); // Index of smaller element and indicates the right position of pivot found so far
 
    for (int j = low; j <= high - 1; j++)
    {
        // If current element is smaller than the pivot
        if (arr[j] < pivot)
        {
            i++; // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

/* The main function that implements QuickSort
arr[] --> Array to be sorted,
low --> Starting index,
high --> Ending index */
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
        at right place */
        int pi = partition_last_element(arr, low, high);
 
        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

```

**Implementation of QuickSort using first element as pivot:**

```cpp
int partition_first_element(int arr[], int low, int high)
{
    int i = low;
    int j = high;
    int pivot = arr[low];
    while (i < j)
    {
        while (pivot >= arr[i])
            i++;
        while (pivot < arr[j])
            j--;
        if (i < j)
            swap(arr[i], arr[j]);
    }
    swap(arr[low], arr[j]);
    return j;
}

// QuickSort Function will be same as above, but this time we will use first element as pivot.
```    

**Analysis of QuickSort**   

Time taken by QuickSort, in general, can be written as following.   
$T(n) = T(k) + T(n-k-1) + Θ(n)$   
The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.  

- **Worst Case:** The worst case occurs when the partition process always picks greatest or smallest element as pivot. If we consider above partition strategy where last element is always picked as pivot, the worst case would occur when the array is already sorted in increasing or decreasing order. Following is recurrence for worst case. 
    $T(n) = T(0) + T(n-1) + \theta(n)$ Which is equivalent to $T(n) = T(n-1) + \theta(n)$  
    
    **The solution of above recurrence is (n2).**  
- **Best Case:** The best case occurs when the partition process always picks the middle element as pivot. Following is recurrence for best case. 
    $ T(n) = 2T(n/2) + \theta(n)$
    **The solution of above recurrence is (nLogn). It can be solved using case 2 of Master Theorem.**
- **Average Case:** To do average case analysis, we need to consider all possible permutation of array and calculate time taken by every permutation which doesn’t look easy.    
We can get an idea of average case by considering the case when partition puts O(n/9) elements in one set and O(9n/10) elements in other set. Following is recurrence for this case.  
$T(n) = T(n/9) + T(9n/10) + \theta(n)$    
    **The solution of above recurrence is also O(nLogn)**

**More Variations of Quick Sort**

**1. 3-Way QuickSort:** In QuickSort algorithm, we select an element as pivot, partition the array around pivot and recur for subarrays on left and right of pivot.    
Consider an array which has many redundant elements. For example, {1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4}. If 4 is picked as pivot in Simple QuickSort, we fix only one 4 and recursively process remaining occurrences. In 3 Way QuickSort, an array arr[l..r] is divided in 3 parts:    
- arr[l..i] elements less than pivot. 
- arr[i+1..j-1] elements equal to pivot. 
- arr[j..r] elements greater than pivot.   

See [3-Way-Quick-Sort-Implementation](https://www.geeksforgeeks.org/3-way-quicksort-dutch-national-flag/)   

**2. QuickSort for Linked Lists:** Simply see the implementation on singly and doubly linked list [QuickSort on Singly Linked List](https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/) & [QuickSort on Doubly Linked List](https://www.geeksforgeeks.org/quicksort-for-linked-list/)    

**3. Iterative Quick Sort:** Above is the recursive implementation of Quick Sort. Following is [iterative implementation of Quick Sort](https://www.geeksforgeeks.org/iterative-quick-sort/).    

[More Detail on Quick Sort](https://www.geeksforgeeks.org/quick-sort/)    
#### Radix Sort

The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort. Using Radix Sort an array in linear time.     

**Radix Sort Algorithm**

- Find the maximum element of the array, let it be $max$.
- Find the number of digits in $max$, let it be $k$.
- For each, $i$ ranging from $1$ To $k$, apply the counting sort algorithm for the $i^{th}$ least-significant digit of each element. If any element has less than $i$ digits consider $0$ at its place (Because $29$ can also be represented as $029$).    

![Radix Sort Algorithm](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Radix_Sort_Format.png?raw=true)    

**Radix Sort Pseudocode**     

```cpp
RadixSort(a[], n):
    // Finding the maximum element
    max=a[0]
    For (i=1 to n-1):
        If (a[i]>max):
            max=a[i]
            
    // Calling countingSort for 
    // k times using For loop.
    For (div=1 to max/div>0):
        countingSort(a, n, div)
        div=div*10
```   

**Example :**   

![Radix Sort Example](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Radix_Sort_Example.png?raw=true)    

**Explanation :**    

- *Original, unsorted list: 326, 453, 608, 835, 751, 435, 704, 690.*  
- *1st LSD i.e. Sorting by least significant digit (1s place) will be sorted in assending order as we need to sort this list in assending order.*   
- *Then 2nd LSD i.e. Sorting by next digit (10s place) will and sorted.*   
- *Then 3rd MSD Sorting by the most significant digit (100s place).*   

```cpp
// A function to do counting sort of arr[] according to the digit represented by exp.
void countSort(int arr[], int n, int exp)
{
    int output[n]; // output array
    int i, count[10] = { 0 };
  
    // Store count of occurrences in count[]
    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
  
    // Change count[i] so that count[i] now contains actual position of this digit in output[]
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
  
    // Build the output array
    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
  
    // Copy the output array to arr[], so that arr[] now contains sorted numbers according to current digit
    for (i = 0; i < n; i++)
        arr[i] = output[i];
}
  
// The main function to that sorts arr[] of size n using Radix Sort
void radixsort(int arr[], int n)
{
    // Find the maximum number to know number of digits
    int m = getMax(arr, n);
  
    // Do counting sort for every digit. Note that instead of passing digit number, exp 
    // is passed. exp is 10^i where i is current digit number
    for (int exp = 1; m / exp > 0; exp *= 10)
        countSort(arr, n, exp);
}
```

- **Time Complexity:** Let there be $d$ digits in input integers. Radix Sort takes $O(d*(n+b))$ time where $b$ is the base for representing numbers, for example, for the decimal system, $b$ is $10$. What is the value of $d$? If $k$ is the maximum possible value, then $d$ would be $O(logb(k))$. So overall time complexity is $O((n+b) * logb(k))$.   

- **Space Complexity:** In this algorithm, we have two auxiliary arrays cnt of size $b$ (base) and tempArray of size $n$ (number of elements), and an input array arr of size $n$. So, Overall space complexity is $O(n+b)$.    

**More Details:**   

- [Time and Space Complexity of Radix Sort](https://iq.opengenus.org/time-and-space-complexity-of-radix-sort/)   
- [Radix Sort on GeeksforGeeks](https://www.geeksforgeeks.org/radix-sort/)  
- [Radix Sort on Scaler](https://www.scaler.com/topics/data-structures/radix-sort/)

#### Counting Sort

Counting sort is a linear time sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then do some arithmetic to calculate the position of each object in the output sequence. It sort in O(n+k) time when elements are in the range from 1 to k.    

*Counting sort makes assumptions about the data*, for example, it assumes that values are going to be in the range of 0 to 10 or 10 – 99 etc, Some other assumptions counting sort makes are input data will be all real numbers. Like other algorithms this sorting algorithm is not a comparison-based algorithm, it hashes the value in a temporary count array and uses them for sorting. It uses a temporary array making it a *Non-In-Place-Algorithm*.    

**Algorithm :**   

- *Consider a given array that needs to be sorted. First, you’ll have to find the largest element in the array and set it to the max.* 
- *To store the sorted data, you will now initialize a new count array with length "max+1" and all elements set to 0.*
- *Later, as shown in the figure, you will store elements of the given array with the corresponding index in the count array.*
- *Now, you will change the count array by adding the previous counts to produce the cumulative sum of an array, as shown below.*
- *Because the original array has nine inputs, you will create another empty array with nine places to store the sorted data, place the elements in their correct positions, and reduce the count by one.*
- *As a result, the sorted array is: shown below*

![Count Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/countingsort.gif?raw=true)

**Pseudocode of Counting Sort**

```cpp
CountingSort(A)
  //A[]-- Initial Array to Sort
  // Complexity: O(k)
  for i = 0 to k do
  c[i] = 0
  // Storing Count of each element
  // Complexity: O(n)
  for j = 0 to n do
  c[A[j]] = c[A[j]] + 1
  // Change C[i] such that it contains actual position of these elements in output array
  // Complexity: O(k)
  for i = 1 to k do
  c[i] = c[i] + c[i-1]
  // Build Output array from C[i]
  // Complexity: O(n)
  for j = n-1 downto 0 do
  B[ c[A[j]]-1 ] = A[j]
  c[A[j]] = c[A[j]] - 1
end func
```

*Below is code implementation.*

```cpp
// The main function that sort the given string arr[] in alphabetical order
void countSort(char arr[])
{
    int RANGE=255;
    // The output character array that will have sorted arr
    char output[strlen(arr)];
 
    // Create a count array to store count of individual characters and initialize count array as 0
    int count[RANGE + 1], i;
    memset(count, 0, sizeof(count));
 
    // Store count of each character
    for (i = 0; arr[i]; ++i)
        ++count[arr[i]];
 
    // Change count[i] so that count[i] now contains actual position of this character in output array
    for (i = 1; i <= RANGE; ++i)
        count[i] += count[i - 1];
 
    // Build the output character array
    for (i = 0; arr[i]; ++i) {
        output[count[arr[i]] - 1] = arr[i];
        --count[arr[i]];
    }
 
    /*
    For Stable algorithm
    for (i = sizeof(arr)-1; i>=0; --i)
    {
        output[count[arr[i]]-1] = arr[i];
        --count[arr[i]];
    }
    */
 
    // Copy the output array to arr, so that arr now contains sorted characters
    for (i = 0; arr[i]; ++i)
        arr[i] = output[i];
}
``` 

- **Time Complexity:** O(n+k) where n is the number of elements in the input array and k is the range of input. 
- **Auxiliary Space:** O(n+k) 

**Facts:**   

**1. What if the elements are in the range from $1$ to $n^2$ :** We can’t use counting sort because counting sort will take O(n2) which is worse than comparison-based sorting algorithms. **Can we sort such an array in linear time?:-** *Radix Sort is the answer. The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort.*   
*2. Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K.*   
*3. It is not a comparison-based sorting. Its running time complexity is O(n) with space proportional to the range of data.*   
*4. Counting sort is able to achieve this because we are making assumptions about the data we are sorting.*  

**More Details:**   

- [Counting Sort on InterviewCake](https://www.interviewcake.com/concept/python/counting-sort)  
- [Counting Sort on Simplilearn](https://www.simplilearn.com/tutorials/data-structure-tutorial/counting-sort-algorithm)  
- [Counting Sort on GeekforGeeks](https://www.geeksforgeeks.org/counting-sort/)  
- [Counting Sort Pseudocode](https://www.codingeek.com/algorithms/counting-sort-explanation-pseudocode-and-implementation/)    

#### Bucket Sort

Bucket sort is mainly useful when input is uniformly distributed over a range and with floating-point values or even integers. It uses Scatter-gather approach as given below. Hence, it work great for smaller values but not for larger values.

The idea is to use bucket sort. Following is bucket algorithm.    

```cpp
bucketSort(arr[], n)
1) Create n empty buckets (Or lists).
2) Do following for every array element arr[i].
.......a) Insert arr[i] into bucket[n*array[i]]
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.
```   

*The basic procedure of performing the bucket sort is given as follows -*

- First, partition the range into a fixed number of buckets.    
- Then, toss every element into its appropriate bucket.    
- After that, sort each bucket individually by applying a sorting algorithm.    
- And at last, concatenate all the sorted buckets.   

![Bucket Sort Image](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Bucket_Sort.png?raw=true)   

Below is code implementation.    

```cpp
// Function to sort arr[] of
// size n using bucket sort
void bucketSort(float arr[], int n)
{
     
    // 1) Create n empty buckets
    vector<float> b[n];
 
    // 2) Put array elements
    // in different buckets
    for (int i = 0; i < n; i++) {
        int bi = n * arr[i]; // Index in bucket
        b[bi].push_back(arr[i]);
    }
 
    // 3) Sort individual buckets
    for (int i = 0; i < n; i++)
        sort(b[i].begin(), b[i].end());
 
    // 4) Concatenate all buckets into arr[]
    int index = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < b[i].size(); j++)
            arr[index++] = b[i][j];
}
```   

- **Time Complexity:** Best and Average-case complexity of bucket sort is $O(n + k)$, and the worst-case complexity of bucket sort is $O(n^2)$, where n is the number of items.

- **Space Complexity:** $O(n*k)$ as it is not a in-place sorting algorithm.

**More Details:**   
- [Bucket Sort on GeeksforGeeks](https://www.geeksforgeeks.org/bucket-sort-2/)
- [Bucket Sort on Javatpoint](https://www.javatpoint.com/bucket-sort)

#### ShellSort

Shell sort is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has to be moved far ahead, many movements are involved. The idea of ShellSort is to allow the exchange of far items. In Shell sort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. An array is said to be h-sorted if all sublists of every h’th element are sorted.   

*The interval between the elements is reduced based on the sequence used. Some of the optimal sequences that can be used in the shell sort algorithm are:*

- Shell's original sequence: N/2 , N/4 , …, 1  
- Knuth's increments: 1, 4, 13, …, (3k – 1) / 2  
- Sedgewick's increments: 1, 8, 23, 77, 281, 1073, 4193, 16577...4j+1+ 3·2j+ 1  
- Hibbard's increments: 1, 3, 7, 15, 31, 63, 127, 255, 511…  
- Papernov & Stasevich increment: 1, 3, 5, 9, 17, 33, 65,...   
- Pratt: 1, 2, 3, 4, 6, 9, 8, 12, 18, 27, 16, 24, 36, 54, 81....     

**Algorithm:**   
**Step 1** − Start
**Step 2** − Initialize the value of gap size. Example: h
**Step 3** − Divide the list into smaller sub-part. Each must have equal intervals to h
**Step 4** − Sort these sub-lists using insertion sort
**Step 5** – Repeat this step 2 until the list is sorted.
**Step 6** – Print a sorted list.
**Step 7** – Stop.

![Shell Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Shell_Sort.png?raw=true)   

Below is code implementation

```cpp
/* function to sort arr using shellSort */
int shellSort(int arr[], int n)
{
    // Start with a big gap, then reduce the gap
    for (int gap = n/2; gap > 0; gap /= 2)
    {
        // Do a gapped insertion sort for this gap size.
        // The first gap elements a[0..gap-1] are already in gapped order
        // keep adding one more element until the entire array is
        // gap sorted 
        for (int i = gap; i < n; i += 1)
        {
            // add a[i] to the elements that have been gap sorted
            // save a[i] in temp and make a hole at position i
            int temp = arr[i];
  
            // shift earlier gap-sorted elements up until the correct 
            // location for a[i] is found
            int j;            
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                arr[j] = arr[j - gap];
              
            //  put temp (the original a[i]) in its correct location
            arr[j] = temp;
        }
    }
    return 0;
}
```    

- **Time Complexity:** Time complexity of the above implementation of Shell sort is Worst Case $O(n^2)$. There are many other ways to reduce gaps as given above which leads to better time complexity.  
- **Space Complexity:** $O(1)$


**More Details:**   

- [ShellSort on GeeksforGeeks](https://www.geeksforgeeks.org/shellsort/)
- [ShellSort on Javatpoint](https://www.javatpoint.com/shell-sort)  
- [ShellSort on Programiz](https://www.programiz.com/dsa/shell-sort) 

#### Comb Sort

Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always compares adjacent values. So all inversions are removed one by one. Comb Sort improves on Bubble Sort by using a gap of the size of more than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1. Thus Comb Sort removes more than one inversion count with one swap and performs better than Bubble Sort.   

*The process of performing the comb sort -*   

- Calculate the gap value if gap value==1 {Print the sorted array} else {Iterate over data set and compare each item with gap item}
- While Iterate over data set and compare each item with gap item then {Swap the element if require else}
- At last print the array when gap value==1 Print the sorted array or not if not needed.

![Comb Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Comb_Sort.png?raw=true)   

Below is code implementation.    

```cpp
// To find gap between elements
int getNextGap(int gap)
{
    // Shrink gap by Shrink factor
    gap = (gap*10)/13;
 
    if (gap < 1)
        return 1;
    return gap;
}
 
// Function to sort a[0..n-1] using Comb Sort
void combSort(int a[], int n)
{
    // Initialize gap
    int gap = n;
 
    // Initialize swapped as true to make sure that
    // loop runs
    bool swapped = true;
 
    // Keep running while gap is more than 1 and last
    // iteration caused a swap
    while (gap != 1 || swapped == true)
    {
        // Find next gap
        gap = getNextGap(gap);
 
        // Initialize swapped as false so that we can
        // check if swap happened or not
        swapped = false;
 
        // Compare all elements with current gap
        for (int i=0; i<n-gap; i++)
        {
            if (a[i] > a[i+gap])
            {
                swap(a[i], a[i+gap]);
                swapped = true;
            }
        }
    }
}
```   

- **Time Complexity:** Average case time complexity of the algorithm is $Ω(N^2/2^p)$, where p is the number of increments. The worst-case complexity of this algorithm is $O(n^2)$ and the Best Case complexity is $O(nlogn)$.   
- **Auxiliary Space:** $O(1)$.   

**More Details:**   

- [CombSort on GeeksforGeeks](https://www.geeksforgeeks.org/comb-sort/)  
- [CombSort on Javatpoint](https://www.javatpoint.com/comb-sort)  
- [CombSort on Opengenus](https://iq.opengenus.org/comb-sort/)  

#### Pigeonhole Sort

To perform this sort, we need to make some holes. The number of holes needed is decided by the range of numbers. In each hole, items are inserted. Finally deleted from the hole and stored into an array for sorted order. It requires O(n + Range) time where n is number of elements in input array and ‘Range’ is number of possible values in array.   

**Working of Algorithm :**   

- Find minimum and maximum values in array. Let the minimum and maximum values be ‘min’ and ‘max’ respectively. Also find range as ‘max-min+1’. 
- Set up an array of initially empty “pigeonholes” the same size as of the range.
- Visit each element of the array and then put each element in its pigeonhole. An element arr[i] is put in hole at index arr[i] – min.
- Start the loop all over the pigeonhole array in order and put the elements from non- empty holes back into the original array. 

![Pigeonhole Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Pigeonhole_Sort.jpg?raw=true)

Below is code implementation.    

```cpp
// Sorts the array using pigeonhole algorithm
void pigeonholeSort(int arr[], int n)
{
    // Find minimum and maximum values in arr[]
    int min = arr[0], max = arr[0];
    for (int i = 1; i < n; i++)
    {
        if (arr[i] < min)
            min = arr[i];
        if (arr[i] > max)
            max = arr[i];
    }
    int range = max - min + 1; // Find range
  
    // Create an array of vectors. Size of array range. Each vector represents a hole that
    // is going to contain matching elements.
    vector<int> holes[range];
  
    // Traverse through input array and put every
    // element in its respective hole
    for (int i = 0; i < n; i++)
        holes[arr[i]-min].push_back(arr[i]);
  
    // Traverse through all holes one by one. For
    // every hole, take its elements and put in array.
    int index = 0;  // index in sorted array
    for (int i = 0; i < range; i++)
    {
       vector<int>::iterator it;
       for (it = holes[i].begin(); it != holes[i].end(); ++it)
            arr[index++]  = *it;
    }
}
```   

- **Time Complexity:** O(n+2^k) 
- **Space Complexity:** O(2^k) 

**More Details:**   

- [Pigeonhole Sort on GeeksforGeeks](https://www.geeksforgeeks.org/pigeonhole-sort/)  
- [Pigeonhole Sort on Tutorialspoint](https://www.tutorialspoint.com/Pigeonhole-Sort)  
- [Pigeonhole Sort on Opengenus](https://iq.opengenus.org/pigeonhole-sorting/)  

#### Cycle Sort

Cycle sort is a comparison sorting algorithm that forces array to be factored into the number of cycles where each of them can be rotated to produce a sorted array. It is theoretically optimal in the sense that it reduces the number of writes to the original array.   
It is an in-place and unstable sorting algorithm. Cycle sort forces an array to be factored into a number of cycles where every element can rotate in order to produce a sorted array.   

**Algorithm**  
Suppose there is an array arr with n distinct elements. Given an element A, we can find its index by counting the number of elements smaller than A.  

- If the element is at its correct position, simply leave it as it is.
- Else, we have to find the correct position of A by counting the number of elements smaller than it. Another element B is replaced to be moved to its correct position. This process continues until we get an element at the original position of A.

The above-illustrated process constitutes a cycle. Repeat this cycle for every element of the list until the list is sorted.

![Cycle Sort](https://github.com/thisiskushal31/Datastructures-and-Algorithms/blob/main/Algorithms/assets/Cycle_Sort.png?raw=true)   

Below is code implementation.    

```cpp
// Function sort the array using Cycle sort
void cycleSort(int arr[], int n)
{
    // count number of memory writes
    int writes = 0;
 
    // traverse array elements and put it to on
    // the right place
    for (int cycle_start = 0; cycle_start <= n - 2; cycle_start++) {
        // initialize item as starting point
        int item = arr[cycle_start];
 
        // Find position where we put the item. We basically
        // count all smaller elements on right side of item.
        int pos = cycle_start;
        for (int i = cycle_start + 1; i < n; i++)
            if (arr[i] < item)
                pos++;
 
        // If item is already in correct position
        if (pos == cycle_start)
            continue;
 
        // ignore all duplicate  elements
        while (item == arr[pos])
            pos += 1;
 
        // put the item to it's right position
        if (pos != cycle_start) {
            swap(item, arr[pos]);
            writes++;
        }
 
        // Rotate rest of the cycle
        while (pos != cycle_start) {
            pos = cycle_start;
 
            // Find position where we put the element
            for (int i = cycle_start + 1; i < n; i++)
                if (arr[i] < item)
                    pos += 1;
 
            // ignore all duplicate  elements
            while (item == arr[pos])
                pos += 1;
 
            // put the item to it's right position
            if (item != arr[pos]) {
                swap(item, arr[pos]);
                writes++;
            }
        }
    }
 
    // Number of memory writes or swaps
    // cout << writes << endl ;
}
```

- **Time Complexity:** $O(n^2)$ in best,average,worst case
- **Space Complexity:** $O(1)$, space complexity is constant cause this algorithm is in place so it does not use any extra memory to sort.

**More Details:**   

- [Cycle Sort on GeeksforGeeks](https://www.geeksforgeeks.org/cycle-sort/)  
- [Cycle Sort Sort on Javatpoint](https://www.javatpoint.com/cycle-sort)  
- [Cycle Sort Sort on Opengenus](https://iq.opengenus.org/cycle-sort/)  

#### Tim Sort 

*TimSort* is a sorting algorithm based on Insertion Sort and Merge Sort.  

It is better explained in the geeksforgeeks [article](https://www.geeksforgeeks.org/timsort/) and also on [delftstack](https://www.delftstack.com/tutorial/algorithm/tim-sort/).
### Summary   

#### Searching Algorithms

Here is list of all the algorithm discussed above with there time and space complexity.

| Algorithm  | Best Time Complexity | Average Time Complexity | Worst Time Complexity | Space Complexity |
| ---- | ---- | ---- | ---- | ---- |
| **Linear Search** | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ |
| **Binary Search** | $O(1)$ | $O(log n)$ | $O(log n)$ | $O(1)$ |
| **Jump Search**   | $O(1)$ | $O(√n)$ | $O(√n)$ | $O(1)$ |
| **Interpolation Search** | $O(1)$ | $O(log(logn))$ | $O(n)$ | $O(1)$ |
| **Exponential Search** | $O(1)$ | $O(log n)$ | $O(log n)$ | $O(1)$ |
| **Ternary Search** | $O(1)$ | $O(log{_3}n)$ | $O(log{_3}n)$ | $O(1)$ |
| **Fibonacci Search** | $O(1)$ | $O(logn)$ | $O(logn)$ | $O(1)$ |

#### Sorting Algorithms

Here is list of all the algorithm discussed above with there time and space complexity.   

| Algorithm  | In Place | Stable | Best Time Complexity | Average Time Complexity | Worst Time Complexity | Space Complexity |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **Selection Sort** | Yes | Unstable | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Bubble Sort**    | Yes | Stable | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Insertion Sort** | Yes | Stable | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Merge Sort**     | No | Stable | $O(nlogn)$ | $O(nlogn)$ | $O(nlogn)$ | $O(n)$ |
| **Heap Sort**      | Yes | Unstable | $O(nlogn)$ | $O(nlogn)$ | $O(nlogn)$ | $O(1)$ |
| **Quick Sort**     | No | Unstable | $O(nlogn)$ | $O(nlogn)$ | $O(n^2)$ | Worst-$O(n)$ Best-$O(logn)$ |
| **Radix Sort(1)**     | No | Stable | $O(n*k)$ | $O(n*k)$ | $O(n*k)$ | $O(n+k)$ |
| **Counting Sort(2)**  | No | Stable | $O(n+k)$ | $O(n+k)$ | $O(n+k)$ | $O(k)$ |
| **Bucket Sort(3)**    | No | Depends on the sorting algorithm used to sort the bucket | $O(n)$ | $O(n+n^{2}/k + k)$ | $O(n^2)$ | $O(n*k)$ |
| **Shell Sort**     | Yes | Unstable | $O(nlogn)$ | $O(nlogn)$ | $O(n^2)$ | $O(1)$ |
| **Comb Sort**      | Yes | Stable | $O(nlogn)$ | $O(n^2/2^p)$(p is a number of increment) | $O(n^2)$ | $O(1)$ |
| **Pigeonhole Sort(4)**| No | Stable | $O(n+N)$ | $O(n+N)$ | $O(n+N)$ | $O(n+N)$ |
| **Cycle Sort**     | Yes | Unstable | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Tim Sort**       | No | Hybrid Stable | $O(n)$ | $O(nlogn)$ | $O(nlogn)$ | $O(n)$ |

-  *(1)-k represents the number of digits in the largest number in the array*
- *(2)- k represents the difference between the smallest and the largest array value*
- *(3)- k represents the number of buckets*
- *(4)- n is the number of elements and N is the range of the input data*

**References**   

- [Sorting Algorithm CheatSheat](https://www.interviewcake.com/sorting-algorithm-cheat-sheet)  


> **Source:** *GeeksforGeeks*           
> [https://www.geeksforgeeks.org/fundamentals-of-algorithms](https://www.geeksforgeeks.org/fundamentals-of-algorithms/#SearchingandSorting)        