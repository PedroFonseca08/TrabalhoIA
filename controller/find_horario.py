import re

def find_horario(arrText):
    # Padrão de regex para encontrar horários no formato HH:MM
    padrao_horario1 = r'\d{2}:\d{2}'
    padrao_horario2 = r'\d{1}:\d{2}'

    horario = ""

    # Procura por correspondências em cada elemento da lista usando regex
    for palavra in arrText:
        correspondencias = re.findall(padrao_horario1, palavra)
        if correspondencias:
            horario = correspondencias[0]
            break
        correspondencias = re.findall(padrao_horario2, palavra)
        if correspondencias:
            horario = correspondencias[0]
            break
    
    # Retorna a lista de horários encontrados
    return horario
