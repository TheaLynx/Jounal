#! /bin/bash

#names="Dennis Florian Sarah"

#for name in $names
#do
#echo "$name"
#done

for name in $@
do 
echo "$name mit @"
done

echo "${@:1:1}"

#for name in "$*"
#do
#echo "$name mit *"
#done
