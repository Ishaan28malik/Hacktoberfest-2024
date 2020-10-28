def binary_search(lst, n):
	start = 0
	end = len(lst) - 1
	lst.sort()
	while start <= end:
		mid = (start + end) // 2
		if lst[mid] == n:
			return mid
		elif lst[mid] < n:
			start = mid + 1
		else:
			end = mid - 1
	return -1

def main():
	print("Enter the elements of list separated by space: ")
	lst = [int(x) for x in input().split()]
	print("Enter the element to be searched: ")
	n = int(input())
	x = binary_search(lst, n)
	if x != -1:
		print("Element found at position: " + str(x + 1))
	else:
		print("Oops! Element not found!")

if __name__ == '__main__':
	main()
