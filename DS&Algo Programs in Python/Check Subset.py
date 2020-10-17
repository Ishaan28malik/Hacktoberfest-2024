#Program that checks if A is subset of B
def is_subset(listA, listB):
    if(len(listA) > len(listB)):#A is bigger than B, so not a subset
        return False
    else: #verify if is subset
        i = j = 0
        flag = 0
        listA.sort()
        listB.sort()
        sizeA = len(listA)
        while(i < len(listA) and j < len(listB)):
            if(listA[i] == listB[j]):
                i += 1
                j += 1
                sizeA -= 1
            else:
                j += 1
        if(sizeA == 0):
            return True
        else:
            return False

if __name__ == '__main__':
    number_of_tests = int(input())

    for i in range(number_of_tests):
        number_of_elem_A = int(input())
        numbers = input().split(maxsplit = number_of_elem_A)
        elements_A = list(map(int, numbers))

        # print(elements_A)

        number_of_elem_B = int(input())
        numbers = input().split(maxsplit = number_of_elem_B)
        elements_B = list(map(int, numbers))

        # print(elements_B)

        print(is_subset(elements_A, elements_B))
