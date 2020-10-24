def towers(num,frompeg,topeg,auxpeg):
    if (num == 1):
        print("Move disk 1 from peg %c to peg %c"% (frompeg, topeg))
        return
    towers(num - 1, frompeg, auxpeg, topeg)
    print("Move disk %d from peg %c to peg %c"% (num, frompeg, topeg))
    towers(num - 1, auxpeg, topeg, frompeg)


print("Enter the number of disks : ")
num=int(input())
print("The sequence of moves involved in the Tower of Hanoi are :")
towers(num, 'A', 'B', 'C')
