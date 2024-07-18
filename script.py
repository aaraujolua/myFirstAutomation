# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import pandas
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.rightClick(x=653, y=172)
pyautogui.click(x=887, y=171)
time.sleep(1)
pyautogui.click(x=705, y=447)


# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)


# Passo 2: Fazer login
# selecionar o campo de email
# escrever o seu email
pyautogui.press("tab") # entrando no primeiro campo
pyautogui.write("emailteste@gmail.com")
pyautogui.press("tab") # passando pro proximo campo
pyautogui.write("rthbbbbbbbbbbbefjooargnorgno")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pandas.read_csv("produtos.csv")

print(tabela)

for produto in tabela.index:
    pyautogui.click(x=650, y=318)
    
    pyautogui.write(str(tabela.loc[produto, "codigo"]))
    
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[produto, "marca"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[produto, "tipo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[produto, "preco_unitario"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[produto, "custo"]))
    
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[produto, "custo"]))
    
    pyautogui.press("tab")
    obs = str(tabela.loc[produto, "obs"])
    
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)
