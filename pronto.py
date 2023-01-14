from time import sleep
import pyautogui as at
import pyperclip as pc
import pandas as pd

at.PAUSE = 1

at.press('winleft')
at.write('chrome')
at.press('enter')
pc.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
at.hotkey('ctrl', 'v')
at.press('enter')

sleep(5)

at.click(x=190, y=274)
at.click(x=174, y=320)
at.click(x=1833, y=93)

tabela = pd.read_excel(r'C:\Users\xxmra\Downloads\Vendas - Dez.xlsx')
print(tabela)

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

print(faturamento, quantidade)
