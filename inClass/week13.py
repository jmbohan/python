from numpy import e
import pandas as pd
import math


def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d


one = {'a':23, 'b':34, 'c':56, 'd':767, 'e':789, 'f':00}
two = {'a':56, 'b':67, 'c':34, 'd':65, 'e':78, 'f':99}
ser_one = pd.Series(data=one, index=['a','b','c','d','e','f'])
ser_two = pd.Series(data=two, index=['a','b','c','d','e','f'])

print(CohenEffectSize(ser_one,ser_two)) 