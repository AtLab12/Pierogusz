#!/bin/bash

# Execute Python script to generate LLVM IR
python3 main.py test_matrix.pierogusz
if [ $? -ne 0 ]; then
    echo "Error during Python script execution"
    exit 1
fi

# Optimize the LLVM IR
opt -O3 -S output.ll -o optimized.ll
if [ $? -ne 0 ]; then
    echo "Error during LLVM optimization"
    exit 1
fi

# Generate object file from LLVM IR
llc -filetype=obj optimized.ll
if [ $? -ne 0 ]; then
    echo "Error during LLVM to object file compilation"
    exit 1
fi

# Compile object file into executable
clang optimized.o runtime.o -o output -lc
if [ $? -ne 0 ]; then
    echo "Error during linking with Clang"
    exit 1
fi

# Run the executable
./output
if [ $? -ne 0 ]; then
    echo "Error during executable run"
    exit 1
fi