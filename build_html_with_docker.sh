#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

echo "Wipping build directory"
mkdir -p ./build/main
rm -rf ./build/main
mkdir -p ./build/main

echo "Generating HTML"
current_dir=`pwd`
current_dir=${current_dir#/mnt} # uncomment when using WSL1 with Docker on Windows 10
docker run --rm -v $current_dir:/project antonkrug/documentation-builders-ng:0fa69ed bash -c "cd /project/source/main && make html"