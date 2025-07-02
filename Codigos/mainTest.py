# sistema de Compra e venda de produtos
# Trabalho produzido para atividade de 1o periodo, Fundamentos de Software
# Sistema permite que o gerenciamento de Vendedor, Produto e Comprador.
# Autor: Vinícius Simões
# Inicio de produção: 27/06/2025
# Conclusão de produção: XX/06/2025

##### IMPORT #####
import os


##### METODOS #####

# exibir menu
def printMenu (tipoMenu):
    match tipoMenu:
        case "inicio":
            print ("*" * 11, " MENU ", "*" * 11)
            print ("*", " 1 - Realizar Compra"      , " " * 5, "*")
            print ("*", " 2 - Gerenciar Produtos"   , " " * 2, "*")
            print ("*", " 3 - Gerenciar Vendedores" , " " * 0, "*")
            print ("*", " 4 - Gerenciar Compradores", "*")
            print ("*", " 0 - SAIR", " " * 16, "*")
            print ("*" * 30)
        case "GVenda":
            print ("*" * 11, " VENDA ", "*" * 12)
            print ("*", " 1 - Ver Produtos"        , " " * 10, "*")
            print ("*", " 2 - Chamar Vendedor"     , " " * 7, "*")
            print ("*", " 3 - Adicionar ao Carrinho" , " " * 1, "*")
            print ("*", " 4 - Ver Carrinho" , " " * 10, "*")
            print ("*", " 5 - Finalizar Compra" , " " * 6, "*")
            print ("*", " 6 - Emitir Notas Fiscais", " " * 2, "*")
            print ("*", " 0 - VOLTAR", " " * 16, "*")
            print ("*" * 32)
        case "GProdutos":
            print ("*" * 8, " PRODUTOS ", "*" * 8)
            print ("*", " 1 - Adicionar Produto", " " * 1, "*")
            print ("*", " 2 - Listar Produtos"  , " " * 3, "*")
            print ("*", " 3 - Alterar Produtos" , " " * 2, "*")
            print ("*", " 4 - Remover Produto"  , " " * 3, "*")
            print ("*", " 0 - VOLTAR  ", " " * 10, "*")
            print ("*" * 28)
        case "GVendedores":
            print ("*" * 8, " Vendedores ", "*" * 8)
            print ("*", " 1 - Adicionar Vendedores", " *")
            print ("*", " 2 - Listar Vendedores"   , " " * 3 , "*")
            print ("*", " 3 - Atualizar Vendedores", " " * 0 , "*")
            print ("*", " 4 - Remover Vendedores"  , " " * 2 , "*")
            print ("*", " 0 - VOLTAR  "            , " " * 12, "*")
            print ("*" * 30)
        case "GCompradores":
            print ("*" * 8, " COMPRADORES ", "*" * 8)
            print ("*", " 1 - Adicionar Compradores", " *")
            print ("*", " 2 - Listar Compradores"   , " " * 3 , "*")
            print ("*", " 3 - Atualizar Compradores", " " * 0 , "*")
            print ("*", " 4 - Remover Compradores"  , " " * 2 , "*")
            print ("*", " 0 - VOLTAR  "             , " " * 13, "*")
            print ("*" * 31)

## Gerenciar Vendas ##
# Atributos
cod_venda:int   # auto incremeto
controle_estoque: int
valor_compra_produto:float
valor_venda: float
carrinho = []

# código de venda com auto incremento
def gerar_prox_cod_venda ():
    try:
        with open ("notaFiscal.txt", "r") as f:
            linhas = f.readlines()

            if not linhas:
                return 1
            
            ultimo_cod_venda = [int(linha.split(",")[0].strip()) for linha in linhas]
            return max (ultimo_cod_venda) + 1
        
    except FileNotFoundError:
        print ("Arquivo não encontrado")
        return 1

# calcualr valor do produto
def calc_preco_produto (preco_unitario, qtneDesejada_venda):
    # forçar para float
    float_preco_unitario = float (preco_unitario)
    float_qtneDesejada_venda = float (qtneDesejada_venda)
    valor_compra_produto = float_preco_unitario * float_qtneDesejada_venda
    return valor_compra_produto

# adicionar compra
def adicionar_ao_carrinho (cpf_comprador_venda, cod_produto_venda, qtneDesejada_venda, cod_vendedor_venda):
    try:
        
        produto_encontrado = False
        vendedor_encontrado = False
        comprador_encontrado = False

        info_produto = None
        info_vendedor = None
        info_comprador = None

        # recebe lista de produtos
        with open ("produto.txt", "r") as f:
            for linha in f:
                cod_produto, nome_produto, qtde_estoque, preco_unitario = [item.strip() for item in linha.strip().split(",")]

                if cod_produto_venda == cod_produto:
                    produto_encontrado = True
                    info_produto = {
                        "cod_produto": cod_produto, 
                        "nome_produto": nome_produto, 
                        "qtde_estoque": int(qtde_estoque), 
                        "preco_unitario": float(preco_unitario)
                    }
                    break
        
        # testa se encontrou
        if not produto_encontrado:
            print("Produto não encontrado. Não adicionado ao carrinho.")
            return 

        # testa se esta disponivel no estoque
        if info_produto["qtde_estoque"] < int(qtneDesejada_venda):
            print(f"Quantidade de produto indisponível, apenas {info_produto['qtde_estoque']} em estoque. \nNão foi possível adicionar ao carrinho. \n")
            return


        # recebe lista de vendedores
        with open ("vendedor.txt", "r") as f:
            for linha in f:
                cod_vendedor, nomeVendedor, salarioFixo, comissao, salarioMes = [item.strip() for item in linha.strip().split(",")]
                if cod_vendedor_venda == cod_vendedor:
                    vendedor_encontrado = True
                    info_vendedor = {
                        "cod_vendedor": cod_vendedor,
                        "nomeVendedor": nomeVendedor,
                        "salarioFixo": float(salarioFixo),
                        "comissao": float(comissao),
                        "salarioMes": float(salarioMes)
                    }
                    break

            if not vendedor_encontrado:
                print("Vendedor não encontrado. Cancelando adição ao carrinho.")
                return


        # recebe lista de compradores
        with open ("comprador.txt", "r") as f:
            comprador_encontrado = False
            for linha in f:
                cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado = [item.strip() for item in linha.strip().split(",")]
                if cpf_comprador_venda == cpf_comprador:
                    comprador_encontrado = True
                    info_comprador = {
                        "cpf_comprador": cpf_comprador,
                        "nomeComprador": nomeComprador
                    }
                    break

            if not comprador_encontrado:
                print("Comprador não encontrado. Cancelando venda.")
                return

        # Adiciona o item ao carrinho
        carrinho.append({
            "cpf_comprador": cpf_comprador_venda,
            "cod_produto": cod_produto_venda,
            "qtneDesejada": int(qtneDesejada_venda),
            "cod_vendedor": cod_vendedor_venda,
            "info_produto": info_produto,
            "info_vendedor": info_vendedor,
            "info_comprador": info_comprador
        })
        print(f"Produto '{info_produto['nome_produto']}' adicionado ao carrinho com sucesso.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Finalizar compra do carrinho
def finalizar_compra ():
    global carrinho
    
    if not carrinho:
        print("Carrinho vazio. Adicione produtos antes de finalizar a compra.")
        return

    vendas_realizadas_com_sucesso = []

    for item in carrinho:
        cpf_comprador_venda = item["cpf_comprador"]
        cod_produto_venda = item["cod_produto"]
        qtneDesejada_venda = item["qtneDesejada"]
        cod_vendedor_venda = item["cod_vendedor"]
        info_produto = item["info_produto"]
        info_vendedor = item["info_vendedor"]
        info_comprador = item["info_comprador"]

        # Calcular valor total da compra do produto
        valor_compra_item = calc_preco_produto(info_produto["preco_unitario"], qtneDesejada_venda)

        # calcular frete
        valor_final_com_frete = valor_compra_item
        if valor_compra_item < 100.0:
            valor_final_com_frete += 30.0
        elif valor_compra_item < 301.0:
            valor_final_com_frete += 20.0

        # atualizar o estoque
        if not atualizar_estoque (cod_produto_venda, qtneDesejada_venda):
            print(f"Venda para o produto '{info_produto['nome_produto']}' (Cód: {cod_produto_venda}) cancelada devido a problemas no estoque.")
            continue

        # atribuir comissao
        adicionar_comissao_vendedor (info_vendedor["nomeVendedor"], valor_final_com_frete)

        # recebe código atual
        cod_venda_atual = gerar_prox_cod_venda()

        # Converter valores para string
        valor_final_com_frete_str = f"{valor_final_com_frete:.2f}"
        cod_venda_atual_str = str(cod_venda_atual)
        qtneDesejada_venda_str = str(qtneDesejada_venda)
        preco_unitario_str = f"{info_produto['preco_unitario']:.2f}"

        # criar venda
        try:
            with open ("notaFiscal.txt", "a") as f:
                f.write(f"{cod_venda_atual_str}, {info_comprador['nomeComprador']}, {cpf_comprador_venda}, {info_produto['nome_produto']}, {cod_produto_venda}, {qtneDesejada_venda_str}, {preco_unitario_str}, {valor_final_com_frete_str}, {cod_vendedor_venda}\n")
                print (f"Venda: {cod_venda_atual_str}, do cliente: {info_comprador['nomeComprador']} para o produto '{info_produto['nome_produto']}' finalizada com sucesso. Valor total a pagar: R$ {valor_final_com_frete_str}")
                vendas_realizadas_com_sucesso.append(item)

        except FileNotFoundError:
            print("Arquivo notaFiscal.txt não encontrado ao tentar registrar a venda.")
    
    # Limpa o carrinho
    carrinho = [item for item in carrinho if item not in vendas_realizadas_com_sucesso]

    if not carrinho:
        print("\nVendas finalizadas.")
    else:
        print("\nAlguns itens permaneceram no carrinho por causa de algum erro na finalização da venda.")

# Vizualizar o carrinho
def ver_carrinho():
    if not carrinho:
        print("Carrinho esta vazio.")
        return

    for i, item in enumerate(carrinho):
        print(f"Item {i+1}:")
        print(f"  Produto: {item['info_produto']['nome_produto']} (Cód: {item['cod_produto']})")
        print(f"  Quantidade: {item['qtneDesejada']}")
        print(f"  Vendedor: {item['info_vendedor']['nomeVendedor']} (Cód: {item['cod_vendedor']})")
        print(f"  Comprador: {item['info_comprador']['nomeComprador']} (CPF: {item['cpf_comprador']})")

# Ler vendedor (atendimento)
def ler_venda ( ):
    try:
        with open ("notaFiscal.txt", "r") as f:
            for linha in f:
                partes = [p.strip() for p in linha.strip().split(",")]
                if len(partes) == 9:
                    cod_venda_atual, nomeComprador, cpf_comprador_venda, nome_produto, cod_produto_venda, qtneDesejada_venda, preco_unitario, valor_venda, cod_vendedor_venda = partes
                    print (f"\nCódigo da venda: {cod_venda_atual}, CPF comprador: {cpf_comprador_venda}, nome do comprador: {nomeComprador}, \nAtendente: {cod_vendedor_venda}\n Dados do produto: \n->Nome: {nome_produto},\n->Cód: {cod_produto_venda}, \n->Quantidade: {qtneDesejada_venda}, \n->Preço: {preco_unitario}, \n->Valor da compra: {valor_venda}.")
                else:
                    print(f"Formato de linha inválido em notaFiscal.txt: {linha.strip()}")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")





## Gerenciar Produtos ##
# Atributos
cod_produto = int
nome_produto = str
qtde_estoque = int
preco_unitario:float = 10.0

# adicionar produto (Crud)
def criar_produto (cod_produto, nome_produto, qtde_estoque, preco_unitario):
    try:
        # Verifica se já existe
        with open ("produto.txt", "r") as f:
            linhas = f.readlines()
            encontrado = False
            for linha in linhas:
                if cod_produto in linha.strip().split(",")[0].strip(): # Verifica apenas o código
                    encontrado = True
                    break

        # Já existe. Cancela.
        if encontrado == True:
            print (f"Erro! Produto de codigo {cod_produto} já existe. Ação interrompida.")

        # Nao existe. Cria novo.
        else:
            with open ("produto.txt", "a") as f:
                f.write(f"{cod_produto}, {nome_produto}, {qtde_estoque}, {preco_unitario}\n")
                print (f"Produto {nome_produto} adicionado com sucesso.")
    
    except FileNotFoundError:
        print("Arquivo não encontrado.")

# ler produto (cRud)
def ler_produto ():
    try:
        with open ("produto.txt", "r") as f:
            for linha in f:
                cod_produto, nome_produto, qtde_estoque, preco_unitario = [item.strip() for item in linha.split(",")]
                print (f"Codigo: {cod_produto}, Nome: {nome_produto}, Quantidade em estoque: {qtde_estoque}, Preco Unitario: {preco_unitario}")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# atualizar produto (crUd)
def atualizar_produto (antigo_cod_produto, novo_cod_produto, novo_nome_produto, novo_qtde_estoque, novo_preco_unitario):
    try:
        with open ("produto.txt", "r") as f:
            linhas = f.readlines()
        
        with open ("produto.txt", "w") as f:
            encontrado = False

            for linha in linhas:
                partes = [item.strip() for item in linha.strip().split(",")]

                if len(partes) == 4:
                    cod_produto, nome_produto, qtde_estoque, preco_unitario = partes

                    if cod_produto == antigo_cod_produto:
                        f.write (f"{novo_cod_produto}, {novo_nome_produto}, {novo_qtde_estoque}, {novo_preco_unitario}\n")
                        encontrado = True
                        print (f"Produto de codigo {antigo_cod_produto} atualizado com sucesso para codigo {novo_cod_produto}")
                    else:
                        f.write(linha)
                else:
                    f.write(linha)
            if not encontrado:
                print (f"Produto {antigo_cod_produto} não encontrado.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# deletar produto (cruD)
def deletar_produto (cod_produto_para_deletar):
    try:
        with open ("produto.txt", "r") as f:
            linhas = f.readlines()

        with open ("produto.txt", "w") as f:
            encontrado = False

            for linha in linhas:
                if linha.strip().split(",")[0].strip() != cod_produto_para_deletar:
                    f.write (linha)
                else:
                    encontrado = True
                    print (f"O produto {cod_produto_para_deletar} foi deletado.")

            if not encontrado:
                print (f"O produto {cod_produto_para_deletar} não foi encontrado.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# atualizar estoque
# Receber comissão
def atualizar_estoque (cod_produto_escolhido, qtneDesejada_venda):
    try:
        # receber vendedores
        with open ("produto.txt", "r") as f:
            linhas = f.readlines( )
        
        produto_atualizado = False
        novas_linhas = []

        for linha in linhas:
            partes = [item.strip() for item in linha.strip().split(",")]
            if len(partes) == 4:
                cod_produto, nome_produto, qtde_estoque_str, preco_unitario = partes
                
                if cod_produto_escolhido == cod_produto:
                    qtde_estoque = int(qtde_estoque_str)
                    qtneDesejada_venda_int = int(qtneDesejada_venda)

                    if qtde_estoque < qtneDesejada_venda_int:
                        print(f"ERRO: Quantidade de produto '{nome_produto}' em estoque ({qtde_estoque}) insuficiente para a venda de {qtneDesejada_venda_int} unidades. Venda cancelada para este item.")
                        return False

                    nova_qtde_estoque = qtde_estoque - qtneDesejada_venda_int
                    novas_linhas.append(f"{cod_produto}, {nome_produto}, {nova_qtde_estoque}, {preco_unitario}\n")
                    produto_atualizado = True
                else:
                    novas_linhas.append(linha)
            else:
                novas_linhas.append(linha) 

        if not produto_atualizado:
            print(f"Produto de código {cod_produto_escolhido} não encontrado no estoque.")
            return False

        with open ("produto.txt", "w") as f:
            f.writelines(novas_linhas)
        return True

    except FileNotFoundError:
        print ("Arquivo não encontrado.")





## Gerenciar Vendedores ##
# Atributos
cod_vendedor: int 
nomeVendedor = str
salarioFixo:float = 10.0
comissao:float = 10.0

# autoincremente cod
def gerar_prox_cod_vendedor ():
    try:
        with open ("vendedor.txt", "r") as f:
            linhas = f.readlines()

            if not linhas:
                return 1
            
            ultimo_cod_vendedor = [int(linha.split(",")[0].strip()) for linha in linhas]
            return max (ultimo_cod_vendedor) + 1
        
    except FileNotFoundError:
        print ("Arquivo não encontrado")
        return 1

# Criar vendedor  # Cod com autoincremente
def criar_vendedor (nomeVendedor, salarioFixo):
    try:
        # recebe cod_vendedor atual
        cod_vendedor = gerar_prox_cod_vendedor()
        
        # iniciar sem comissao
        comissao = 0.00
        
        # calcular salario do mes
        floatSalarioFixo = float(salarioFixo)
        floatComissao = float(comissao)
        salarioMes = floatSalarioFixo + floatComissao
        salarioMes = str(salarioMes)
        comissao = str(comissao)

        # Verifica se o vendedor já existe
        with open("vendedor.txt", "r") as f:
            for linha in f:
                if nomeVendedor.lower() == linha.strip().split(",")[1].strip().lower():
                    print(f"Erro! Vendedor '{nomeVendedor}' já existe. Ação interrompida.")
                    return

        # escreve novo vendedor
        with open ("vendedor.txt", "a") as f:
            f.write (f"{cod_vendedor}, {nomeVendedor}, {salarioFixo}, {comissao}, {salarioMes}\n")
            print (f"O vendedor {nomeVendedor}, de codigo {cod_vendedor}, foi registrado com sucesso.")

    except FileNotFoundError:
        print ("Arquivo não encontrado")

# Ler vendedor
def ler_vendedor ():
    try:
        with open ("vendedor.txt", "r") as f:
            for linha in f:
                partes = [item.strip() for item in linha.strip().split(",")]
                if len(partes) == 5:
                    cod_vendedor, nomeVendedor, salarioFixo, comissao, salarioMes = partes

                    floatSalarioFixo = float(salarioFixo)
                    floatComissao = float(comissao)
                    salarioMes_calculado = floatSalarioFixo + floatComissao

                    print (f"Nome: {nomeVendedor}, Cód: {cod_vendedor}, Salário fixo: {floatSalarioFixo:.2f}, Comissão acumulada: {floatComissao:.2f}, Salário do mês: {salarioMes_calculado:.2f}\n")
                else:
                    print(f"Formato de linha inválido em vendedor.txt: {linha.strip()}")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Ler vendedor (atendimento)
def ler_vendedor_atendendo ( ):
    try:
        with open ("vendedor.txt", "r") as f:
            for linha in f:
                cod_vendedor, nomeVendedor, _, _, _ = [item.strip() for item in linha.strip().split(",")]
                print (f"{nomeVendedor}, cód:{cod_vendedor}.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Atualizar vendedor
def atualizar_vendedor (antigo_nomeVendedor, novo_nomeVendedor, novo_salarioFixo):
    try:
        # recebe vendedor
        with open ("vendedor.txt", "r") as f:
            linhas = f.readlines()

        # buscar vendedor
        with open ("vendedor.txt", "w") as f:
            encontrado = False
            for linha in linhas:
                partes = [item.strip() for item in linha.strip().split(",")]

                if len(partes) == 5:
                    cod_vendedor, nomeVendedor, salarioFixo, comissao, salarioMes = partes

                    if nomeVendedor == antigo_nomeVendedor:
                        f.write (f"{cod_vendedor}, {novo_nomeVendedor}, {novo_salarioFixo}, {comissao}, {salarioMes}\n")
                        encontrado = True
                        print (f"O(a) vendedor(a) {novo_nomeVendedor}, antigo {antigo_nomeVendedor}, foi atualizado com sucesso.")
                    else:
                        f.write(linha)
                else:
                    f.write(linha) 

            if not encontrado:
                print (f"Vendedor(a) {antigo_nomeVendedor} não foi encontrado(a). Encerrando ação.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Deletar vendedor
def deletar_vendedor (apagar_cod_vendedor):
    try:
        # receber lista
        with open ("vendedor.txt", "r") as f:
            linhas = f.readlines( )

        novas_linhas = []
        encontrado = False

        for linha in linhas:
            partes = [item.strip() for item in linha.strip().split(",")]

            if len(partes) > 0 and partes[0] == apagar_cod_vendedor:
                encontrado = True
                print(f"Vendedor(a) {partes[1]}, de código {apagar_cod_vendedor}, foi deletado(a).")
            else:
                novas_linhas.append(linha)

        with open ("vendedor.txt", "w") as f:
            f.writelines(novas_linhas)

        if not encontrado:
            print (f"O código {apagar_cod_vendedor} não foi encontrado.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Receber comissão
def adicionar_comissao_vendedor (nomeVendedor_atendendo, valor_venda):
    try:
        # receber vendedores
        with open ("vendedor.txt", "r") as f:
            linhas = f.readlines( )
        
        vendedor_atualizado = False
        novas_linhas = []

        for linha in linhas:
            partes = [item.strip() for item in linha.strip().split(",")]

            if len(partes) == 5:
                cod_vendedor, nomeVendedor, salarioFixo, comissao_str, salarioMes_str = partes
                
                if nomeVendedor_atendendo == nomeVendedor:
                    comissao = float(comissao_str)
                    salarioFixo = float(salarioFixo)
                    
                    # 3% do valor da venda
                    nova_comissao = comissao + (valor_venda * 0.03) 
                    novo_salarioMes = salarioFixo + nova_comissao
                    
                    novas_linhas.append(f"{cod_vendedor}, {nomeVendedor}, {salarioFixo:.2f}, {nova_comissao:.2f}, {novo_salarioMes:.2f}\n")
                    vendedor_atualizado = True
                else:
                    novas_linhas.append(linha)
            else:
                novas_linhas.append(linha)
        
        if not vendedor_atualizado:
            print(f"Vendedor(a) {nomeVendedor_atendendo} não encontrado(a) para adicionar comissão.")
            return

        with open ("vendedor.txt", "w") as f:
            f.writelines(novas_linhas)

    except FileNotFoundError:
        print ("Arquivo vendedor.txt não encontrado.")





## Gerenciar Comprador ##
# Atributos
cpf_comprador:str
email: str
nomeComprador: str
cep: str
rua: str
bairro: str
cidade: str
estado: str

# Criar comprador
def criar_comprador (cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado):
    try:
        # Verifica se o comprador já existe
        with open("comprador.txt", "r") as f:
            for linha in f:
                if cpf_comprador == linha.strip().split(",")[0].strip():
                    print(f"Erro! Comprador com CPF {cpf_comprador} já existe. Ação interrompida.")
                    return
                
        # escreve novo comprador
        with open ("comprador.txt", "a") as f:
            f.write (f"{cpf_comprador}, {email}, {nomeComprador}, {cep}, {rua}, {bairro}, {cidade}, {estado}\n")
            print (f"O comprador {nomeComprador}, foi registrado com sucesso.")

    except FileNotFoundError:
        print ("Arquivo não encontrado")

# Ler comprador
def ler_comprador ():
    try:
        with open ("comprador.txt", "r") as f:
            for linha in f:
                partes = [item.strip() for item in linha.strip().split(",")]
                if len(partes) == 8:
                    cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado = partes
                    print (f"\nNome: {nomeComprador}, CPF: {cpf_comprador}, \nContato: {email}, CEP:{cep}, \nEndereço: \n->Rua: {rua}, \n->Bairro: {bairro}, \n->Cidade: {cidade}, \n->Estado: {estado}")
                else:
                    print(f"Formato de linha inválido em comprador.txt: {linha.strip()}")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Atualizar comprador
def atualizar_comprador (antigo_cpf_comprador, novo_cpf_comprador, novo_email, novo_nomeComprador, novo_cep, novo_rua, novo_bairro, novo_cidade, novo_estado):
    try:
        # recebe comprador
        with open ("comprador.txt", "r") as f:
            linhas = f.readlines()
        
        # buscar vendedor
        with open ("comprador.txt", "w") as f:
            encontrado = False

            for linha in linhas:
                partes = [item.strip() for item in linha.strip().split(",")]

                if len(partes) == 8:
                    cpf_comprador, email, nomeComprador, cep, rua, bairro, cidade, estado = partes
                    if cpf_comprador == antigo_cpf_comprador:
                        f.write (f"{novo_cpf_comprador}, {novo_email}, {novo_nomeComprador}, {novo_cep}, {novo_rua}, {novo_bairro}, {novo_cidade}, {novo_estado}\n")
                        encontrado = True
                        print (f"O(a) comprador(a) {novo_nomeComprador}, foi atualizado com sucesso.")
                    else:
                        f.write(linha)
                else:
                    f.write(linha)

            if not encontrado:
                print (f"Vendedor(a) {antigo_cpf_comprador} não foi encontrado(a). Encerrando ação.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")

# Deletar comprador
def deletar_comprador (apagar_cpf_comprador):
    try:
        # receber lista
        with open ("comprador.txt", "r") as f:
            linhas = f.readlines( )

        novas_linhas = []
        encontrado = False

        for linha in linhas:
            partes = [item.strip() for item in linha.strip().split(",")]

            if len(partes) > 0 and partes[0] == apagar_cpf_comprador:
                encontrado = True
                print(f"Comprador(a) {partes[2]}, de CPF {apagar_cpf_comprador}, foi deletado(a).")
            else:
                novas_linhas.append(linha)

        with open ("comprador.txt", "w") as f:
            f.writelines(novas_linhas)

        if not encontrado:
            print (f"O CPF {apagar_cpf_comprador} não foi encontrado.")

    except FileNotFoundError:
        print ("Arquivo não encontrado.")


##### MAIN #####

def main():

    #TESTES#

    # PRODUTOS #

    # Criar produtos
    # cod_produto:str || qtde_estoque:int || valor_unitario:float
    # criar tomada, cod 001, estoque 100, valor unitario 2.90
    criar_produto ("001", "Tomada", 100, 2.90)

    # criar lampada, cod 002, estoque 120, valor unitario 4.80
    criar_produto ("002", "lampada", 120, 4.80)

    # criar abajur, cod 003, estoque 150, valor unitario 10.20
    criar_produto ("003", "Abajur", 150, 10.20)
    ler_produto()

    # Atualizar produto
    # antigo_cod_produto:str || novo_cod_produto:str || novo_nome_produto:str || novo_qtde_estoque:int || novo_preco_unitario:float
    atualizar_produto ("001", "001", "Tomada Deluxe", "80", "4.60")
    ler_produto()

    # Apagar produto
    # cod_produto:str
    deletar_produto ("002")
    ler_produto()
    
    # VENDEDOR #
    print ("=" * 30)
    
    # Cadastrar novo vendedor
    # nomeVendedor:str || salarioFixo:str
    # vendedor Caio, salario 1800.00
    criar_vendedor ("Caio", 1800.00)

    # vendedor Karen, salario 2150.02
    criar_vendedor ("Karen", 2150.02)
    ler_vendedor()

    # Atualizar vendedores
    # antigo_nomeVendedor:str || novo_nomeVendedor:str || novo_salarioFixo:float
    atualizar_vendedor ("Karen", "Karen", 2150.02)
    ler_vendedor()

    # Remover vendedor
    # cod_vendedor
    deletar_vendedor (1)
    ler_vendedor()

    # Mostrar vendedores com apenas nome e código, ocultando salario e comissao
    ler_vendedor_atendendo()

    # COMPRADOR #
    print ("=" * 30)

    # Criar comprador
    # cpf_comprador:str || email:str || nome_comprador:str || cep || rua:str || bairro:str || cidade:str || estado:str
    criar_comprador ("10010010010", "daniel@email", "Daniel", 10100100, "Gaspar", "Coreu", "Belo Horizonte", "MG")
    criar_comprador ("20020020020", "shirley@email", "Shirley", 20200200, "Jose", "Coração Eucaristico", "BH", "Minas Gerais")
    criar_comprador ("30030030030", "luiz@email", "Luiz", 30300300, "Manuel", "Alphaville", "Campos", "RJ")
    ler_comprador()


    # Atualizar dados comprador
    # antigo_cpf_comprador: str || novo_cpf_comprador:str || novo_email:str || novo_nomeComprador:str || novo_cep || novo_rua:str || novo_bairro:str || novo_cidade:str || novo_estado:str
    atualizar_comprador("20020020020", "20020020020", "shirleyNovo@email", "Shirley Pessoa", 20300400, "Josue", "Eucaristico", "BH", "MG")
    ler_comprador()

    # Apagar dados comprador
    # apagar_cpf_comprador:str
    deletar_comprador ("20020020020")
    ler_comprador()

    # VENDAS #
    print ("=" * 30)

    # Adicionar produto ao carrinho
    # cpf_comprador_venda:str || cod_produto_venda:str || qtneDesejada_venda:int || cod_vendedor_venda:str
    adicionar_ao_carrinho ("10010010010", "001", 25, 1)
    adicionar_ao_carrinho ("10010010010", "002", 31, 1)
    ver_carrinho()

    # Fechar carrinho e salval dados nos arquivos txt
    finalizar_compra()
    ver_carrinho()

    ler_venda()

if __name__ ==  "__main__":
    main()