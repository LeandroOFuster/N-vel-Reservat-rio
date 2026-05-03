from colorama import init, Fore, Style

init()

mensagens = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)",
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

print("=== Monitoramento do Reservatório ===\n")

for i in range(len(mensagens)):
    nivel = i + 1
    cor = definir_cor(nivel)
    print(cor + mensagens[i])

print(Style.RESET_ALL)