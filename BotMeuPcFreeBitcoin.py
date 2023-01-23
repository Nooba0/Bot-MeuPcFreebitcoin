import pyautogui
import time
import keyboard





while keyboard.is_pressed('k') == False:
    time.sleep(5)
    print(pyautogui.position())


#CLICA NO CRHOME
    time.sleep(2)
    pyautogui.click(x=762, y=1061)

#SELECIONA BARRA PESQUISA
    time.sleep(5)
    pyautogui.click(x=604, y=48)

#DIGITA BARRA PESQUISA
    time.sleep(2)
    pyautogui.write('fre')

#BOTAO ENTER
    time.sleep(2)
    pyautogui.press('enter')

#ABAIXA SCROLL
    time.sleep(3)
    pyautogui.click(x=1909, y=925)

#Caixa Preencher
    time.sleep(2)
    pyautogui.click(x=831, y=785)

#Selecionar Roll
    time.sleep(2)
    pyautogui.click(x=953, y=875)


#MINIMIZA PAGINA
    time.sleep(3)
    pyautogui.click(x=1796, y=9)
    time.sleep(3600)














