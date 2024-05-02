# This is a comment
def pergunte(mensagem, retentativas=4, lembrete='por favor, tente novamente'):
    while True:
        resposta = input(mensagem)
        if resposta in {'s','sim'}:
            return True
        if resposta in {'n','não','nao'}:
            return False
        retentativas = retentativas -1
        if retentativas <0:
            raise ValueError('Resposta do usuário inválida')
        print (lembrete)
for s in range(99):
    print (s,end='')
    print('')
print ('RESPONDA:')

pergunte('Você entendeu?')
pergunte('Está pronto agora?')

