# Variáveis livres  + monlocal
def fora():
    a = 1
    def dentro():
        return a
    return dentro

def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final+=valor_a_concatenar
        return valor_final
    return interna
c = concatenar('a')
print(c('b'))
print(c('d'))
print(c('c'))
print(c('e'))