import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")
from Functions.Fuzzy.DivFuzzy import *

def qkPart3(part1, part2):
    results = []
    for i in range(len(part1)):
        result = divFuzzy(part1[i][0], part1[i][1], part1[i][2], part2[i][0], part2[i][1], part2[i][2])
        results.append(result)

    return results