# Lista de Produtos (exercício acadêmico) ✅

Projeto simples para representar uma lista de produtos em Python. É um exercício **acadêmico** destinado ao aprendizado — não é um sistema para uso em produção.

---

## Funcionalidades 🔧

- **Inserir** produtos
- **Deletar** produtos
- **Alterar** produtos
- **Consultar** produtos
- **Persistência** em arquivo JSON (`db/products.json`)

---

## Como usar 💡

1. Certifique-se de ter Python 3.8+ instalado
2. Clone o repositório
3. Execute o script principal:

```bash
python index.py
```

> O projeto salva e lê os produtos em `db/products.json` automaticamente.

---

## Estrutura do projeto 📁

- `index.py` — entrada do programa
- `classes/Product.py` — classe que representa um produto
- `db/products.json` — arquivo onde os produtos são gravados em formato JSON