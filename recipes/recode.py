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

'Recode with floats'
df2 = pd.DataFrame({
    'A' : [1,2,3,4,5]  
})

df2['B'] = df2['A'].astype(float).replace([1, 2, 3, 4, 5], [1, 0.85, 0.70, 0.55, 0.40])

df2['C'] = df2['A'].map(dict(zip([1, 2, 3, 4, 5], [1, 0.85, 0.70, 0.55, 0.40])))

# Print DataFrame
print df2

# Print Column Attributes
print df2.dtypes