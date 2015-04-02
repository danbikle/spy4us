#!/bin/bash

# /home/ann/spy4us/noon50.bash

# cron should call this script at 12:50pm California time.
# This script should call ml101.bash with correct variables.

# This should give me a YRS amount of predictions:
export YRS=15
# YRS should be >= TRAIN_YRS
# Each prediction should train from TRAIN_YRS amount of observations:
export TRAIN_YRS=10

# This should be yes when I want a prediction near calif-noon:55 m-f:
export HTML=yes
# At night, if I set HTML=yes a duplicate observation of the most recent close
# will appear in the data.
# So, at night, export HTML=no

# cron needs this:
export PATH=/home/ann/anaconda3/bin:$PATH

cd ~ann/spy4us/
./ml101.bash 
./publish2web.bash

exit
