#!/bin/bash
a=5
b=0

for i in $(seq 1 100)
do
    b=$(( $b + $(( $i * $a))))

    done
echo $b