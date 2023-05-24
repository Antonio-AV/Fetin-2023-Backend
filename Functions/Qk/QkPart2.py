import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")
from Functions.Fuzzy.SubFuzzy import *

def qkPart2(maxSmax, minSMin, maxSmid, minSMid, maxSmin, minSMax, size):
    results = []
    for i in range(size):
        result = subFuzzy(maxSmin, maxSmid, maxSmax, minSMin, minSMid, minSMax)
        results.append(result)

    return results
