def subFuzzy(f1Min, f1Mid, f1Max, f2Min, f2Mid, f2Max):
    
    resultMin = f1Max - f2Min
    resultMid = f1Mid - f2Mid
    resultMax = f1Min - f2Max

    return resultMin, resultMid, resultMax


