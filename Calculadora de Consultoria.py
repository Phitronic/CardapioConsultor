# agora vou fazer uma cálculadora de consultoria
# um teste para entender melhor o if, else e elif
import customtkinter as ctk
import pandas as pd
from PIL import Image
from tkinter import Canvas as CV

ctk.set_widget_scaling(1.50)

janela = ctk.CTk()
janela.title("Calculadora de consultoria")
janela.geometry("16:9")
print("sua calculadora de consultoria")


#trabalhando para adaptar o CTK pois não tenho experiencia nenhuma com isso (Até o momento)
label_servico = ctk.CTkLabel(janela, text=(''' Trabalhamos com os seguintes produtos:
    1 - Planilhas = R$100,00
    2 - Conversor de imagem = R$200,00
    3 - Limpeza de dados = R$50,00
     '''), justify="left")
label_servico.pack(pady=(60, 15))
entrada_servico = ctk.CTkEntry(janela, placeholder_text="Ex: 1")
entrada_servico.pack(pady=5)


label_proposta = ctk.CTkLabel(janela, text="Quanto deseja pagar?")
label_proposta.pack(pady=(30, 15))
entrada_proposta = ctk.CTkEntry(janela, placeholder_text="Ex: 100")
entrada_proposta.pack(pady=5)

label_Resultado = ctk.CTkLabel(janela, text="", text_color="Green")

#agora vou trabalhar a função antes de prosseguir

def processar_venda ():
    global label_Resultado
    servico_texto = entrada_servico.get()
    proposta_texto = entrada_proposta.get()
    try:
       valor_numerico = int(proposta_texto) 
#Configuração do primeiro produto
       if servico_texto == "1":
            label_Resultado.configure(text=">>> Planilhas Selecionado")
            if valor_numerico == 100:
                 label_Resultado.configure(text=">>> Sucesso: Pago com êxito")
            elif valor_numerico <= 99:
                 label_Resultado.configure(text=">>> Erro: Valor incompleto.")
            else:
                 label_Resultado.configure(text=">>> Aviso: Valor acima do preço.")
#Configuração do segundo produto
       if servico_texto == "2":
            label_Resultado.configure(text=">>> Conversor de imagem selecionado")
            if valor_numerico == 200:
                label_Resultado.configure(text=">>> Sucesso: Pago com êxito")
            elif valor_numerico <= 199:
                label_Resultado.configure(text=">>> Erro: Valor incompleto.")
            else:
                label_Resultado.configure(text=">>> Aviso: Valor acima do preço.")
#Configuração do terceiro produto
       if servico_texto == "3":
            label_Resultado.configure(text=">>> Limpeza de dados selecionado")
            if valor_numerico == 50:
                label_Resultado.configure(text=">>> Sucesso: Pago com êxito")
            elif valor_numerico <= 49:
                label_Resultado.configure(text=">>> Erro: Valor incompleto.")
            else:
                label_Resultado.configure(text=">>> Aviso: Valor acima do preço.")
    except ValueError:
        label_Resultado.configure(text=">>> Aviso: ERRO!!!!.")
botao_confirmar = ctk.CTkButton(janela, text="Verificar Pagamento", command=processar_venda)
botao_confirmar.pack(pady=20)
label_Resultado.pack(pady=(30, 15))
janela.mainloop()
        
# HELLO WORLD, DON´T GIVE UP
    