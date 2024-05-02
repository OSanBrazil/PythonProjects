# Programa para fazer comentários sobre a idade

def verifiqueidade():
    volta = True
    while (volta):
        print()
        idade = input('Quantos anos você tem? -> ')
        if (idade.isdigit()) == False:
            print('Digite apenas números, ok?')
            volta = True
        elif (int(idade) < 1 or int(idade) > 200):
            print('Desculpe, mas essa idade é inválida ou irreal!')
            volta = True
        else:
            volta = False
    return idade

def criaresposta(idadeint):
    if (idadeint < 6):
        mensagem = 'Nossa! Você deveria estar no jardim da infância! HUAHUA!!'
    elif (idadeint > 5 and idadeint < 18):
        mensagem = 'Você é uma pessoa muito nova. Será que este é mesmo o curso pra você?'
    elif (idadeint > 17 and idadeint < 50):
        mensagem = 'É, você tá na média. Acho que tem muitas oportunidades pela frente...'
    elif (idadeint > 49 and idadeint < 70):
        mensagem = 'Você deve estar um pouquinho cansado, mas se tiver força de vontade, acho que ainda aguenta, hehe.'
    elif (idadeint > 69 and idadeint < 100):
        mensagem = 'Nossa, você deve tá bem cansadinho, já. Mas o que vale é a disposição, né? Vai em frente.'
    elif (idadeint > 99 and idadeint < 120):
        mensagem = 'Impressionante! Como você chegou até aqui? Parabéns pela longevidade e garra!'
    elif (idadeint > 119):
        mensagem = 'Santa Gertrudes! Tem certeza de que você ainda está vivo?! HUAHUAHUA!!'
    return mensagem

def main():
    idadeinfo = verifiqueidade()
    mensagem = criaresposta(int(idadeinfo))
    print(mensagem)

conditional = True
while (conditional == True):
    main()

# Fim do Programa



