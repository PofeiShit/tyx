#!/bin/bash
echo "this script is to rename picture"


for names in images/*.jpg
do 
	news=$i
	mv $names images/$news.jpg
	let i=i+1
done
