import numpy as np
import sys
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")
from Functions.Qk.QkPart1 import *
from Functions.Qk.QkPart2 import *
from Functions.Qk.QkPart3 import *
from Functions.Qk.QkPart4 import *
from Functions.Qk.QkPart5 import *
from Functions.Qk.QkPart6 import *

def qkFinal(v, sk, rk):

    sMin = []
    sMid = []
    sMax = []

    rMin = []
    rMid = []
    rMax = []

    i = 0 

    while i < int(len(sk)):
        sMin.append(sk[i])
        rMin.append(rk[i])

        sMid.append(sk[i+1])
        rMid.append(rk[i+1])

        sMax.append(sk[i+2])
        rMax.append(rk[i+2])

        i += 3

    minSMin = round(np.min(sMin),2)
    maxSmin = round(np.max(sMin),2)

    minSMid = round(np.min(sMid),2)
    maxSmid = round(np.max(sMid),2)

    minSMax = round(np.min(sMax),2)
    maxSmax = round(np.max(sMax),2)


    minRMin = round(np.min(rMin),2)
    maxRmin = round(np.max(rMin),2)

    minRMid = round(np.min(rMid),2)
    maxRmid = round(np.max(rMid),2)

    minRMax = round(np.min(rMax),2)
    maxRmax = round(np.max(rMax),2)



    retPart1 = qkPart1(sMin, sMid, sMax, minSMin, minSMid, minSMax)
    #print(retPart1)

    retPart2 = qkPart2(maxSmax, minSMin, maxSmid, minSMid, maxSmin, minSMax, len(sMin))
    #print(retPart2)

    retPart3 = qkPart3(retPart1, retPart2)
    #print(retPart3)

    finalS = []
    for i in range(len(retPart3)):
        for j in range(3):
            multV = retPart3[i][j] * v
            finalS.append(multV)

    #print(finalS)

    retPart4 = qkPart4(rMin, rMid, rMax, minRMin, minRMid, minRMax)
    #print(retPart4)

    retPart5 = qkPart5(maxRmax, minRMin, maxRmid, minRMid, maxRmin, minRMax, len(rMin))
    #print(retPart5)

    retPart6 = qkPart6(retPart4, retPart5)
    #print(retPart6)

    finalR = []
    for i in range(len(retPart6)):
        for j in range(3):
            multInvV = retPart6[i][j] * (1-v)
            finalR.append(round(multInvV,5))

    #print(finalR)

    Q = []

    for i in range(len(finalR)):
        result = finalS[i] + finalR[i]
        Q.append(result)

    return Q



    