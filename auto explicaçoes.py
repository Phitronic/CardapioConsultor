#Funções básicas em python
#A ideia é apenas mapear pontos e comandos importantes deixando tudo registrado de como cada função funciona na prática
print("Imaginação moldando a programação")
#print serve para mostrar informações na tela
try:
#o try é usado para capturar erros que podem ocorrer no código
    Peso = int(input("qual seu peso?"))
    if Peso >= 50:
        print('tu ta enorme')     
    else:
        print('só os ossokjjjjjj')
except ValueError:
    print('Resposta errada, porfavor use um numero inteiro')
    # o except serve para voltar respostas em casos de erro