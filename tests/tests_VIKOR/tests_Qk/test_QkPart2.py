import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")

from Functions.Qk.QkPart2 import qkPart2

def test_qkPart2():
    assert qkPart2(0.59, 0.43, 0.7, 0.26, 0.83, 0.18, 6) != [(0.1, 0.2, 0.3), (0.4, 0.5, 0.6), (0.7, 0.8, 0.9), (0.8, 0.7, 0.6), (0.5, 0.4, 0.3), (0.2, 0.1, 0.2)]