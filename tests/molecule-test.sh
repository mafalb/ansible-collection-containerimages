#!/bin/bash -eu
virtualenv=$1
source "$virtualenv"
molecule test

