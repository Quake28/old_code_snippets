# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv ('/content/Income Dataset (50k).csv')


dfn = df.fillna(0)


newdata = pd.get_dummies (dfn.workclass)


mergeddata = pd.concat ([dfn, newdata], axis= 'columns')


finaldata = mergeddata.drop (['workclass'], axis='columns')
