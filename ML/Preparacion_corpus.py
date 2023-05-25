from Limpieza import Limpieza
import re
import glob
# import pandas as pd
# =============================================================================
# Apertura
# =============================================================================
lista_files = glob.glob('Textos/entrevistas_hasler/*.txt') #glob para abrir todo al mismo tiempo
corpus = {file[46:-4]: open(file,
                            'r',
                            encoding="utf-8").read() for file in lista_files} #extraer nombres
del lista_files
corpus = ' '.join(item for item in corpus.values()) #juntamos en un string
corpus = [oracion for oracion in corpus.split('\n') if len(oracion)>0] # separamos por linea
# =============================================================================
# Datos corpus entrevistas Felipe
# =============================================================================
texto = [oracion for oracion in corpus if oracion.startswith('\\tx ')] #extraemos el texto en mapudungun
texto = [oracion.replace('\\tx ', '').strip() for oracion in texto] #eliminamos el simbolo
texto = [Limpieza.remover_simbolos(oracion) for oracion in texto] #eliminamos simbolos extraños
texto = [oracion.split() for oracion in texto] #separamos las palabras por espacios
palabras = [elemento for lista in texto for elemento in lista] #contamos las palabras en total
print('Palabras totales')
print(len(palabras)) 
del texto
print('Tokens')
tokens = set(palabras) #cantidad de tokens sin filtrar
print(len(tokens))
contador = {palabra: palabras.count(palabra) for palabra in palabras} #contamos las ocurrencias de palabras
# =============================================================================
# Glosas
# =============================================================================
corpus = [oracion for oracion in corpus if oracion.startswith('\\mb ')]
corpus = [oracion.replace('\\mb ', '').strip() for oracion in corpus]
corpus = [Limpieza.remover_simbolos(oracion) for oracion in corpus]
corpus = [re.sub(" -", "-", oracion) for oracion in corpus]
corpus = [oracion.split() for oracion in corpus]
glosa = [elemento for lista in corpus for elemento in lista]
del corpus
# =============================================================================
# Planilla
# =============================================================================
# lexema = [item.replace('-','') for item in set(glosa)]
# planilla = pd.DataFrame(zip(lexema, set(glosa)), columns=["Palabra", "Glosa"])
# planilla.to_csv("Datos/datos_revisados.csv", sep=";")
# =============================================================================
# Borrar datos
# =============================================================================}
# del contador, glosa, lexema, palabras, planilla, tokens

# =============================================================================
# Extraccion corpus limpio
# =============================================================================
texto = ' '.join(palabras)
with open("Datos/EH_string.txt", mode='w', encoding='UTF-8') as t:
    t.write(texto)
