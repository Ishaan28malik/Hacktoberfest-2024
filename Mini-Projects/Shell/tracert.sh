#!/usr/bin/env bash

if [[ -z "$1" || "$@" == *'-h'* ]]
	then echo -e "Usage:
 $(basename -- $0) [IP]
 $(basename -- $0) [DOMAIN]
"
exit

fi


##################################################################################
##################################################################################


timeout=2 #seconds


##################################################################################
##################################################################################


host=$1
i=1


while true
do 
	ping=$(ping -t $i -c 1 -W $timeout $host | grep -E "From|from")
	[[ $? > 0 && $i == 1 ]] && exit
	if [[ $(echo $ping | cut -d ' ' -f 1) == "64" ]]
		then
			#Last hop in route
			 
			if [[ $(echo $ping | cut -d ' ' -f 4 | tr -d '():' ) =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]] 
				then echo -e "$i\t$(echo $ping | cut -d ' ' -f 4 | tr -d '():' )\t$(if [[ "$1" =~ [1-9][0-9].. && ${#1} == 4 ]]; then echo $1; else echo $host; fi)"
				else echo -e "$i\t$(echo $ping | cut -d ' ' -f 5 | tr -d '():' )\t$(echo $ping | cut -d ' ' -f 4)"
			fi

			exit 0
		
		else		
	
			if [[ $(echo $ping | cut -d ' ' -f 3 | tr -d '():') =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]
    		    then echo -e "$i\t$(echo $ping | cut -d ' ' -f 3 | tr -d '():')\t$(echo $ping | cut -d ' ' -f 2)"
				else echo -ne "$i\t$(echo $ping | cut -d ' ' -f 2)\t"
					if [[ $(echo $ping | cut -d ' ' -f 2) =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]
						then echo -e "$(host $(echo $ping | cut -d ' ' -f 2) | cut -d ' ' -f 5 | sed 's/\.$//g' | sed 's/3(NXDOMAIN)//g')"
						else echo -e "*"
					fi
			fi
	fi
		

	((i++))
done 
