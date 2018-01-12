#!/bin/bash

## Display strings contained in files in the current directory
for file in $(ls|tr -s "" ":"|cut -d "." -f 1 | uniq);do 
	echo -en "file content $file\n" ; 
	strings $file;
echo;done