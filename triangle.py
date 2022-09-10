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
triangle = cl.load_sample('raa')


def print_triangle_propeties(triangle):
    """
    Returns properties of run-off triangle

    Args:
        triangle (chainladder.core.triangle.Triangle): run-off triangle
    """

    # link ration: multiplicative change in amounts from one development period to the next.
    print(triangle.link_ratio)

    # view and manipulate the latest_diagonal of the triangle   
    print(triangle.latest_diagonal)

    # latest diagonal certainly corresponds to valuation_date
    print(triangle.valuation_date)

    # triangle.is_cumulative: whether the data acumulates across the development periods or is incremental
    print('Is triangle cumulative?', triangle.is_cumulative)

    # triangle.is_ultimate: whether ultimate values are contained in the triangle
    print('Does triangle contain ultimate projections?', triangle.is_ultimate)

    # triangle.is_val_tri whether the development period is stated as a valuation data as opposed to an age
    print('Is this a valuation triangle?', triangle.is_val_tri)

    # triangle.is_full: whether the bottom half of the triangle has been completed
    print('Has the triangle been "squared"?', triangle.is_full)

    # ???
    print('Origin grain: ', triangle.origin_grain)

    # ???
    print('Development grain: ', triangle.development_grain)

