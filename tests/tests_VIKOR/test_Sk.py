import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")

from Functions.Sk import sk

def test_sk():
    assert sk([1,2,3,4,5,6,7,8,9]) == 45

def test_sk_neg():
    assert sk([1,2,3,4,5,6,7,8,9]) != 40