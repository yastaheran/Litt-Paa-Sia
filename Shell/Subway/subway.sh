#!/bin/bash

if [ "$1" = "Forskningsparken" ]; then
	var1=$(curl -s "https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0")
elif [ "$1" = "Blindern" ]; then
	var1=$(curl -s "https://ruter.no/reiseplanlegger/Stoppested/(3010360)Blindern%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0")
elif [ "$1" = "Borgen" ]; then
	var1=$(curl -s "https://ruter.no/reiseplanlegger/Stoppested/(3012210)Ullev%C3%A5l%20stadion%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0")
fi

if [ "$2" = "--E" ]; then
	var2=${var1#*\"platforms\":\[\{\"name\":\"1}
	var3=${var2%\}\]\}\]\},\{\"name\":\"2 *}
#	echo $var3
elif [ "$2" = "--W" ]; then
	var2=${var1#*\}\]\}\]\},\{\"name\":\"2 }
	var3=${var2%\}\]\}\]\}\]\}\)\);*}
#	echo $var3
fi

counter=0
while [ $counter -lt 3 ]
do
	#Destination
	var4=${var3#*\"destination\":}
	var5=${var4%%,\"transportation\"*}
	
	#Time
	var6=${var3#*\"departureTime\":}
	var7=${var6%%,\"isRemainingTime\"*}
	
	counter=$(($counter + 1))
	var3=$var6
	echo $var5 $var7
done
