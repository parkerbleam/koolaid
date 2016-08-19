#!/bin/bash
while true
do
	sudo nmap -sP -n 10.0.1.0/24 | grep MAC > MAC-scrape.txt
	date >> MAC-scrape.txt
	sleep 60 
done
