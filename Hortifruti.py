produtos = {} #abertura da lista de produtos

n = int(input("Quantidade de produtos: ")) #o usuário insere a quantidade de produtos que serão adicionados e essa quantidade é inserida na variável N

for i in range(n): #estrutura de repetição que irá repetir baseada na variável N, aberta anteriormente
    produto = input("Produto: ").lower() #variável produto recebe o nome do produto inserida pelo usuário
    preco = float(input("Preço: ")) #variável preço recebe o valor do produto inserido pelo usuário
    if produto in produtos: #condição, caso o produto já esteja cadastrado na lista de produtos o programa retorna "Produto já cadastrado", caso contrário o preço é adicionado junto ao produto na lista de produtos 
        print("Produto já cadastrado")
    else:
        produtos[produto] = preco

produto_busca = input("Produto a buscar (ou 'Fim' para sair): ").lower() #aqui começa a busca do usuário na lista de produtos, para verificar se o produto já está cadastrado
while produto_busca != "fim": #irá repetir até que a palavra "fim" seja digitada pelo usuário
    if produto_busca in produtos:
        print(f"O Preço de {produto_busca} é de: R${produtos[produto_busca]:.2f}") #se o produto estiver na lista ele será listado aqui juntamente com o preço
    else:
        print("Produto não cadastrado") #se o produto não estiver na lista o programa retorna "Produto não cadastrado", e então dará a opção de informar outro produto, ou digitar sair para finalizar o programa
    produto_busca = input("Produto a buscar (ou 'Fim' para sair): ").lower()
