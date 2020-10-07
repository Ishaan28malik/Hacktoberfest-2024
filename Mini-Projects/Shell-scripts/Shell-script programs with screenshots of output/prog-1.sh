#!/bin/bash

read -p "Enter Cost Price: "  cp
read -p "Enter Selling Price: "  sp

#temp=$(expr $sp - $cp)
temp=$((sp - cp))

if [ $sp -gt $cp ]
then
echo "Profit of $temp"

elif [ $sp -lt $cp ]
then
temp=$((-temp))
echo "Loss of $temp"

elif [ $sp -eq $cp ]
then
echo "Neither Profit nor Loss"

fi
