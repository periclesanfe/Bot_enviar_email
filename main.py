from time import sleep

import pyautogui as paut
import pyperclip as pcl

# Cooldown de 1 segundo entre cada comando
paut.PAUSE = 1

# abre o chrome
paut.press('winleft')
paut.write('chrome')
paut.press('enter')

# abre o email
pcl.copy('https://mail.google.com/mail/u/1/#inbox')  # utiliza a biblioteca pyperclip para colar texto com caracteres especiais
paut.hotkey('ctrl', 'v')
paut.press('enter')

sleep(5)

# Pega o email de um banco de dados
"""for index in len(seuBancoDeDados):
    email = tabela['email',index]"""

# escreve o email na aba de escrever
paut.click(x=96, y=168)
paut.write('email')
paut.press('tab')
paut.press('tab')

# escreve o assunto do email
pcl.copy('assunto')
paut.hotkey('ctrl', 'v')
paut.press('tab')

# Escreve o texto desejado e envia
texto = "Mensagem de texto"

pcl.copy(texto)
paut.hotkey('ctrl', 'v')
paut.hotkey('ctrl', 'enter')
