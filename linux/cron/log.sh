#!/bin/bash

day=$(date +'%m/%d/%Y - %H:%M:%S')

filename="$HOME/log.txt"

echo $day >> $filename
