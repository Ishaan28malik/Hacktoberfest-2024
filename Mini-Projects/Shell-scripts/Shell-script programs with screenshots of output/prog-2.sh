#!/bin/bash

read -p "Enter the number "  num

flag=0

for ((i=1;i<=num/2;i++))
do
	if (( $num % i == 0 ))
	then
		((flag+=1))
	fi
done
if [ $flag -eq 1 ]
then
	echo "$num is a Prime Number"
else
	echo "$num is not a Prime Number"
fi
