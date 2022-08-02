#!/bin/bash
while read item
do
	echo $item
	item=$(echo ${item}|base64 --decode)
	echo $item|jq '.os'
	#eval $(echo $item|jq -r '.|to_entries|.[]|.key + "=" + (.value|@sh)')
	#echo bla$os
done < <(cat imagetree.yml|python3 yaml2json.py|jq -r '.images["centos7"][] | @base64')
