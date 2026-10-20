#!/bin/zsh

echo -n "Enter file path: "
read path

if [ -f "$path" ]; then 
    echo "File found: "$path
else
    echo "File not found: "$path
fi
