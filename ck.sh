#!/bin/bash

date
lastDate=2021-09-23
result=r.txt
./checkNVD.py $lastDate > $result
cat $result | grep ASSIGN
cat $result | grep value
