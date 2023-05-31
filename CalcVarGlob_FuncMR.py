def soma(valor):
    global acumulador
    global memoria
    global backup
    backup = acumulador
    acumulador = acumulador + valor
    
def subitracao(valor):
    global acumulador
    global memoria
    global backup
    backup = acumulador
    acumulador = acumulador - valor
    
def multiplicacao(valor):
    global acumulador
    global memoria
    global backup
    backup = acumulador
    acumulador = acumulador * valor 
    
def divisao(valor):
    global acumulador
    global memoria
    global backup
    backup = acumulador
    acumulador = acumulador / valor 
    
def c(valor):
    global acumulador
    global memoria
    global backup
    backup = 0
    acumulador = 0  
    
def ce(valor):
    global acumulador
    global memoria
    global backup
    acumulador = backup
    
def ms(valor):
    global acumulador
    global memoria
    global backup
    memoria = acumulador
    
def mr(valor):
    global acumulador
    global memoria
    global backup
    acumulador = memoria
    
def mc(valor):
    global acumulador
    global memoria
    global backup
    memoria = 0
    
def mmais(valor):
    global acumulador
    global memoria
    global backup
    memoria = acumulador + memoria
    
def mmenos(valor):
    global acumulador
    global memoria
    global backup
    memoria = memoria - acumulador
    
def calculomemoria(valor):
    global acumulador
    global memoria
    global backup
    acumulador = acumulador + memoria
    
def memoriaMR():
    valor = input("Digite um número: ")
            if valor != 'mr':
                valor = float(valor)
            if valor == 'mr':
               valor = memoria
def main():
   
    global acumulador
    global memoria
    global backup
    acumulador = 0
    memoria = 0
    backup = 0
 
    print(f'Estado Inicial: Acumulador: {acumulador}; Backup: {backup}; Memória: {memoria}')

    while True:
        
        operacao = (input('Digite a operação desejada: ')).lower()
       
        if operacao == '=':
            backup = acumulador
            break
            
        elif operacao == '+':
            valor = memoriaMR()
            soma(valor)
            
        elif operacao == '-':
          valor = memoriaMR()
            subitracao(valor) 
            
        elif operacao == '*':
            valor = input("Digite um número: ")
           valor = memoriaMR()
            multiplicacao(valor)  
            
        elif operacao == '/':
          valor = memoriaMR()
            divisao(valor)
            
        elif operacao == 'ce':
            ce(valor)
            
        elif operacao =='c':
            c(valor)
            
        elif operacao == 'ms':
            ms(valor)
            
        elif operacao == 'mr':
            mr(valor)
            
        elif operacao == 'mc':
            mc(valor)
            
        elif operacao == 'm+':
            mmais(valor)
            
        elif operacao == 'm-':
            mmenos(valor)
            
        elif operacao == '+/-':
            acumulador = acumulador - acumulador*2
            
        elif operacao == '1/x':
            acumulador = 1 / acumulador
            
        elif operacao == 'x^2':
            acumulador **= 2
            
        elif operacao == 'r2x':
            acumulador **= 0.5
            
        elif  operacao == int:
             valor = float(input("Digite um número: "))   
             divisao(valor)
              
        elif operacao != str:
            acumulador = float(operacao)     
            
        else:
            raise NotImplementedError("Outras operações não implementadas")

        print(f'Acumulador: {acumulador}; Backup: {backup}; Memória: {memoria}')

    print(f'Resultado Final: Acumulador: {acumulador}; Backup: {backup}; Memória: {memoria}')

if __name__=='__main__':
    main()
