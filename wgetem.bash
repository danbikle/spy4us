#!/bin/bash

# /home/ann/spy4us/wgetem.bash

# This script should get CSV data from Yahoo.

mkdir -p /tmp/spy4us/
cd       /tmp/spy4us/

TKRH='%5EGSPC'
TKR='GSPC'
rm -f ${TKR}.csv

wget --output-document=${TKR}.csv  http://ichart.finance.yahoo.com/table.csv?s=${TKRH}
cat ${TKR}.csv | awk -F, '{print $1 "," $5}' > ${TKR}2.csv

exit
