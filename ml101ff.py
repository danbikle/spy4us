# ~ann/spy4us/ml101ff.py

# This script should generate predictions from:
# ftrGSPC2.csv
# $TRAIN_YRS
# $YRS
# prdf1.csv

# Demo:
# cd /tmp/spy4us/
# python ~ann/spy4us/ml101.py   4
# python ~ann/spy4us/ml101ff.py 4 1

import pdb
import pandas as pd
import numpy  as np
import sys

#  len(sys.argv) should == 3
if len(sys.argv) < 3:
  print('Demo:')
  print('cd /tmp/spy4us/')
  print('python ~ann/spy4us/ml101ff.py 4 1')
  sys.exit()

train_yrs = int(sys.argv[1])
yrs       = int(sys.argv[2])
# I should learn from this many observations:
train_count = 252 * train_yrs
# I should calculate  this many predictions:
pcount      = 252 * yrs

df1 = pd.read_csv('ftrGSPC2.csv')
# The data I want to feed-forward should have been created by
# ml101.py and placed in this file:
df3 = pd.read_csv('prdf1.csv')

# I should match rows from df1 with df3 rows.
# So I build df5 from df1 and force
# len(df5) == len(df3)
# This is a row operation.
# DF is a poor row operator so I convert
# df1 to array,
# operate on its rows,
# then convert back to DF:

df5 = pd.DataFrame(np.array(df1)[:len(df3)])
df5.columns = df1.columns

# Now I can copy columns from df3 to df5.

# I should transform prediction in df3 into a feature in df5.

df5['ip'] = df3['prediction']

# I should build a column named presult.
prediction_a = df3['prediction'].values
actual_a     = df3['actual'].values
presult_a    = np.sign(prediction_a) * actual_a

# I should make most recent presult_a value a feature in df5
presult_l = [elm for elm in presult_a] + [0.0]
df5['presult'] = presult_l[1:]

# I should calculate presult2_l.
# The idea is to sum the 3 most recent presults:

presult2_l = []
rowc = 1
for elm in presult_l[1:-2]:
  presult2_l.append(presult_l[rowc+0]+presult_l[rowc+1]+presult_l[rowc+2])
  rowc +=1

# set len(presult2_l) == len(df5)
presult2_l.append(0.0)
presult2_l.append(0.0)

# I should make it a feature:
df5['p2'] = presult2_l

# How many observations have I?
obs_count = len(df5)
print('I have this many observations: '+str(obs_count))

if pcount + train_count > obs_count:
  print('I dont have enough observations.')
  print('You want too many predictions.')
  print('You need to lower YRS and-or TRAIN_YRS.')
  sys.exit()
  
# I should get some training data from df5.
# I should put it in NumPy Arrays.

# I should declare some integers to help me navigate the Arrays.
# The layout and names of the columns are specified by joinem.sql:

cdate_i   = 0
cp_i      = 1
pctlead_i = 2
gspc4_i   = 3
gspc5_i   = 4
gspc6_i   = 5
gspc7_i   = 6
ip_i      = 7
presult_i = 8
p2_i      = 9

wide_a = np.array(df5)
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
prdf1.to_csv('ff1.csv', float_format='%4.3f', index=False)
print('I have saved predictions in ff1.csv')

'bye'
