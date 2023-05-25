#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Busqueda import Estados_finitos as EF
# =============================================================================
# Apertura corpus 
# =============================================================================
with open("Datos/EH_string.txt","r", encoding= "UTF-8") as t:
    texto = t.read()
    t.close()
# =============================================================================
# Nominalizaciones
# =============================================================================
el = EF.el(texto) #Nominalizaciones con el
el = [oracion for lista in el for oracion in lista] #filtrado

n = EF.n(texto) #Nominalizaciones con n
n = [oracion for lista in n for oracion in lista] 
#es muy dificil filtrar por nominalizaciones con ñi, es necesario encontrar una forma para encontrar los verbos

# =============================================================================
# Construcciones seriales
# =============================================================================
pepi = EF.pepi(texto)
pepi = [oracion for lista in pepi for oracion in lista]

kupa = EF.kupa(texto)
kupa = [oracion for lista in kupa for oracion in lista]
#estas dos construcciones seriales son relativamente faciles de encontrar debido a que no aparecen por si solas, o bien su significado cambia cuando esto pasa

kim = EF.kim(texto)
kim = [oracion for lista in kim for oracion in lista]
#Es dificil separar el kim, presenta un desafio en si mismo