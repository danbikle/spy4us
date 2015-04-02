#!/bin/bash

# /home/ann/spy4us/publish2web.bash

# This script should use meteor to publish my predictions to the web.
# This script only runs on Ubuntu 14,
# not mac, not windows.

if [ -e /tmp/spy4us ]
then
  echo /tmp/spy4us exists.
  echo I am happy.
else
  echo /tmp/spy4us does not exist.
  echo We have a problem.
  echo Maybe /home/ann/spy4us/call_ml101.bash
  echo was not called?
  exit 1
fi

if [ `cat /home/ann/spy4us/sitename.txt` == 'spy.meteor.com' ]
then
  echo $0 will not run.
  echo Why?
  echo You need to read this file:
  echo /home/ann/spy4us/sitename_readme.txt
  exit 1
fi

cd /tmp/spy4us/
rm -rf spy4us
rsync -a /home/ann/spy4us/spy4us .
mkdir -p spy4us/public
cp -p *csv *png spy4us/public/

cd /tmp/spy4us/spy4us/
echo '<template name="t2">'         > t2.html
echo '<h3>head public/ff1.csv</h3>' >> t2.html
echo '<pre>'                        >> t2.html
head public/ff1.csv                 >> t2.html
echo '</pre>'                       >> t2.html
echo '<hr />'                       >> t2.html
echo '</template>'                  >> t2.html

~ann/.meteor/meteor deploy `cat /home/ann/spy4us/sitename.txt`

exit

