import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")

from Functions.Qk.QkPart4 import qkPart4

def test_qkPart4():
    assert qkPart4([0.3, 0.2, 0.4, 0.4, 0.3111111, 0.3], [0.2666667, 0.1666667, 0.3555556, 0.4, 0.2222222, 0.2666667], [0.2, 0.1333333, 0.2666667, 0.3555556, 0.1777778, 0.2333333], 0.2, 0.17, 0.13) != [(0.0, 0.1, 0.2), (-0.3, -0.4, 0.5), (0.6, 0.7, 0.8), (0.9, 0.8, 0.7), (-0.6, 0.5, 0.4), (0.3, 0.2, 0.1)]