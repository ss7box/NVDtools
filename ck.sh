#!/bin/bash

date
startDate=2023-03-21
endDate=2023-03-23
result=r.txt
./r2.checkNVD.py $startDate $endDate > $result
cat $result | grep "vulnStatus\|ASSIGN\|value\|CVE-\|sourceIdentifier"
