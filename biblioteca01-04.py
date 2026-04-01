
# Sistema de gestão de biblioteca

# Dicionário p/ armazenar os livros
catalogo = {}

# Dicionário p/ armazenar os empréstimos ativos
emprestimosAtivos = {}

# Lista p/ armazenar o histórico de transição
historico = []

# Função: Adicionar livro
def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com código {codigo} já existe")
        return False

    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True


adicionarLivro("L001", "Código Limpo", "Robert Martin", 2)