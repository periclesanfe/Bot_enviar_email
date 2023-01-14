# Espera 5 segundos e pega a posição de sua tela de onde estiver o seu mouse

import pyautogui
import time

time.sleep(5)

print(pyautogui.position())
