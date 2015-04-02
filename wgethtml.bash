#!/bin/bash

# /home/ann/spy4us/wgethtml.bash

# This script helps me get most recent price

TKRH='%5EGSPC'
TKR='GSPC'
rm -f ${TKR}.html

wget --output-document=${TKR}.html http://finance.yahoo.com/q?s=$TKRH

exit

