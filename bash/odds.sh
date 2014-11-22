#!/usr/bin/env bash

echo "Bash version $BASH_VERSION..."

for X in {0..99}; do
    if (( X % 2 == 1 )); then
        echo "$X"
    fi
done
