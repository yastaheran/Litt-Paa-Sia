#!/bin/bash

if [ $1 = "--AMPM" ]; then
	while sleep 1; do
		clear
		now=$(date +%r)
		printf "Current time: %s \n" "$now"
	done
else
	while sleep 1; do
		clear
		now=$(date +%T)
		printf "Current time: %s \n" "$now"
	done
fi
