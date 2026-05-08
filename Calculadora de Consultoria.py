# agora vou fazer uma cálculadora de consultoria
# um teste para entender melhor o if, else e elif
import customtkinter as ctk
import pandas as pd
janela = ctk.CTk()
janela.title("Calculadora de consultoria")
janela.geometry("600x400")
print("sua calculadora de consultoria")

#trabalhando para adaptar o CTK pois não tenho experiencia nenhuma com isso

label_servico = ctk.CTkLabel(janela, text=(''' Trabalhamos com os seguintes produtos:
    1 - Planilhas = R$100,00
    2 - Automação web = R$200,00
    3 - Limpeza de dados = R$50,00
     '''), justify="left")
label_servico.pack(pady=(20, 5))
entrada_servico = ctk.CTkEntry(janela, placeholder_text="Ex: 1")
entrada_servico.pack(pady=5)

#Separando agora serviço e proposta pois estava muito enrolado esse código

label_proposta = ctk.CTkLabel(janela, text="Quanto deseja pagar?")
label_proposta.pack(pady=(10, 5))
entrada_proposta = ctk.CTkEntry(janela, placeholder_text="Ex: 100")
entrada_proposta.pack(pady=5)

#agora vou trabalhar a função antes de prosseguir

def processar_venda ():
    servico_texto = entrada_servico.get()
    proposta_texto = entrada_proposta.get()
    try:
       valor_numerico = int(proposta_texto) 
       if servico_texto == "1":
            print("Item selecionado: Planilhas (R$ 100,00)")
            if valor_numerico == 100:
                print(">>> Sucesso: Pago com êxito!")
            elif valor_numerico <= 99:
                print(">>> Erro: Valor incompleto.")
            else:
                print(">>> Aviso: Valor acima do preço.")   
#    elif Qual_servico == "2":
#       print("Automação Web, custa R$200,00")
#        proposta = input ("quanto deseja pagar?")
#    valor_numerico = int(proposta)
#    if valor_numerico == 200:
#            print("produto Automação web pago com êxito")
#    elif valor_numerico <=199:
#            print("Valor incompleto")
#    else:
#            print("Ultrapassou o valor")
#
#    elif Qual_servico == "0":
#    print("encerrando o programa")
#A estrutura do segundo produto, quase um Ctrl C + Ctrl V da outra, a próxima vou usar a mesma sequencia
#    elif Qual_servico == "3":
#    print("Limpeza de dados, custa R$50,00")
#        proposta = input ("quanto deseja pagar?")
#    valor_numerico = int(proposta)
#    if valor_numerico == 50:
#          print("produto limpeza de dados pago com êxito")
#    elif valor_numerico <= 49:
#          print("Valor imcompleto")
#    else:
#            print("Ultrapassou o valor")
#    else: 
#    print("Resposta incorreta, tentar novamente")
    except ValueError:
        print("eroooou")
botao_confirmar = ctk.CTkButton(janela, text="Verificar Pagamento", command=processar_venda)
botao_confirmar.pack(pady=20)
janela.mainloop()
        
# HELLO WORLD, DON´T GIVE UP
    