# =============================================================================
# defs de limpieza
# =============================================================================
class Limpieza:
    def __init__(self):
        pass
    @staticmethod
    def remover_puntuacion(s): # input: string
        for c in '+\(\)\"\'\$\#\¿\?\/\&\,\.\*':
            s = s.replace(c, " ")
            s = s.replace('\t', ' ')
        return s
    @staticmethod
    def remover_numeros(k): # input: string
        numeros = [numero for numero in range(0,100)]
        for z in numeros:
            k = k.replace(str(z), " ")
            k = k.replace('pag', '')
        return k
    @staticmethod
    def remover_simbolos(s): # input: string
        s = s.replace('\n', ' ')
        s = s.replace('\t', ' ')
        s = s.replace('[r]', ' ')
        s = s.replace('Â¶', ' ')
        s = s.replace('[0-9]', ' ')
        s = s.replace('P ', '')
        s = s.replace('R ', '')
        s = s.replace('\n', '')
        s = s.replace('Â¿', '')
        s = s.replace('â', '')
        s = s.replace('â¦', '')
        s = s.replace('<\*spa>', '')
        s = s.lower()
        s = Limpieza.remover_numeros(s)
        s = Limpieza.remover_puntuacion(s)
        s = ' '.join(s.split())
        return s

    