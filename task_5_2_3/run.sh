#!/bin/bash

make clean
make

cat test.txt | ./dijkstra
