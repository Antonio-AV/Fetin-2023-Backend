import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")
from Functions.Fuzzy.SubFuzzy import *

def qkPart4(rMin, rMid, rMax, minRMin, minRMid, minRMax):
    results = []
    for i in range(len(rMin)):
        result = subFuzzy(rMin[i], rMid[i], rMax[i], minRMin, minRMid, minRMax)
        results.append(result)

    return results