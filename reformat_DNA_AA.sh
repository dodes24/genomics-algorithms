# encoding=utf-8
#!/bin/bash

if [ $# -ne 1 ]; then
    echo $"> SEQ"
    grep -oz '[A-N,P-T,V-Z,a-n,p-t,v-z,*,-]*' $1 | tr -d "\r" | tr -d "\n" | tr -d " " | tr -d '\000'
else
    echo $">$1"
    grep -oz '[A-N,P-T,V-Z,a-n,p-t,v-z,*,-]*' $1 | tr -d "\r" | tr -d "\n" | tr -d " " | tr -d '\000'
fi

