#!/bin/bash
while true
do
	arp -a -n | grep ? > MAC-scrape.txt
	date >> MAC-scrape.txt
	sleep 60 
done
