# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:33:00 2015

@author: dhong
"""
import os, shutil
import pandas as pd
import glob

# set path of source files
source = r'D:\Users\dhong\Documents\Zonar'
# set path for target file
target = r'D:\Users\dhong\Documents\Zonar\merged'

# loop through all folders in source folder and copy to target folder
for root, dirs, files in os.walk((os.path.normpath(source)), topdown=False):
    for name in files:
        if name.startswith('red1782-path'):
            print "Found"
            sourceFolder = os.path.join(root,name)
            shutil.copy2(sourceFolder, target)

# create empty dataframe to temporarily store file data
allData = pd.DataFrame()

# append data from source files into the allData dataframe
for f in glob.glob(r'D:\Users\dhong\Documents\Zonar\merged\*.csv'):
    df = pd.read_csv(f)
    allData = allData.append(df,ignore_index=True)

# write allData to csv file
allData.to_csv(os.path.join(target, "out.csv"), index=False)
