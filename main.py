import numpy as np
import pandas as pd
import json
import sys
import requests
sys.path.append("C:/Users/ACER/Desktop/Pasta AV/Inatel/Fetin-2023-Backend")
from Functions.SkPart1 import *
from Functions.Sk import *
from Functions.Rk import *
from Functions.Qk.QkFinal import *
from Functions.Fuzzy.FuzzyToNormal import *


test = open('test.json')

data = json.load(test)


nCriterios = len(data["Criteria"])
nAlternatives = len(data["Criteria"][0]["Alternatives"])
v = 0.5


#Trabalhando com a função Sk Parte 1
retSkPart1 = []
for i in range(nCriterios):
    grades = []
    for j in range(nAlternatives):
        grade = data["Criteria"][i]["Alternatives"][j]["Grade"]
        smaller = grade - (0.1 * grade)
        medium = grade
        bigger = grade + (0.1 * grade)

        if smaller < 0:
            smaller = 0

        if bigger > 10:
            bigger = 10

        grades.append(smaller)
        grades.append(medium)
        grades.append(bigger)
    print(grades)
    weights = data["Criteria"][i]["Weight"]
    weights = 0.1 * weights
    ret = skPart1(grades, weights)
    retSkPart1.append(ret)
retSkPart1 = np.array(retSkPart1)



#Trabalhando com a função Sk
retSk = []
for i in range(retSkPart1.shape[1]):
    skGrades = []
    for j in range(retSkPart1.shape[0]):
        skGrade = retSkPart1[j][i]
        skGrades.append(skGrade)
    ret = round(sk(skGrades),7)
    retSk.append(ret)


#Trabalhando com a função Rk
retRk = []
for i in range(retSkPart1.shape[1]):
    rkGrades = []
    for j in range(retSkPart1.shape[0]):
        rkGrade = retSkPart1[j][i]
        rkGrades.append(rkGrade)
    ret = round(rk(rkGrades),7)
    retRk.append(ret)


#Trabalhando com a função Qk
notasQk = qkFinal(v, retSk, retRk)

#Convertendo de fuzzy para normal
result = fuzzyToNormal(notasQk)
sorted_result = np.sort(result)

alternatives = []
for i in range(len(result)):
    for j in range(len(sorted_result)):
        if result[j] == sorted_result[i]:
            alternative = data["Criteria"][0]["Alternatives"][j]["Name"]
            alternatives.append(alternative)

print(alternatives)
print(sorted_result)

ranking = {"ranking":[]}

for i in range(len(alternatives)):
    ranking["ranking"].append(
        {
            "Alternativa": alternatives[i],
            "Nota": sorted_result[i]
        }
    )

with open("Ranking.json", "w") as arquivo:     
    json.dump(ranking, arquivo, indent=4)



#Interação com o firebase
link = "https://fortis-criteris-default-rtdb.firebaseio.com/"

# Salvando entrada (POST)
dados = data
requisicao = requests.post(f'{link}/Data/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)


# Salvando saída (POST)
dados = ranking
requisicao = requests.post(f'{link}/Results/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)









