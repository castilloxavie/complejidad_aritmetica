def morral(tamanho_morral, peso, valores, n):
    
    if n == 0 or tamanho_morral == 0:
        return 0
    
    if peso[n - 1] > tamanho_morral:
        return morral(tamanho_morral, peso, valores, n -1)
    
    return max(valores[n-1]+ morral(tamanho_morral - peso[n-1], peso, valores, n - 1),
               morral(tamanho_morral, peso,valores, n -1))


if __name__ == '__main__':
    valores = [20,50.48]
    peso = [20,50,30]
    tamanho_morral = 100
    n = len(valores)

    resultado = morral(tamanho_morral, peso, valores, n)
    print(resultado)