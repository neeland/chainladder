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
triangle.index.head() 

# example of filtering
triangle[(triangle['GRNAME']=="Aegis Grp")&(triangle['LOB']=="ppauto")]['IncurLoss']

print("end")