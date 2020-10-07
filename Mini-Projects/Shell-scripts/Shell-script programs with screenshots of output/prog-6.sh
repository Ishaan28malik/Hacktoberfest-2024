#!/bin/bash 

# Input type of operation 
while true
do
echo "1. Addition"
echo "2. Subtraction"
echo "3. Multiplication"
echo "4. Division"
echo "Enter Choice :"
read ch 

# Take user Input 
echo "Enter Two numbers : "
read a 
read b 

# Switch Case 
case $ch in
1)res=`echo $a + $b | bc` 
;; 
2)res=`echo $a - $b | bc` 
;; 
3)res=`echo $a \* $b | bc` 
;; 
4)res=`echo "scale=2; $a / $b" | bc` 
;; 
esac
echo "Result : $res"
done
