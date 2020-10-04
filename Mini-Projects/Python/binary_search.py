stack = [7, 7, 22, 37, 47, 57, 57, 86, 91]
needle = int(input("Enter the number you are searching for: "))
length = len(stack)
lower_bound = 0
upper_bound = length - 1
found = False

while found == False and lower_bound <= upper_bound:
    mid_point = (lower_bound + upper_bound) // 2
    if stack[mid_point] == needle:
        print("Your number has been found")
        found = True
    elif stack[mid_point] < needle:
        lower_bound = mid_point + 1
    else:
        upper_bound = mid_point - 1

if found == False:
    print("Your number is not in the list")
