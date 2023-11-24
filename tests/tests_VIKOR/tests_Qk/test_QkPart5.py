import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")

from Functions.Qk.QkPart5 import qkPart5

def test_qkPart5():
    assert qkPart5(0.36, 0.2, 0.4, 0.17, 0.4, 0.13, 6) != [(0.1, 0.2, 0.3), (0.4, 0.5, 0.6), (0.7, 0.8, 0.9), (0.8, 0.7, 0.6), (0.5, 0.4, 0.3), (0.2, 0.1, 0.2)]