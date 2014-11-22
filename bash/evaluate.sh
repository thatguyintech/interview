#!/bin/bash

read input
answer=`echo "scale=3; $input" | bc -l`
echo $answer

printf "%.3f" $(echo "scale=2; $input" | bc -l)
