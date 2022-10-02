"""
https://notebook.community/jbogaardt/chainladder-python/docs/tutorials/triangle-tutorial
notes on exploring chainladder pypi package functionality for run-off triangles

authors: neelan.pather@gmail.com
"""

import pandas as pd
import numpy as np
import chainladder as cl

# index generally represents reserve groupings - in this example, lines of business and companies
triangle = cl.load_sample('clrd')
# Create a 'NetPaidLossRatio' column in triangle from the existing columns
triangle['NetPaidLossRatio'] = triangle['CumPaidLoss']/triangle['EarnedPremNet']

# What is the highest net paid loss ratio for any observation for origin 1997 Age 12
highest_net_paid_loss_ratio = triangle[triangle.origin=='1997'][triangle.development==12]['NetPaidLossRatio'].max()

# triangle.shape==(775, 7, 10, 10)==(len(triangle['GRNAME']), len(triangle.columns), len(triangle.origin), len(triangle.development)) 
# also, len(triangle['GRNAME']== len(triangle['LOB'])

# Subset the overall triangle to just include 'Alaska Nat Ins Co'
subset_triangle = triangle[triangle['GRNAME']=='Alaska Nat Ins Co']

# Use boolean indexing to create a triangle subset that includes all triangles for companies with names starting with 'B'
subset_triangle_boolean = triangle[triangle['GRNAME'].str[0]=='B']

# Which companies are in the top 5 net premium share for 1990?
top5 = triangle[triangle.origin=='1990']['EarnedPremNet'].latest_diagonal.groupby('GRNAME').sum().to_frame().sort_values(ascending=False)[:5]
#triangle[triangle.origin=='1990']['EarnedPremNet'].latest_diagonal.groupby('GRNAME').sum().to_frame().sort_values().iloc[-5:]


# TODO: ??? don't really get why you need the .sum() to use `to_frame()`
test = triangle[triangle.origin=='1990']['EarnedPremNet'].latest_diagonal.groupby('GRNAME') 
print("end")
