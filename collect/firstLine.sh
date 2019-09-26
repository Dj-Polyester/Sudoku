#!/bin/bash

filenames=("$@")

num=$(sed '1q;d' ${filenames[0]})

sed -i "1s/.*/$((num+1))/g" ${filenames[0]}
