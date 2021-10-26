def binary_iterative(arr:list, low, high, tar:int):
    while low <= high:
        mid = low + ((high-low)//2)
        if arr[mid] == tar:
            return f"{tar} found at index {mid}."
        elif arr[mid] < tar:
            low = mid + 1
        elif arr[mid] > tar:
            high = mid - 1
    return f"{tar} not found"

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    print(binary_iterative(arr,0,len(arr)-1,40))
