#! /bin/bash

echo 'Bei der Definiton von Variablen DARF MAN KEIN Leerzeichen nehmen: Username=$1'
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

echo 'ALLE Leerzeichen in "if [ $# -eq 1 ]" sind NOTWENDIG!'
if [ $# -eq 1 ] 
then
	username=$1
	echo "$username"
elif [ $# -eq 2 ]
then 
	username=$1
	username2=$2
	echo "$username und $username2"
else
	echo "Falsche Anzahl an Argumenten: $#"
fi   # HIER hört das if - Statement auf
