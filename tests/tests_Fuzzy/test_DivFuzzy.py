import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")

from Functions.Fuzzy.DivFuzzy import divFuzzy

def test_div_fuzzy():
    assert divFuzzy(6,6,6,2,2,2) == (3,3,3)

def test_div_fuzzy_neg():
    assert divFuzzy(6,6,6,2,2,2) != (1,1,1)