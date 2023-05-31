from collections import namedtuple

EstadoCalculadora = namedtuple('Estado', ['acumulador', 'backup', 'memoria'])

def soma(estado, valor):
    novo_estado = EstadoCalculadora(
        acumulador = estado.acumulador + valor,
        backup = estado.acumulador, 
        memoria = estado.memoria)
    return novo_estado

def subtracao(estado, valor):
    novo_estado = EstadoCalculadora(
        acumulador = estado.acumulador - valor,
        backup = estado.acumulador, 
        memoria = estado.memoria)
    return novo_estado

def multiplicacao(estado, valor):
    novo_estado = EstadoCalculadora(
        acumulador = estado.acumulador * valor,
        backup = estado.acumulador, 
        memoria = estado.memoria)
    return novo_estado

def divisao(estado, valor):
    novo_estado = EstadoCalculadora(
        acumulador = estado.acumulador / valor,
        backup = estado.acumulador, 
        memoria = estado.memoria)
    return novo_estado
  
def memoriamr(estado):
    valor = input("Digite um número: ")
    if valor != 'mr':
        valor = float(valor)
    elif valor == 'mr':
        valor = estado.memoria
    return valor

def main():

    # estado = EstadoCalculadora(acumulador=0, backup=0, memoria=0)
    estado = EstadoCalculadora(0, 0, 0)

    print(f'Estado Inicial: Acumulador: {estado.acumulador}; Backup: {estado.backup}; Memória: {estado.memoria}')

    while True:
        
        operacao = str(input('Digite a operação desejada: ')).lower()

        if operacao == '=':
            estado = EstadoCalculadora(estado.acumulador, estado.acumulador, estado.memoria)
            break

        elif operacao == '+':
            valor = memoriamr(estado)
            estado = soma(estado, valor)
          
        elif operacao == '-':
            valor = memoriamr(estado)
            estado = subtracao(estado, valor)
          
        elif operacao == '*':
            valor = memoriamr(estado)
            estado = multiplicacao(estado, valor)
           
        elif operacao == '/':
            valor = memoriamr(estado)
            estado = divisao(estado, valor)

        elif operacao == '+/-':
            estado = EstadoCalculadora(estado.acumulador * -1, estado.backup, estado.memoria)
          
        elif operacao == '1/x':
            estado = EstadoCalculadora(1 / estado.acumulador, estado.backup, estado.memoria)
          
        elif operacao == 'x^2':
            estado = EstadoCalculadora(estado.acumulador ** 2, estado.backup, estado.memoria)
          
        elif operacao == 'r2x':
            estado = EstadoCalculadora(estado.acumulador ** 0.5 , estado.backup, estado.memoria)

        elif operacao == 'c':
            estado = EstadoCalculadora(estado.acumulador*0, estado.backup*0, estado.memoria)

        elif operacao == 'ce':
            estado = EstadoCalculadora(estado.backup, estado.backup, estado.memoria)

        elif operacao == 'mc':
            estado = EstadoCalculadora(estado.acumulador, estado.backup, estado.memoria*0)

        elif operacao == 'm+':
            estado = EstadoCalculadora(estado.acumulador, estado.backup, estado.memoria + estado.acumulador)
          
        elif operacao == 'm-':
            estado = EstadoCalculadora(estado.acumulador, estado.backup, estado.memoria - estado.acumulador)

        elif operacao == 'ms':
            estado = EstadoCalculadora(estado.acumulador, estado.backup, estado.acumulador)
          
        elif operacao == 'mr':
            estado = EstadoCalculadora(estado.memoria, estado.backup, estado.memoria)

        elif operacao != str:
            estado = EstadoCalculadora (float(operacao), estado.backup, estado.memoria)
          
        else:
            raise NotImplementedError("Outras operações não implementadas")

        print(f'Acumulador: {estado.acumulador}; Backup: {estado.backup}; Memória: {estado.memoria}')

    print(f'Resultado Final: Acumulador: {estado.acumulador}; Backup: {estado.backup}; Memória: {estado.memoria}')
        
if __name__=='__main__':
    main()
   
   
