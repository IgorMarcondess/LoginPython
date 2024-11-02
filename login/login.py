import customtkinter

customtkinter.set_appearance_mode("dark") #DEFININDO A COR DA JANELA - ("dark") COR DARK
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")# DEFININDO O TAMANHO DA TELA

def clique():
    mensagem.configure(text="Login realizado com sucesso!")#REALIZANDO O ENVIO DA MENSAGEM PÒS CLIQUE

#CRIANDO INPUTS E BOTÔES
texto = customtkinter.CTkLabel(janela, text="Faça login")
email = customtkinter.CTkEntry(janela, placeholder_text="E-mail") 
senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
button = customtkinter.CTkButton(janela, text="Login", command=clique)


mensagem = customtkinter.CTkLabel(janela, text="")#LABEL VAZIA PARA RECEBER A MENSAGEM DA FUNÇÃO

#ESPAÇAMENTO ENTRE AS LABELS 
texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
button.pack(padx=10, pady=10)
mensagem.pack(padx=10, pady=10)

janela.mainloop()