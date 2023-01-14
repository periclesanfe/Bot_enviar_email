import pyautogui as at
import pyperclip as pc
from time import sleep

at.PAUSE = 1

at.press('winleft')
at.write('chrome')
at.press('enter')
pc.copy('https://mail.google.com/mail/u/1/#inbox')
at.hotkey('ctrl', 'v')
at.press('enter')

sleep(5)

at.click(x=96, y=168)
at.write('celebrito03@gmail.com')
at.press('tab')
at.press('tab')

pc.copy('Teste de Automação')
at.hotkey('ctrl', 'v')
at.press('tab')
valor1 = 1512132
valor2 = 9312518

texto = f"""Olá amor da minha vida, Péricles aqui!

Estou usando seu email para teste!
Caso tenha recebido, manda uma mensagem no zap <3

vai ter uns numeros aqui pq eu to testando, como o :{valor1} e o {valor2}"""
pc.copy(texto)
at.hotkey('ctrl', 'v')
at.hotkey('ctrl', 'enter')
