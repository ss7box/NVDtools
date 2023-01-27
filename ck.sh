#!/bin/bash

date
startDate=2023-01-20
endDate=2023-01-27
result=r.txt
./r2.checkNVD.py $startDate $endDate > $result
cat $result | grep ASSIGN
cat $result | grep value
