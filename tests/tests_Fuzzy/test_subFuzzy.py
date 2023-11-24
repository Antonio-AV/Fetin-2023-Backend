import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")

from Functions.Fuzzy.SubFuzzy import subFuzzy

def test_subFuzzy():
    assert subFuzzy(4,4,4,2,2,2) == (2,2,2)

def test_subFuzzy_neg():
    assert subFuzzy(4,4,4,2,2,2) != (1,1,1)