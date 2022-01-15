#Esse código serve para obter a posição do seu mouse 5 segundos após executar-lo

import pyautogui
import time
#pyautogui.position() serve para mostrar a posição do mouse e pode ser interligado con o time.sleep para ter a posição correta do clique
time.sleep(5)
posicao = pyautogui.position()

print(posicao)