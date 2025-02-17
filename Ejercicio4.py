"""
Contar digitos
"""

def contar(n):
    longitud = len(str(n))
    if longitud == 1:
        return 1  
    else:
        contador = contar(n // 10)  
        return contador + 1  


print(contar(1234))