#!/bin/bash

clang -c -o runtime.o runtime.c
if [ $? -ne 0 ]; then
    echo "Error during creation runtime file"
    exit 1
fi

python3 main.py test_matrix.pierogusz
if [ $? -ne 0 ]; then
    echo "Error during Python script execution"
    exit 1
fi

clang -o output output.ll runtime.o -lm
if [ $? -ne 0 ]; then
    echo "Error during linking with Clang"
    exit 1
fi

./output
if [ $? -ne 0 ]; then
    echo "Error during executable run"
    exit 1
fi