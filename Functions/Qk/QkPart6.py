import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")
from Functions.Fuzzy.DivFuzzy import *

def qkPart6(part4, part5):
    results = []
    for i in range(len(part4)):
        result = divFuzzy(part4[i][0], part4[i][1], part4[i][2], part5[i][0], part5[i][1], part5[i][2])
        results.append(result)

    return results