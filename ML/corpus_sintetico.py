#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:30:43 2022

@author: felipe
"""
# =============================================================================
# Librerias
# =============================================================================
import pandas as pd
import re
# =============================================================================
# preparar morfessor
# =============================================================================
#import morfessor
#io = morfessor.MorfessorIO(encoding="utf-8",construction_separator=' ',comment_start= '#', compound_separator="\\s", atom_separator=None, lowercase= False)
#cost = morfessor.baseline.AnnotatedCorpusEncoding("utf-8")
# ===5==========================================================================
# defs limpieza
# =============================================================================
def remover_puntuacion(s):
    puntuacion = """!"#$%&\'()*+,.:;<=>?@[\\]^_`{|}~"""
    for c in puntuacion:
        s=s.replace(c,"")
        s=s.replace('\t','')
    return s
def remover_numeros(k): 
    numeros= []
    for numero in list(range(100)):
        numeros+= [numero]
    numeros = str(numeros)
    for z in numeros:
        k=k.replace(z," ")
        k=k.replace('pag','')
    return k
# =============================================================================
# 
# =============================================================================
df = pd.read_csv("Morfessor/NO_BORRAR.csv", sep=";")
df = df[["palabra","segmentacion"]]
palabras = df["palabra"].to_list()
palabras = [remover_puntuacion(str(item)) for item in palabras]
palabras = [item.replace('-','') for item in palabras]
segmentacion = df["segmentacion"].to_list()
segmentacion = [remover_puntuacion(str(item)) for item in segmentacion]
segmentacion = [item.replace('-',' ') for item in segmentacion]
AF1 = list(zip(palabras, segmentacion))

# =============================================================================
del palabras, segmentacion
# =============================================================================
# Corpus sintético
# =============================================================================
# =============================================================================
# Defs de cambios
# =============================================================================
def cambiar_terminaciones(X):#X corresponde a una lista
    nuevos = []
    terminaciones = ["n","ün","ymi","ymün","nge","y","ymü","pe","le","li","lmi","liyiñ","yu","liyu","lu", "el"]
    for terminacion in terminaciones:
        for item in X:
            nuevo = item[1][:-1] + [terminacion]
            nuevos.append(nuevo)
    return nuevos

def cambiar_directas(X):#X corresponde a una lista con dos objetos: cada segmentacion y el verbo
    directas = ["ñ",
                "yiñ",
                "yu",
                "mi",
                "mu",
                "ymün",
                "y",
                "nge",
                "pe",
                "le",
                "li",
                "lmi",
                "liyiñ",
                "liyu",
                "el"]
    nuevos = []
    for directa in directas:
        for item in X:
            nuevo= item[1][:-1]+[directa]
            nuevos.append(nuevo)
    return nuevos

def cambiar_inversas(X):#X corresponde a una lista con dos objetos: cada segmentacion y el verbo
    nuevos = []
    inversas = [["e","n","ew"],
                ["e","y","ew"],
                ["e","ym","ew"],
                ["e","yu","mew"],
                ["e","ymu","mew"],
                ["e","iñ","mew"],
                ["e","mün","mew"],
                ["e","t","ew"]]
    for inversa in inversas:
        for item in X:
            if item[1][-1] == "ew":
                nuevo= item[1][:-3] + [sufijo for sufijo in inversa]
                nuevos.append(nuevo)
            elif item[1][-1] == "mew":
                nuevo= item[1][:-3] + [sufijo for sufijo in inversa]
                nuevos.append(nuevo)
    return nuevos

def cambiar_directas2(X):#X corresponde a una lista con dos objetos: cada segmentacion y el verbo
    directas = ["ñ",
                "yiñ",
                "yu",
                "mi",
                "mu",
                "ymün",
                "y",
                "nge",
                "pe",
                "le",
                "li",
                "lmi",
                "liyiñ",
                "liyu",
                "el"]
    nuevos = []
    for directa in directas:
        for item in X:
            nuevo= item[:-1]+[directa]
            nuevos.append(nuevo)
    return nuevos

def cambiar_inversas2(X):#X corresponde a una lista con dos objetos: cada segmentacion y el verbo
    nuevos = []
    inversas = [["e","n","ew"],
                ["e","y","ew"],
                ["e","ym","ew"],
                ["e","yu","mew"],
                ["e","ymu","mew"],
                ["e","iñ","mew"],
                ["e","mün","mew"],
                ["e","t","ew"]]
    for inversa in inversas:
        for item in X:
            if item[-1] == "ew":
                nuevo= item[:-3] + [sufijo for sufijo in inversa]
                nuevos.append(nuevo)
            elif item[-1] == "mew":
                nuevo= item[:-3] + [sufijo for sufijo in inversa]
                nuevos.append(nuevo)
    return nuevos

def numero_morfemas(X):#X corresponde a un diccionario donde cada palabra es un key y su segmentacion el value
    mapu_construcciones = {"1": {k:v for k,v in AF2.items() if len(v) == 2},
                           "2":{k:v for k,v in AF2.items() if len(v) == 3},
                           "3":{k:v for k,v in AF2.items() if len(v) == 4},
                           "4":{k:v for k,v in AF2.items() if len(v) == 5}
                           }
    return mapu_construcciones


def crear_inversa(X):#X corresponde a una lista con dos objetos: cada segmentacion y el verbo
    nuevo = X[1][:-2]+ ["e"]+["n"]+["ew"]
    return nuevo
def crear_directa(X):#X corresponde a una lista con dos objetos: cada segmentacion y el verbo
    nuevo = X[1][:-3]+ ["fi"]+["ñ"]
    return nuevo
def invertir_AP(X):#X corresponde a una lista de listas
    nuevos=[]
    for item in X:
        if item[1][-2] == "fi":
            nuevo = crear_inversa(item)
            nuevos.append(nuevo)
        if item[1][-2] != "fi":
            if item[1][-1] == "ew":
                nuevo = crear_directa(item)
                nuevos.append(nuevo)
            if item[1][-1] == "mew":
                nuevo = crear_directa(item)
                nuevos.append(nuevo)
    return nuevos

# =============================================================================
# verbos sin -fi
# =============================================================================
AF2 = [[item[0],item[1].split(" ")] for item in AF1 if len(item[1]) != 1]
AF2 = [[item[0],item[1]] for item in AF2 if len(item[1]) != 1]
terminaciones = ["n","ün","ymi","ymün","nge","y","ymü","pe","le","li","lmi","liyiñ","yu","liyu","lu", "el"]
verbos = [[item[0],item[1]] for item in AF2 if item[1][-1] in terminaciones]
verbos = [[item[0],item[1]] for item in verbos if not re.search("fi[a-zA-Zñü]",item[0])]
verbos_negados = [[item[0],item[1]] for item in verbos if re.search("[^l]no[a-zA-Zñü]|[^l]la[a-zA-Zñü]|[^l]kil[a-zA-Zñü]",item[0])]
verbos = [[item[0],item[1]] for item in verbos if not re.search("[^l]no[a-zA-Zñü]|[^l]la[a-zA-Zñü]|[^l]kil[a-zA-Zñü]",item[0])]

verbos_segmentados = cambiar_terminaciones(list(verbos))
verbos_nuevos = [remover_puntuacion(str(item)).replace(" ","") for item in verbos_segmentados]
verbos_nuevos = dict(zip(verbos_nuevos,verbos_segmentados))
verbos_nuevos = {k:v for k,v in verbos_nuevos.items() if not re.search("[aeiouü]ün",k)}
corpus_sintetico = {k:v for k,v in verbos_nuevos.items() if not re.search("[bcdfghjklmnñpqrstvwxyz]n$",k)}


# =============================================================================
# verbos con -fi y -ew
# ============================================================================
AF3 = AF2 = [[item[0],item[1]] for item in AF2 if len(item[1]) > 2]
directas = [[item[0],item[1]] for item in AF3 if item[1][-2] == "fi"]
directas_invertidas = invertir_AP(directas)
inversas = [[item[0],item[1]] for item in AF3 if item[1][-1] == "ew"]
inversas_invertidas =invertir_AP(inversas)
del AF2, terminaciones, verbos, verbos_nuevos
directas = cambiar_directas(directas)
directas += cambiar_directas2(inversas_invertidas)
inversas = cambiar_inversas(inversas)
inversas += cambiar_inversas2(directas_invertidas)
transitivas = directas+inversas

verbos_nuevos = [remover_puntuacion(str(item)).replace(" ","") for item in transitivas]
corpus_sintetico.update(dict(zip(verbos_nuevos,transitivas)))
del AF3, directas, directas_invertidas, inversas
del inversas_invertidas, transitivas, verbos_negados, verbos_nuevos, verbos_segmentados

# =============================================================================
# AF final (descomentar solo para ingresar las palabras)
# =============================================================================

corpus_natural = pd.read_csv("Morfessor/NO_BORRAR.csv",sep = ";")
corpus_natural = corpus_natural[["palabra","segmentacion"]]
palabras_natural = corpus_natural["palabra"].to_list()
palabras_natural = [remover_puntuacion(str(item)) for item in palabras_natural]
palabras_natural = [item.replace('-','') for item in palabras_natural]
segmentacion_natural = corpus_natural["segmentacion"].to_list()
segmentacion_natural = [remover_puntuacion(str(item)) for item in segmentacion_natural]
segmentacion_natural = [item.replace('-',' ') for item in segmentacion_natural]
AF1 = dict(zip(palabras_natural, segmentacion_natural))

corpus_sintetico = pd.DataFrame(list(zip(list(corpus_sintetico.keys()),list(corpus_sintetico.values()))),columns=["palabra","segmentacion"])
corpus_sintetico = corpus_sintetico[["palabra","segmentacion"]]
palabras_sintetico = corpus_sintetico["palabra"].to_list()
palabras_sintetico = [remover_puntuacion(str(item)) for item in palabras_sintetico]
palabras_sintetico = [item.replace('-','') for item in palabras_sintetico]
segmentacion_sintetico = corpus_sintetico["segmentacion"].to_list()
segmentacion_sintetico = [remover_puntuacion(str(item)) for item in segmentacion_sintetico]
segmentacion_sintetico = [item.replace('-',' ') for item in segmentacion_sintetico]
AF2 = dict(zip(palabras_sintetico, segmentacion_sintetico))
AF1.update(AF2)

#with open(Morfessor/"AF2.txt", "w") as text_file:
#   for i,j in AF1.items():
#       text_file.write(i + " " + j + "\n")
# =============================================================================
# Sustantivos
# =============================================================================

# =============================================================================
# Adjetivos
# =============================================================================

# =============================================================================
# Adverbios
# =============================================================================
