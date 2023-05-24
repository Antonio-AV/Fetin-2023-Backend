import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")
from Functions.Fuzzy.SubFuzzy import *

def qkPart1(sMin, sMid, sMax, minSMin, minSMid, minSMax):
    results = []
    for i in range(len(sMin)):
        result = subFuzzy(sMin[i], sMid[i], sMax[i], minSMin, minSMid, minSMax)
        results.append(result)

    return results