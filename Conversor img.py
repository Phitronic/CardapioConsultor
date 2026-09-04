import customtkinter as ctk
from PIL import Image

#ctk.set_widget_scaling(1.50)

#janela = ctk.CTk()
#janela.title("Conversor de imagem")
#janela.geometry("800x600")

#Escolher_Formato = ctk.CTkLabel(janela, text="Qual Formato deseja escolher?")
#Escolher_Formato.pack(pady=(30, 15))



img = Image.open("C:/Users/Mihaeu/Documents/Metroider.webp")
img.save("C:/Users/Mihaeu/Documents/Metroider.png", "PNG", optimize=True)
#print("Conversão bem sucedida")

#janela.mainloop()
# Teste de conversor de Imagem




#                         Ferramentas para ir adicionando
# PIL.ImageGrab.grabclipboard (Para imprimir imagem do "Copiar")
# 
