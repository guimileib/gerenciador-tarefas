# Código desenvolvido a partir das aulas de python da ROCKETSEAT, prof Gabriel Casemiro
# dev: guimileib

# Função adiciona tarefa
def adicionar_tarefa(tarefas, nome_tarefa): 
    tarefa = {"tarefa": nome_tarefa, "completada": False} 
    tarefas.append(tarefa) #adciona um elemento na lista
    print(f"\nTarefa {nome_tarefa} foi adicionada com sucesso!")
    return

# Função opção ver tarefas
def ver_tarefas(tarefas):
    print("\nLista de tarefas: ")
    for indice, tarefa in enumerate(tarefas, start = 1): # começando pelo 1 e não pelo 0
        status = "✓" if tarefa["completada"] else " " # diferenciando tarefa completada e de não completada
        nome_tarefa = tarefa["tarefa"] 
        print(f"{indice}. [{status}] {nome_tarefa}") # printando conforme a ordem 
    return
        
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa - 1) # tratando para selecionar apenas numeros inteiros e selecionar o indice 0
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas): # tratamento para apenas selecionar indices existentes
        tarefas[indice_tarefa_ajustado] ["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("\nIndice de tarefas inválido! Tente novamente:")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1 # mesmo tratamento usado na função anterior
    tarefas[indice_tarefa_ajustado]["completada"] = True # selecionando e marcando como "completada"
    print(f"Tarefa {indice_tarefa} marcada como completada.")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa) # usando remove para remover tarefa selecionada
    print("Tarefas completadas foram deletadas.")
    return 

tarefas = [] # lista que armazenará as tarefas

# MENU
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adcionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")
    
    escolha = input("Digite a sua escolha: ")
    
    # condicionais para escolha do gerenciador:
    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite um númmero da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break

print("Programa finalizado")
