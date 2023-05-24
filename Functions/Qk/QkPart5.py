import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")
from Functions.Fuzzy.SubFuzzy import *

def qkPart5(maxRmax, minRMin, maxRmid, minRMid, maxRmin, minRMax, size):
    results = []
    for i in range(size):
        result = subFuzzy(maxRmin, maxRmid, maxRmax, minRMin, minRMid, minRMax)
        results.append(result)

    return results
