import pandas as pd
from modules.assumptions_and_constants import assumptions

def unpack_assessed_value(val,r_nr):

    if r_nr == 'r':
        factor = assumptions().loc['Assessed Value Ratio (Residential)'].squeeze()
    else:
        factor = assumptions().loc['Assessed Value Ratio (Non Residential)'].squeeze()

    val['Market Value Per unit']=val['Market Value Per unit'].str.replace(',','', regex=True)
    val['Market Value Per unit']=val['Market Value Per unit'].str.replace('$','', regex=True).astype(float)
    val['Assessed Value Ratio']=factor
    val['Assessed Value Per unit']=val['Market Value Per unit']*val['Assessed Value Ratio']
    val.reset_index(drop=True, inplace=True)
    val = val

    return val

