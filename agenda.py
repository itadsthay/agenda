from datetime import date

# Data do registro atual
data_registro = date.today().strftime('%d/%m/%Y')

# Lista para armazenar os contatos
contatos = list()

# Função para adicionar um novo contato
def adicionar_contato():
    print('\tAdicionar contato')
    email = input('Digite o E-mail: ')
    
    # Verifica se o e-mail já está na lista de contatos
    if len(contatos) > 0:
        for contato in contatos:
            if email == contato['email']:
                print('Este contato já existe.')
                return True

    # Adiciona o novo contato
    contatos.append({
        'email': email.lower(),
        'nome': input('Nome: ').strip().capitalize(),
        'sobrenome': input('Sobrenome: ').strip().capitalize(),
        'telefone': input('Telefone: ').strip(),
        'data': date.today().strftime('%d/%m/%Y')
    })

# Função para alterar um contato existente
def alterar_contato():
    if len(contatos) > 0:
        email = input('Digite o e-mail do contato que deseja alterar: ')
        for contato in contatos:
            if contato['email'] == email:
                print(f"Nome do contato: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print('1 - Alterar nome')
                print('2 - Alterar telefone')
                print('3 - Voltar')
                escolha = input('>> ')
                
                if escolha == '1':
                    novo_nome = input('Digite um novo nome para o contato: ')
                    contato['nome'] = novo_nome
                    return
                elif escolha == '2':
                    novo_tel = input('Digite um novo telefone para o contato: ')
                    contato['telefone'] = novo_tel
                    return
                elif escolha == '3':
                    return
                else:
                    print('Opção inválida.')
                    return
        print('Não existe usuário cadastrado com o e-mail informado.')
    else:
        print('Não há contatos registrados na agenda.')

# Função para procurar um contato pelo e-mail
def procurar_contato():
    if len(contatos) > 0:
        email = input('Digite o e-mail do contato: ')
        for contato in contatos:
            if contato['email'] == email:
                print(f"Nome: {contato['nome']} {contato['sobrenome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Data de registro: {contato['data']}")
                return
        print('Contato não encontrado.')
    else:
        print('Não há contatos registrados na agenda.')

# Função para remover um contato pelo e-mail
def remover_contato():
    if len(contatos) > 0:
        email = input('Digite o e-mail do contato que deseja remover: ')
        x = 0
        while x < len(contatos):
            if contatos[x]['email'] == email:
                contatos.remove(contatos[x])
                print('Contato removido com sucesso.')
                return True
            x += 1
        print('Contato não encontrado.')
    else:
        print('Não há contatos registrados na agenda.')

# Função para exibir todos os contatos ordenados por nome e sobrenome
def ver_contatos():
    if len(contatos) > 0:
        contatos_ordenados = sorted(contatos, key=lambda contato: contato['nome'] + ' ' + contato['sobrenome'])
        for indice, contato in enumerate(contatos_ordenados, start=1):
            print(f'Contato {indice}'.center(100, ' '))
            print(f"Nome: {contato['nome']} {contato['sobrenome']}")
            print(f"E-mail: {contato['email']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Data de registro: {contato['data']}")
            print()
    else:
        print('Não há contatos registrados na agenda.')

# Menu principal
def menu():
    print('Programa Agenda  '.center(100, ' '))
    print('\t1 - Adicionar contato')
    print('\t2 - Alterar contato')
    print('\t3 - Procurar contato')
    print('\t4 - Remover contato')
    print('\t5 - Ver contatos')
    print('\t6 - Sair')

# Função principal
def main():
    escolha = ''
    while escolha != '6':
        menu()
        escolha = input('>> ')
        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            alterar_contato()
        elif escolha == '3':
            procurar_contato()
        elif escolha == '4':
            remover_contato()
        elif escolha == '5':
            ver_contatos()
        elif escolha == '6':
            print('Fim do Programa.')
        else:
            print('Escolha inválida')

# Executa o programa
if __name__ == '__main__':
    main()
