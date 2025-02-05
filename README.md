# **Projeto Django: CRUD de Produtos**

Este é um projeto Django simples que implementa operações CRUD (Create, Read, Update, Delete) para gerenciar produtos. O projeto inclui validações personalizadas para garantir que os dados sejam inseridos corretamente.

## Funcionalidades

- **Criar Produto**: Adicionar um novo produto com nome, descrição e preço.
- **Listar Produtos**: Visualizar todos os produtos cadastrados.
- **Editar Produto**: Atualizar os dados de um produto existente.
- **Excluir Produto**: Remover um produto do banco de dados.

## Validações

- O **nome do produto** deve ter pelo menos 3 caracteres.
- O **preço** deve ser maior que zero.

- ## Como Configurar o Projeto

Siga estas etapas para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

- **Python** 3.12 ou superior.
- **Django** 5.1 ou superior.

## Passos

1. **Crie um ambiente virtual:**

    ```bash
    python -m venv venv
    ```

2. **Ative o ambiente virtual:**

    - **No Windows:**

    ```bash
    venv\Scripts\activate
    ```

    - **No Linux/Mac:**

    ```bash
    source venv/bin/activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Execute as migrações:**

    ```bash
    python manage.py migrate
    ```

5. **Execute o servidor de desenvolvimento:**

    ```bash
    python manage.py runserver
    ```
    ## Acesse o Projeto

6. Abra o navegador e acesse: 

```bash
http://127.0.0.1:8000/products/
