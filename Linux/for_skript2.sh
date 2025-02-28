#! /bin/bash

arg_i=0

# @:1 liefert die gesamte Argumentenlisten zurück
# @:1:1 liefert das erste Element der Argumentenliste zurück

echo "${@:1:1}"
echo "${@:2:1}"
echo "${@:3:1}"

for arg in $@
do
echo "Argumente: $arg"

arg[$arg_i]=$arg

arg_i=$((arg_i+1))
done

echo "zweites Argument: ${arg[1]}"
echo "${@:1:1}"
