import math
import numpy as np
import pandas as pd

def getStandardDeviations(data):
    max = np.max(data)
    min = np.min(data)
    std = np.std(data)
    mean = data.mean()
    range = max - min
    
    standardDeviations = []
    
    leftStd = math.floor((mean - min) / std)
    for i in np.arange(1, leftStd + 1):
        standardDeviations.append(mean - i * std)
    
    rightStd = math.floor((max - mean) / std)
    for i in np.arange(1, rightStd + 1):
        standardDeviations.append(mean + i * std)
    
    return standardDeviations