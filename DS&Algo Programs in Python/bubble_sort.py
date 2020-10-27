# Implementing bubble sort algorithm

def bubble_sort(nums):
    # We set swapped to True so the Loop runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                # Swap the elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
                # Set the flag to True so we will loop again
                swapped = True

# Verify it works
random_list_of_nums = [20, 199, 4, 56, 99, 37, 68]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)