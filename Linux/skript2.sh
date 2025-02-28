#! /bin/bash

_user=$1
username=$2
x=4
y=3

z=x+y
a=3+4

echo "Hallo Ihr, $_user und $username"
echo 'Hallo Ihr, $_user und $username'
echo "Anzahl an Argumenten: $#"
echo "$x, $y, $z, $a"

if [ $# -eq 0 ]
then
	echo "Geben Sie mindestens 1 Argument an"
	exit 1
else
	echo "$@ oder $* Argumente wurden übergeben"
	echo "$@[1]"
	echo "$*"
	exit 0
fi
echo "Der Text steht hinter dem if und wird NIEMALS ausgegeben."
