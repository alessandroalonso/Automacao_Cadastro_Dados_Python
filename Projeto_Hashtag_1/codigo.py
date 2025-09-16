import pyautogui
import time
import pandas


pyautogui.PAUSE = 0.5

#Passo 1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#abrir o edge
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

#digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#espera 3 segundos para conseguir digitar o email após o site abrir
time.sleep(3)


#Passo 2: Fazer Login
#preencher email
pyautogui.click(x=817, y=366)
pyautogui.write("pythonimpressionador@gmail.com")

#preencher a senha
pyautogui.press("tab")
pyautogui.write("senhasupersecreta")

#clicar no botão de logar
pyautogui.press("tab")
pyautogui.press("enter")

#espera de 3 segundos (opcional)
time.sleep(3)


#Passo 3: Importar a base de dados

tabela = pandas.read_csv("produtos.csv")
#detalhe: para funcionar, esse arquivo TEM que estar na sua pasta do código



#Passo 4: Cadastrar um produto

for linha in tabela.index: 

    pyautogui.click(x=826, y=250)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"]) 
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo =  str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)




#Passo 5: Repetir para todos os produtos. 


