#!/bin/bash

# /home/ann/spy4us/ml101.bash

# This script should learn from GSPC observations and then predict.

# Demo:
# YRS=1 ; TRAIN_YRS=10 ; HTML=no ; ~ann/spy4us/ml101.bash

if [ -e ~ann/spy4us/ ]; then
  echo $0 is in the correct folder.
else
  echo $0 needs to reside here:
  echo ~ann/spy4us/
  echo bye.
  exit 1
fi

if [ -z "$YRS" ]; then
  YRS=2
fi  

if [ -z "$TRAIN_YRS" ]; then
  TRAIN_YRS=4
fi  

if [ -z "$HTML" ]; then
  HTML=no
fi  

echo YRS IS:
echo $YRS

echo TRAIN_YRS IS:
echo $TRAIN_YRS

echo HTML IS:
echo $HTML

mkdir -p /tmp/spy4us/
cd       /tmp/spy4us/

# I should get csv data
~ann/spy4us/wgetem.bash

if [ "$HTML" == 'yes' ]; then
  # I should get most recent price
  ~ann/spy4us/wgethtml.bash
  # I should extract recent prices from html
  python ~ann/spy4us/extprice.py
  # I should cat prices together
  echo 'cdate,cp'                            > GSPC3.csv
  cat GSPCrecent.csv GSPC2.csv|grep -v Date >> GSPC3.csv
  cat GSPC3.csv                              > GSPC2.csv 
fi  

# I should generate features
python ~ann/spy4us/genf.py GSPC2.csv
# That should give me
# /tmp/spy4us/ftrGSPC2.csv

# I should train from ftrGSPC2.csv and $TRAIN_YRS
python ~ann/spy4us/ml101.py $TRAIN_YRS $YRS
# That should give me
# /tmp/spy4us/prdf1.csv

# What happened?
python ~ann/spy4us/plotem.py /tmp/spy4us/prdf1.csv

# Do it Again (Feed-Forward)
python ~ann/spy4us/ml101ff.py $TRAIN_YRS $YRS
# That should give me
# /tmp/spy4us/ff1.csv

# What happened?
python ~ann/spy4us/plotem.py /tmp/spy4us/ff1.csv

exit
