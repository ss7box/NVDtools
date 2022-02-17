#!/bin/bash

date
startDate=2022-02-10
endDate=2022-02-17
result=r.txt
./checkNVD.py $startDate $endDate > $result
cat $result | grep ASSIGN
cat $result | grep value
