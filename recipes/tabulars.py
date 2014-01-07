#!/usr/bin/env python
# encoding=utf8

"""

SYNOPSIS

DESCRIPTION

EXAMPLES

AUTHOR

LICENSE

VERSION  

"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'split_1':[1,2,2,2,1,2,2,2,1,1],
    'split_2':[3,3,3,4,4,4,4,3,3,3],
    'var_1':[1,2,4,3,2,4,2,2,1,2],
    'var_2':[4,2,2,2,1,5,4,3,4,3],
})

grp = df.groupby(['split_1','split_2'])

grp.agg([np.mean, np.median, np.max, np.min, np.size]).stack(0)

