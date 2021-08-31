#FUNCOES
def mostramensagem(msg, num):
    quantidadeTracos = len(msg+str(num)*2)
    print('-'*quantidadeTracos)
    print(msg, num)
    print('-'*quantidadeTracos)

def tabuada(num):
    for i in range(1, 11):
        resultadoTabuada = num * i
        print(num, 'x', i, '=', resultadoTabuada)


#TABUADA
if __name__ == '__main__':
    entradaUsuarioTabuada = int(input('Digite um número para ser calculada a tabuada: '))

    mostramensagem('Tabuada do', entradaUsuarioTabuada)
    tabuada(entradaUsuarioTabuada)