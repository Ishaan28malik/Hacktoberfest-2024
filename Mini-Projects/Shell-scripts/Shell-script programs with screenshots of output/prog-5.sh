#!/bin/bash 

echo -n "Enter the Total number of Subjects :"
read n 
echo "Enter the marks:"
i=0 

while [ $i -lt $n ] 
do
	read a[$i] 
	(( i=i+1 )) 
done

res=0

for i in "${a[@]}"
do
	(( res=res+$i )) 
done

res=$(( res / n ))
echo "Your Aggregate: $res"

if [[ $res -gt 80  && $res -le 100 ]]
then
	echo "Your Result: I-Division"

elif [[ $res -gt 60 && $res -le 80 ]]
then
	echo "Your Result: II-Division"
	
elif [[ $res -gt 40 && $res -le 60 ]]
then
	echo "Your Result: III-Division"
	
elif [[ $res -ge 0 && $res -le 40 ]]
then
	echo "Your Result: Fail"
	
else
	echo "Invalid Marks"
fi
