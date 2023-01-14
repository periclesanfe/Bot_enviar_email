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

a biblioteca pyperclip é instalada junto com o PYAUTOGUI, para isso execute o comando no cmd do python: pip install pyautogui
caso o pyperclip nao seja reconhecido, executar: pip install pyperclip

# NOÇÕES BASICAS DE PYAUTOGUI

import pyautogui

pyautogui.click() -> clicar
pyautogui.write('') -> escrever
pyautogui.press() -> pressionar
pyautogui.hotkey('','') -> atalho
pyautogui.PAUSE = 'tempoEmSegundos' -> coloca um intervalo definido entre cada ação
