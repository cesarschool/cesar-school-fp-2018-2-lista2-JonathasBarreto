## QUESTÃO 4 ##
#
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 4")
    data = input("").lstrip(' ')
    a = data[:-6]
    b = data[-2:]
    c = data[-5:-3]
    ano = int(a)
    mes = int(c)
    dia = int(b)
    dia = dia + 1
    i = 0
    dm = 0
    if mes == 1:
        dm = 31
    elif mes == 2:
        dm = 26
    elif mes == 3:
        dm = 31
    elif mes == 4:
        dm = 30
    elif mes == 5:
        dm = 31
    elif mes == 6:
        dm = 30
    elif mes == 7:
        dm = 31
    elif mes == 8:
        dm = 31
    elif mes == 9:
        dm = 30
    elif mes == 10:
        dm = 31
    elif mes == 11:
        dm = 30
    elif mes == 12:
        dm = 31
    else:
        print("mês invalido")
    if dia > 0 and dia <= (dm + 1):
        if dia == (dm + 1):
            mes+=1
            dia = 1
            if mes == 13:
                ano+=1
                mes = 1
    else:
        print("dia do mês invalido")
    print(ano,"-",'{0:0>2}'.format(mes),"-",'{0:0>2}'.format(dia))

    
if __name__ == '__main__':
    main()
