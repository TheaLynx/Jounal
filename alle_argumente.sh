#! /usr/bin/bash

names="Dennis Flo Sarah"

for name in $names
do
	echo "$name"
done

for name in "$@"
do
	echo "$name in @"
done

echo 
echo 'Benutzt man "$*" dann wird die Argumentenliste zu einem String.'
echo 'Es wird dann nur EINMAL ein Text in dieser Schleife ausgegeben.'
echo
for name in "$*"
do
	echo "$name in *"
done

echo
echo "Ohne Anführungszeichen wird die Liste nacheinander durchlaufen."
echo
for name in $*
do 
	echo "$name in *"
done
