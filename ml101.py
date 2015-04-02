# ~ann/spy4us/ml101.py

# This script should generate predictions from ftrGSPC2.csv and $TRAIN_YRS

# Demo:
# cd /tmp/spy4us/
# python ~ann/spy4us/ml101.py 4
# or
# python ~ann/spy4us/ml101.py $TRAIN_YRS

import pdb
import pandas as pd
import numpy  as np
import sys

#  len(sys.argv) should == 3
if len(sys.argv) < 3:
  print('Demo:')
  print('cd /tmp/spy4us/')
  print('python ~ann/spy4us/ml101.py 4 10')
  sys.exit()

train_yrs = int(sys.argv[1])
yrs       = int(sys.argv[2])
# I should learn from this many observations:
train_count = 252 * train_yrs

# ml101ff.py needs me to double pcount here.
# I should calculate  this many predictions:
pcount      = 253 * yrs * 2

df1 = pd.read_csv('ftrGSPC2.csv')

# How many observations have I?
obs_count = len(df1)
print('I have this many observations: '+str(obs_count))

if pcount + train_count > obs_count:
  print('I dont have enough observations.')
  print('You want too many predictions.')
  print('You need to lower YRS and-or TRAIN_YRS.')
  sys.exit()
  
# I should get some training data from df1.
# I should put it in NumPy Arrays.

# I should declare some integers to help me navigate the Arrays.

cdate_i   = 0
cp_i      = 1
pctlead_i = 2
gspc4_i   = 3
gspc5_i   = 4
gspc6_i   = 5
gspc7_i   = 6

wide_a = np.array(df1)
x_a    = wide_a[:,gspc4_i: ]
y_a    = wide_a[:,pctlead_i]

# Ref:
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

from sklearn import linear_model

lrmodel = linear_model.LogisticRegression()
lrmodel_plot_data_l = []

# I should build a prediction loop from pcount.
# Higher dofit means fewer models means faster loop:
dofit = 10
# I should have this number of days between training data and oos data:
train_oos_gap = dofit # train_oos_gap should <= dofit
# Larger train_oos_gap means less precision.
print('Busy...')
for oos_i in range(0,pcount):
  x_oos       = x_a[oos_i,:]
  train_start = oos_i+1+train_oos_gap
  train_end   = train_start + train_count
  x_train     = x_a[train_start:train_end]
  y_train     = y_a[train_start:train_end]
  yc_train    = y_train > np.mean(y_train)
  pdate       = wide_a[oos_i,cdate_i]
  if (oos_i % dofit == 0) or (oos_i == 0):
    # print('Busy with fit calculations: '+str(oos_i+1))
    lrmodel.fit(x_train, yc_train)
  aprediction = lrmodel.predict_proba(x_oos.astype(float))[0,1]
  pctlead     = wide_a[oos_i,pctlead_i]
  cp          = wide_a[oos_i,cp_i     ]
  lrmodel_plot_data_l.append( [pdate, cp, aprediction-0.5, pctlead] )

prdf1 = pd.DataFrame(lrmodel_plot_data_l  )
prdf1.columns = ['cdate','cp','prediction','actual']

# I should save my work
prdf1.to_csv('prdf1.csv', float_format='%4.3f', index=False)
print('I have saved predictions in prdf1.csv')

'bye'
