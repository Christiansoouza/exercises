string = 'christian'
string_invertida = ''
tamanho_da_string = len(string)

for i in range(tamanho_da_string):
    string_invertida += string[tamanho_da_string - 1 - i]

print(string_invertida)