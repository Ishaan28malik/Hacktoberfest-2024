#!/bin/bash 

# Take user Input 

echo "Enter 1st Number"
read num1
echo "Enter 2nd Number"
read num2
echo "Enter 3rd Number"
read num3

echo "The Largest Number is "

if [ $num1 -gt $num2 ] && [ $num1 -gt $num3 ]
then
    echo $num1
elif [ $num2 -gt $num1 ] && [ $num2 -gt $num3 ]
then
    echo $num2
else
    echo $num3
fi
