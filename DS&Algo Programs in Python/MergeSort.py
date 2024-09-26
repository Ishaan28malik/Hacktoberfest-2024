#----------------------------------------------------------#
#              MERGE SORT IMPLEMENTATION                   #
#----------------------------------------------------------#
import doctest


def merge_sort(collection: list) -> list:

    def merge(left: list, right: list) -> list:
        """
            merge left and right
            param left: left collection
            param right: right collection
            return: merge result
        """

        def _merge():
            while left and right:
                yield (left if left[0] <= right[0] else right).pop(0)
            yield from left
            yield from right

        return list(_merge())

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2                  # floor division calculate mid position 
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))

   

   
doctest.testmod()
user_input  = input("Enter numbers separated by a comma:\n").strip()    
unsorted    = [int(item) for item in user_input.split(",")]
print(*merge_sort(unsorted), sep=",")
