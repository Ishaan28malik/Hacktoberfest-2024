def linear_Search(list1, n, key):  
 
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1 