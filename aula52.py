"""
Faça uma lista de comprar com listas o usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista não permita que
o programa quebre com erros de índices inexistentes na lista 

"""
# import os
        # os.system('clear')
        #minha Solução!
# lista_compras = []
# menu = 'ial'
# while True:
#     opcao = input( 'Selecione uma opção: \n [i]nserir [a]pagar [l]istar: ' ).lower()
#     if  opcao == 'l':
#         if len(lista_compras) > 0:
#             print(f' A sua Lista de compras tem os seguintes items : {lista_compras}')
#         else:
#             print('Lista de compras atualmente vazia. ')
#     elif opcao =='i':
#         item = input('Digite o nome do  item que vc gostaria de adicionar a lista:  ')
#         lista_compras.append(item)
#         print('Item foi adicionado a lista com sucesso!')
#     elif opcao =='a':
#         flag = False
#         remover_item = input('Digite o nome do item que vc gostaria de remover: ')
#         for index ,iten in enumerate(lista_compras):
#             if iten ==remover_item:
#                 lista_compras.pop(index)
#                 flag = True
#         if flag == False:
#             print('Nome do produto nao foi encontrado.')
#     else:
#         print('nenhuma opção encontrada')
        
        #Solução do Curso!
import os
lista = []
while True:
    print('Selecione uma opção')
    opcao = input ('[i]nserir [a]pagar [l]istar: ')
    
    if opcao =='i':
        os.system('clear')
        valor = input('valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_srt = input(
        'Escolha o índice para apagar: '
        )
        try:
            indice = int(indice_srt)
            del lista[indice]
        except:
            print('Não foi possível apagar este índice')
    elif opcao =='l':
        os.system('clear')
        if len(lista) ==0:
            print('Nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)