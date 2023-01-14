# BOT-MAIL
<p align="center">
<img src="https://img.shields.io/badge/PARA TESTES-green">
</p>
Esse codigo básico permite que o dev cadastre uma mensagem, especifique o email e o assunto no qual quer enviar automaticamente

Esse codigo pode ser usado em um projeto maior, em loop lendo emails de uma base de dados e enviando uma mensagem automática para várias pessoas.

# BIBLIOTECAS
<p align="left">
<img src="https://img.shields.io/badge/PYAUTOGUI-green">
<img src="https://img.shields.io/badge/PYPERCLIP-green">
</p>

a biblioteca pyperclip é instalada junto com o PYAUTOGUI, para isso execute o comando no cmd do python:<br> pip install pyautogui<br><br>
caso o pyperclip nao seja reconhecido, executar:<br> pip install pyperclip

# NOÇÕES BASICAS DE PYAUTOGUI

import pyautogui<br>

pyautogui.click() -> clicar<br>
pyautogui.write('') -> escrever<br>
pyautogui.press() -> pressionar<br>
pyautogui.hotkey('','') -> atalho<br>
pyautogui.PAUSE = 'tempoEmSegundos' -> coloca um intervalo definido entre cada ação.
