#FUNCOES
def mostraMensagem(msg, num):
    quantidadeTracos = len(msg+str(num)*2)
    print('-'*quantidadeTracos)
    print(msg, num)
    print('-'*quantidadeTracos)


#TABUADA
entradaUsuarioTabuada = int(input('Digite um número para ser calculada a tabuada: '))
mostraMensagem('Tabuada do', entradaUsuarioTabuada)

for i in range(1, 11):
    resultadoTabuada = entradaUsuarioTabuada*i
    print(entradaUsuarioTabuada, 'x', i, '=', resultadoTabuada)
