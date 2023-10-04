import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, normalize

def Normalization(data, whichOne):
    if whichOne == 1:
        
        scaler = MinMaxScaler()
        normalized = scaler.fit_transform(data)
        
    elif whichOne == 2:
        
        scaler = StandardScaler()
        normalized = scaler.fit_transform(data)
        
    elif whichOne == 3:
        
        normalized = normalize(data, norm='l2', axis=0)
        
    elif whichOne == 4:
        
        normalized = data
    
    return normalized