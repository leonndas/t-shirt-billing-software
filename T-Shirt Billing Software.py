# design da loja
print('Bem vindo à Fábrica de Camisetas do Leon Santiago')
print('Entre com o modelo desejado:')
print(' ')
print('MCS - Manga Curta Simples')
print('MLS - Manga Longa Simples')
print('MCE - Manga Curta com Estampa')
print('MLE - Manga Longa com Estampa')

# funções
def template():  # escolha_modelo
    template_choice = input('Qual o modelo desejado? (MCS, MLS, MCE ou MLE):').upper()  # com verificação de maiúscula

    while template_choice not in ['MCS', 'MLS', 'MCE', 'MLE']:  # while template != MCS and...
        print('Tente escrever algum modelo: MCS, MLS, MCE ou MLE.')
        template_choice = input('Qual o modelo desejado? (MCS, MLS, MCE ou MLE):').upper()
    
    #modelo 
    if template_choice == 'MCS':
        return template_choice, 1.80 #vai retornar escolha de modelo e valor de modelo 
    elif template_choice == 'MLS':
        return template_choice, 2.10
    elif template_choice == 'MCE':
        return template_choice, 2.90
    elif template_choice == 'MLE':
        return template_choice, 3.20

def tshirts_no():  # num_camisetas
    while True:  # loop de numeral e >20.000 camisetas
        try:
            qtty = int(input('Quantas camisetas?:'))  
            if qtty > 20000:
                print('O pedido máximo de camisetas é de 20.000 peças. Sentimos muito.')
            else:
                break  # sair do loop
        except ValueError: #se n for numero
            print('Por favor, insira um número valido.')

    #quantidades de camiseta
    if qtty < 20:
        disc = 0
    elif qtty >= 20 and qtty <= 200:
        disc = 5 / 100
    elif qtty >= 200 and qtty <= 2000:
        disc = 7 / 100
    elif qtty >= 2000 and qtty <= 20000:
        disc = 12 / 100 

    return qtty, disc #retornar a quantidade e o desconto

def delivery():  # frete
    print('Escolha o frete desejado:')
    print('1. Transportadora')
    print('2. Sedex')
    print('3. Retirar na fábrica')

    while True:
        try:
            dlvChoice = int(input('Qual opção de frete você gostaria?'))
            if dlvChoice in [1, 2, 3]: 
                break #se for alguma elegivel pode sair do loop
            else: 
                print('Tente escolher algum frete.')
        except ValueError: #se n for numero
            print('Por favor, insira um número valido.')

    #retornar o valor dos fretes
    dlvPrice = 0
    if dlvChoice == 1:
        return 100  
    elif dlvChoice == 2:
        return 200
    elif dlvChoice == 3:
        return dlvPrice

    return dlvPrice

# main code
modelo, preco = template()
quantidade, desconto = tshirts_no()
frete = delivery()

total_sem_desconto = preco * quantidade
valor_desconto = total_sem_desconto * desconto
total_com_desconto = total_sem_desconto - valor_desconto
total = total_com_desconto + frete

print(f'Você pediu {quantidade} de camisetas {modelo}. O valor total é R$ {total:.2f}, sendo R${valor_desconto:.2f} de desconto e R${frete:.2f} de frete')
