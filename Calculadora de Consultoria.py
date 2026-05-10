# agora vou fazer uma cálculadora de consultoria
# um teste para entender melhor o if, else e elif
import customtkinter as ctk
import pandas as pd

ctk.set_widget_scaling(1.50)

janela = ctk.CTk()
janela.title("Calculadora de consultoria")
janela.geometry("1280x960")
print("sua calculadora de consultoria")

#trabalhando para adaptar o CTK pois não tenho experiencia nenhuma com isso (Até o momento)
label_servico = ctk.CTkLabel(janela, text=(''' Trabalhamos com os seguintes produtos:
    1 - Planilhas = R$100,00
    2 - Automação web = R$200,00
    3 - Limpeza de dados = R$50,00
     '''), justify="left")
label_servico.pack(pady=(60, 15))
entrada_servico = ctk.CTkEntry(janela, placeholder_text="Ex: 1")
entrada_servico.pack(pady=5)


label_proposta = ctk.CTkLabel(janela, text="Quanto deseja pagar?")
label_proposta.pack(pady=(30, 15))
entrada_proposta = ctk.CTkEntry(janela, placeholder_text="Ex: 100")
entrada_proposta.pack(pady=5)

#agora vou trabalhar a função antes de prosseguir

def processar_venda ():
    servico_texto = entrada_servico.get()
    proposta_texto = entrada_proposta.get()
    try:
       valor_numerico = int(proposta_texto) 
#Configuração do primeiro produto
       if servico_texto == "1":
            print("Item selecionado: Planilhas (R$ 100,00)")
            if valor_numerico == 100:
                print(">>> Sucesso: Pago com êxito!")
            elif valor_numerico <= 99:
                print(">>> Erro: Valor incompleto.")
            else:
                print(">>> Aviso: Valor acima do preço.")   
#Configuração do segundo produto
       if servico_texto == "2":
            print("Item selecionado: Automação Web (R$ 200,00)")
            if valor_numerico == 200:
                print(">>> Sucesso: Pago com êxito!")
            elif valor_numerico <= 199:
                print(">>> Erro: Valor incompleto.")
            else:
                print(">>> Aviso: Valor acima do preço.")
#Configuração do terceiro produto
       if servico_texto == "3":
            print("Item selecionado: Limpeza de dados (R$ 50,00)")
            if valor_numerico == 50:
                print(">>> Sucesso: Pago com êxito!")
            elif valor_numerico <= 49:
                print(">>> Erro: Valor incompleto.")
            else:
                print(">>> Aviso: Valor acima do preço.")
    except ValueError:
        print("eroooou")
botao_confirmar = ctk.CTkButton(janela, text="Verificar Pagamento", command=processar_venda)
botao_confirmar.pack(pady=20)
janela.mainloop()
        
# HELLO WORLD, DON´T GIVE UP
    