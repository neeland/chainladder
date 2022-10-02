"""
https://notebook.community/jbogaardt/chainladder-python/docs/tutorials/triangle-tutorial
notes on exploring chainladder pypi package functionality for run-off triangles

authors: neelan.pather@gmail.com
"""

import pandas as pd
import numpy as np
import chainladder as cl
#%matplotlib inline
print(cl.__version__)

# load sample triangle
# for working with > 1 triangle chainladder. Triangle acts like pd.DataFrame & each cell (row x col) is individual triangle. 
# structure manifests itself in four-dimensional space.
triangle = cl.load_sample('clrd')

# `index` generally represents reserve groupings
index_head = triangle.index.head()

# example of filtering
filter = triangle[(triangle['GRNAME']=="Aegis Grp")&(triangle['LOB']=="ppauto")].values[-1][0]
#print(triangle)

#triangles have .origin, .development and .valuation properties

#extracting latest accident period
latest_accident_period = triangle[triangle.origin==triangle.origin.max()]

particular_diagonals = triangle[(triangle.valuation>='1994')&(triangle.valuation<='1995')].sum()['CumPaidLoss']

# slice particular development periods to explore aspects of our data by development age. 
slice = triangle[triangle.development<=24].sum()['CumPaidLoss'].link_ratio #.plot()

#use built in plot method to plot slice
# is simply conversion to pd and using pd plot
plot = slice.plot()

#when Triangle object can be expressed as 2D structure (i.e. 2 of 4 axes w/ length==1)
# .to_frame method --> convert to pd.Data   Frame
query_2d = triangle.groupby('LOB').sum().latest_diagonal['CumPaidLoss']
print(query_2d.shape) # notice shape is (6, 1, 10, 1)

pd_query_2d = query_2d.to_frame().astype(int)

print("end")