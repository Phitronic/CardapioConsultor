# agora vou fazer uma cálculadora de consultoria
# um teste para entender melhor o if, else e elif
import customtkinter as ctk
import pandas as pd
print("sua calculadora de consultoria")
# pode ser falta de experiencia, mas acho bem necessario utilizar o Try...
while True:
  try:
    Qual_servico = input ("qual produto você quer?")
    if Qual_servico == "1":
        print("Planilhas, custa R$100,00")
        proposta = input("quanto deseja pagar?")
        valor_numerico = int(proposta)
        if valor_numerico == 100:
          print("Produto planilhas pago com êxito")
        elif valor_numerico <= 99:
          print("Valor incompleto")
        else:
          print("Ultrapassou o valor")
#Essa é a estrutura do primeiro produto a ser selecionado, bem básico mas espero que rode kkkk    
    elif Qual_servico == "2":
        print("Automação Web, custa R$200,00")
        proposta = input ("quanto deseja pagar?")
        valor_numerico = int(proposta)
        if valor_numerico == 200:
            print("produto Automação web pago com êxito")
        elif valor_numerico <=199:
            print("Valor incompleto")
        else:
            print("Ultrapassou o valor")
#teste de break a seguir.
    elif Qual_servico == "0":
        print("encerrando o programa")
        break
#A estrutura do segundo produto, quase um Ctrl C + Ctrl V da outra, a próxima vou usar a mesma sequencia
    elif Qual_servico == "3":
        print("Limpeza de dados, custa R$50,00")
        proposta = input ("quanto deseja pagar?")
        valor_numerico = int(proposta)
        if valor_numerico == 50:
          print("produto limpeza de dados pago com êxito")
        elif valor_numerico <= 49:
          print("Valor imcompleto")
        else:
            print("Ultrapassou o valor")
    else: 
        print("Resposta incorreta, tentar novamente")
  except ValueError:
   print("eroooou")
        
#                       Abaixo um esboço que fiz antes sobre o que juntar na linha de código    
#    proposta = input("quanto deseja pagar?")
#    if proposta  == "100":
#    elif proposta == "200":
#        print("você concluiu o pagamento de AUTOMAÇÃO WEB")
#    elif proposta == "50":
#        print("você concluiu o pagamento de LIMPEZA DE DADOS")
#    else: print ("não temos produtos nesse valor, tente novamente") 
#except ValueError:
#        print("tente novamente")
    