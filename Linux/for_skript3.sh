#! /bin/bash

if [ $# -eq 0 ]
then
	echo "Bitte mindestens einen Namen nennen!"
	exit 1
else
	echo -n "Hallo $1"
	shift
	for name in $@
	do
#	echo "$name"
		echo $name | grep "^[A-Za-z]*$" > /dev/null
		if [ $? -eq 1 ]  # Der Exit code von grep ist 1, wenn der Name NICHT NUR Buchstaben enthält
		then 
			echo " "
			echo "ERROR: Der Name $name besteht nicht nur aus Buchstaben!"
			exit 2
		else
			echo -n ", und $name"
		fi
	done
	echo "!"
	exit 0
fi

