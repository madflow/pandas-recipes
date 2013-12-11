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

'Assign some random values'
df = pd.DataFrame({ 
    'A' : np.random.randint(5, size=10),
    'B' : np.random.randint(5, size=10),
})


'Recode into column C with some operations'
df['C'] = 0.0

df['C'] = (df['A'] + df['B']) * 0.25

# Print DataFrame
print df

# Print Column Attributes
print df.dtypes

