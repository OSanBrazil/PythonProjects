# Imprime uma sequência de Números a partir de valores escolhidos, incrementando ou decrementando o valor definido
def Apresenta():
    print()
    print('ESTE PROGRAMA IMPRIME UMA SEQUÊNCIA DE NÚMEROS A PARTIR DE VALORES ESCOLHIDOS, INCREMENTANDO OU DECREMENTANDO O VALOR DEFINIDO PELO USUÁRIO')
    print()
def RecebeEntrada():
    inicio = input('Digite o número inicial: ')
    fim = input('Digite o número final: ')
    passo = input('Digite em quantos passos: ')
    return inicio, fim, passo
def ImprimeSequencia(inicio,fim,passo):
    for x in range (inicio, fim + passo, passo):
        print (str(x),end='')
        if not (x == fim):
            print (', ',end='')

def VerificaErros(inicio,fim,passo):
    Erro = False
    MsgErro = ''
    if not (inicio.isdigit() or fim.isdigit() or passo.isdigit()):
        Erro = True
        MsgErro = 'Digite apenas números!'
    try:
        inicio = int(inicio)
        fim = int(fim)
        passo = int(passo)
    except:
        Erro = True
        MsgErro = 'Digite valores válidos!'
    if Erro == False and ((inicio == fim) or passo <= 0):
        Erro = True
        MsgErro = 'O início não pode ser igual ao final nem o passo igual ou menor que zero!'

    if Erro == False and ((fim - inicio) % passo != 0):
        Erro = True
        MsgErro = 'A faixa entre ' + str(inicio) + ' e ' + str(fim) + ' precisa ser divisível por ' + str(passo)

    if Erro == False and ((fim - inicio) / passo > 299 or (fim - inicio) / passo < -299):
        Erro = True
        MsgErro = 'Uma sequência com mais de 300 números, infelizmente não será permitida.'

    return Erro,MsgErro,inicio,fim,passo


while True:
    Apresenta()
    inicio, fim, passo = RecebeEntrada()
    Erro,MsgErro,i,f,p = VerificaErros(inicio,fim,passo)
    if Erro == False:
        if i > f:
            p = - p
        print()
        ImprimeSequencia(i, f, p)
        print()
    else:
        print()
        print('ERRO!!')
        print(MsgErro)
        print()
