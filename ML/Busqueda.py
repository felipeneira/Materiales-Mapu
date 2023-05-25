import re

# =============================================================================
# Iniciar clase
# =============================================================================
class Estados_finitos:
    def __init__(self):
        pass
# =============================================================================
# pepi
# =============================================================================
    def pepi(x):
        posibilidadespepi = ["pepi"]
        pepi = [re.findall(r"\s+"+str(item)+"+\s?[a-z]+\s+", x) for item in posibilidadespepi]
        return(pepi)
# =============================================================================
# kupa
# =============================================================================
    def kupa(x):    
        posibilidadeskupa = ["kü","qui","ki","ku", "cu", "que", "c", "cù"]
        kupa = [re.findall(r"\s+"+str(item)+"pa+\s?[a-z]{6,20}\s+", x) for item in posibilidadeskupa]
        for item in kupa:
            print(item)
        return(kupa)
# =============================================================================
# Apariciones de kim
# =============================================================================
    def kim(x):
        posibilidadeskim = ["kim","quim"]
        kim = [re.findall(r"\s+"+str(item)+"+[^el][^che]\s?[a-z]+\s", x) for item in posibilidadeskim]
        return(kim)
# =============================================================================
# nominalizaciones con el
# =============================================================================
    def el(x):
        posibilidadesel = ["ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"]
        el = [re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l]e?l\s", x) for item in posibilidadesel]
        return(el)
# =============================================================================
# nominalizaciones con n
# =============================================================================
    def n(x):
        posibilidades = ["ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"]
        n = [re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l][a-zü]+?n\s", x) for item in posibilidades]
        return(n)
