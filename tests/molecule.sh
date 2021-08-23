#!/bin/bash -eu

virtualenv="$1"
if test -z "$virtualenv"
then
	echo "virtualenv needed"
fi
source "$virtualenv"
molecule test

