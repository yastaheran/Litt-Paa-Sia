#!/bin/bash

#read variables from command line, one by one
operation=$1
shift;
math=$1
shift;

while [ $# -gt 0 ]
do
  case "$operation" in
    S)    #SUM
        math=$(($math + $1)) 
        shift; ;;
    P) 	  #PRODUCT
		math=$(($math * $1))
        shift; ;;	
    M)    #MAX
		if [ $1 -gt $math ]; then
			math=$1
		fi
		shift;
		;;
    m) 	  #MIN
      	if [ $1 -lt $math ]; then 
      		math=$1 
      	fi
      	shift;
		;;
  	*)	
  		echo 'not an valid operation'
		exit
		;;
  esac
done

echo $math