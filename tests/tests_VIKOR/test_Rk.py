import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")

from Functions.Rk import rk

def test_rk():
    assert rk([1,2,3,4,5,6,7,8,9]) == 9

def test_rk_neg():
    assert rk([1,2,3,4,5,6,7,8,9]) != 15