
animais = ['Avestruz', 'Gaviao', 'Macaco', 'Mosquito', 'Elefante', 'jacare', 'Boi', 'Vaca', 'Minhoca']

listaAnimal = [animal for animal in animais if animal[0] == 'M' and len(animal) <= 7]

print(listaAnimal)



mercado = {
    'Carne':{'Preco': 19.90, 'Fabrica': 150.00, 'Quantidade': 18},
    'Sabao':{'Preco': 13.90, 'Fabrica': 120.00, 'Quantidade': 20},
    'Biscoito':{'Preco': 23.90, 'Fabrica': 77.90, 'Quantidade': 78},
    'Pasta': {'Preco': 11.10, 'Fabrica': 58.90, 'Quantidade': 100},
}

Vendas = []
CompraEstoque = []

op = 0

while op != 4:
    print('1 - Registrar venda\n2 - Compra de estoque\n3 - Resumo da loja\n4 - Sair')
    op = int(input('Opçao: '))
    
    if op == 1:
        while True:
            alimento_vendido = (input('Alimento Vendido: '))
            try:
                quantidade_vendida = int(input('Quantidade Vendida: '))
                estoque_quantidade = mercado[alimento_vendido]['Quantidade']
                if quantidade_vendida <= estoque_quantidade:
                    print(f'\n{alimento_vendido} Vendido\n')
                    mercado[alimento_vendido]['Quantidade'] -= quantidade_vendida
                    Vendas.append(quantidade_vendida * mercado[alimento_vendido]['Preco'])
                    break
                else:
                    print(f'\nNão há {quantidade_vendida} unidades disponiveis para {alimento_vendido} no estoque.')
            except KeyError:
                print(f'\nProduto "{alimento_vendido}" alimento vendido nao encotrado no estoque. Por favor, Digite novamente.')
        print(f'\n{alimento_vendido} Vendido\n')
        mercado[alimento_vendido]['Quantidade'] -= quantidade_vendida
        Vendas.append(quantidade_vendida * mercado[alimento_vendido]['Preco'])
    elif op == 2:
        alimento_comprado = (input('Alimento comprado: '))
        quantidade_comprada = int(input('Quantidade comprada: '))
        print(f'\n{alimento_comprado} comprado\n')
        mercado[alimento_comprado]['Quantidade'] += quantidade_comprada
        CompraEstoque.append(quantidade_comprada * mercado[alimento_comprado]['Fabrica'])
        
    elif op == 3:
        print('\nQuantidade em estoque:')
        for produto, info in mercado.items():
            print(f'{produto}: {info["Quantidade"]}')


print(f'\nLucros: R${sum(Vendas)}')
print(f'\nDespesas: R${sum(CompraEstoque)}')
print(f'\nCaixa: R${sum(Vendas) - sum(CompraEstoque)}')
print('\nCaixa Fechado!')