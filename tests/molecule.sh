#!/bin/bash -eu

virtualenv="$1"
scenario="$2"

if test -z "$virtualenv"
then
	echo "virtualenv needed"
fi
if test -z "$scenario"
then
	echo "scenario needed"
fi
source "$virtualenv"
molecule test -s "$scenario"

