## QUESTÃO 2 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 2")
    from math import sqrt
    a = input().upper()
    c = 0
    b = 0
    d = 0
    e = 0
    while a:
        direcao = a[:a.find(' ')]
        p = a[a.find(' ')+1:]
        passos = int(p)
        if direcao == 'CIMA':
            c = c + passos 
        if direcao == 'BAIXO':
            b = b + passos
        if direcao == 'ESQUERDA':
            e = e + passos
        if direcao == 'DIREITA':
            d = d + passos
        if c > b:
            X = c - b
        else:
            X = b - c
        if e > d:
            Y = e - d
        else:
            Y = d - e
        H = sqrt((Y*Y)+(X*X))
        a = input().upper()
    print(int(H))



    
if __name__ == '__main__':
    main()
