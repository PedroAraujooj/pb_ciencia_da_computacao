import multiprocessing
from multiprocessing import Pool
import sys
import random
import time
import matplotlib.pyplot as plt

def calcular_troco(val, moedas):
    resul = {"1":0, "0.5":0, "0.25":0, "0.10":0, "0.05":0, "0.01":0}
    return calcular_troco_aux(val,moedas, resul)
def calcular_troco_aux(val, moedas, resul):
    if val == 0:
        return resul
    total = (val//1)
    if total <= moedas["1"] and moedas["1"] != 0 and total != 0:
        resul["1"] += (val//1)
        resto = val - (val//1)
        moedas["1"] -= (val//1)
        return calcular_troco_aux(resto, moedas, resul)
    elif total > moedas["1"]:
        resul["1"] += moedas["1"]
        val -= moedas["1"]*1
        moedas["1"] = 0

    total = (val//0.5)
    if(total <= moedas["0.5"] and moedas["0.5"] != 0 and total != 0):
        resul["0.5"] += total
        resto = val - total*0.5
        moedas["0.5"] -= total
        return calcular_troco_aux(resto, moedas, resul)
    elif total > moedas["0.5"]:
        resul["0.5"] += moedas["0.5"]
        val -= moedas["0.5"]*0.5
        moedas["0.5"] = 0

    total = (val//0.25)
    if(total <= moedas["0.25"] and moedas["0.25"] != 0 and total != 0):
        resul["0.25"] += total
        resto = val - total*0.25
        moedas["0.25"] -= total
        return calcular_troco_aux(resto, moedas, resul)
    elif total > moedas["0.25"]:
        resul["0.25"] += moedas["0.25"]
        val -= moedas["0.25"]*0.25
        moedas["0.25"] = 0

    total = (val//0.10)
    if(total <= moedas["0.10"] and moedas["0.10"] != 0 and total != 0):
        resul["0.10"] += total
        resto = val - total*0.10
        moedas["0.10"] -= total
        return calcular_troco_aux(resto, moedas, resul)
    elif total > moedas["0.10"]:
        resul["0.10"] += moedas["0.10"]
        val -= moedas["0.10"]*0.10
        moedas["0.10"] = 0

    total = (val//0.05)
    if(total <= moedas["0.05"] and moedas["0.05"] != 0 and total != 0):
        resul["0.05"] += total
        resto = val - total*0.05
        moedas["0.05"] -= total
        return calcular_troco_aux(resto, moedas, resul)
    elif total > moedas["0.05"]:
        resul["0.05"] += moedas["0.05"]
        val -= moedas["0.05"]*0.05
        moedas["0.05"] = 0

    total = (val//0.01)
    if(total <= moedas["0.01"] and moedas["0.01"] != 0 and total != 0):
        resul["0.01"] += total
        resto = val - total*0.01
        moedas["0.01"] -= total
        return calcular_troco_aux(resto, moedas, resul)
    else:
        resul["0.01"] += moedas["0.01"]
        val -= moedas["0.01"]*0.01
        moedas["0.01"] = 0

    return resul

if __name__ == '__main__':
    moedas = {"1":4, "0.5":1, "0.25":2, "0.10":10, "0.05":8, "0.01":1}
    print(calcular_troco(5.51, moedas))