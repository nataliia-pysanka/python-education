#!/bin/bash

#script prints sorted files in local dir

counter=0
echo ""
echo "There are files in dir $(pwd):"

for file in $(ls | tr " " "_" | sort)
do
        echo $counter : $file
        counter=$[$counter + 1]
done

echo ""
echo "Now: $(date +'%d-%m-%Y %H:%M')"
