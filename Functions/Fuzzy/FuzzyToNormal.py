import numpy as np

def fuzzyToNormal(notasQk):
    qMin = []
    qMid = []
    qMax = []

    i = 0 

    while i < int(len(notasQk)):
        qMin.append(notasQk[i])
        qMid.append(notasQk[i+1])
        qMax.append(notasQk[i+2])

        i += 3

    minQMin = round(np.min(qMin),2)
    maxQMin = round(np.max(qMin),2)

    minQMid = round(np.min(qMid),2)
    maxQMid = round(np.max(qMid),2)

    minQMax = round(np.min(qMax),2)
    maxQMax = round(np.max(qMax),2)


    qMinAvg = np.sum(qMin)/len(qMin)
    qMidAvg = np.sum(qMid)/len(qMid)
    qMaxAvg = np.sum(qMax)/len(qMax)

    part1 = ((maxQMin-minQMax)+2*(maxQMid-minQMid)+(maxQMax-minQMin))/2
    part2 = 2*(minQMax-maxQMin)

    if minQMax < minQMax:
        T = part1 + part2

    else:
        T = part1

    results = []
    for i in range(len(qMin)):
        result = (1/2)*(((qMin[i]-qMaxAvg)+2*(qMid[i]-qMidAvg)+(qMax[i]-qMinAvg))/(2*T)+1)
        results.append(result)

    return results 



