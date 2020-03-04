#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:17:18 2020

@author: aetienne
"""

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

s

dates = pd.date_range('20130101', periods=30)

dates

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype= 'float32'),
                    'D': np.array([3] * 4, dtype= 'int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
df2

df2.dtypes

df2.head()
