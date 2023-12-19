import re


digit_mask = r'\d'
symbol_mask = r'\W'
period_mask = r'.'

data = ['.', '4', '%']

digits = [0, 0, 0]
symbols =[0, 0, 0]
periods = [0, 0, 0]

fff = re.findall(digit_mask, data)
print(fff)
