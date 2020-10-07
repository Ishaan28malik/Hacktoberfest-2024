#!/bin/bash

read -p "Enter the radius of circle "  r

pi=3.14

area=$(echo "$pi*$r*$r" | bc)
echo "Area of circle = $area"

circumf=$(echo "2*$pi*$r" | bc)
echo "Circumference of circle = $circumf"
