def binary_recursive(arr:list, low, high, tar:int):
    if low <= high:
        mid = low + ((high-low)//2)
        if tar == arr[mid]:
            return f"{tar} found at {mid}."
        elif tar < arr[mid]:
            return binary_recursive(arr, low, mid-1, tar)
        else:
            return binary_recursive(arr, mid+1, high, tar)
    else:
        return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    print(binary_recursive(arr, 0, len(arr)-1, 40))


