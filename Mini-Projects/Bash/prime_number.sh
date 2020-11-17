#!/bin/bash

echo "Enter the number"
read number
two=2
zero=0

while [ $two -lt $number ]
do
  s=`expr $number % $two`
  if [ $s -eq $zero ]
  then
    echo $number" is not a prime number"
    exit
  else
    i=`expr $two + 1`
  fi
done

echo $number " is a pime number"
