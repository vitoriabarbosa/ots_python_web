# 📝 Gerenciamento de Posts com Flask

## 📋 Introdução
> O projeto é um **Gerenciador de Posts**, que oferece uma interface web para adicionar, visualizar e gerenciar posts em um banco de dados SQLite.


## 🌟 Funcionalidades
- 📝 **Gerenciamento de Posts**: Criação e visualização de posts com título e texto.
- 🔒 **Sistema de Login**: Acesso restrito a funcionalidades de criação de posts.
- 🔄 **Controle de Sessões**: Manutenção de sessões de usuários logados.


### 🧱 Em construção:
- Deixar a interface mais "atraente"
- Personalizar os posts
- Deixar o sistema mais "funcional":
    - cadastro de usuário
    - edição e exclusão de posts
    - curtir / avaliar posts
    - pesquisar posts
- Implementar tipos de ordenação na visualização dos posts


## 🛠️ Implementação
- **Linguagem de Programação:** Python
- **Framework:** Flask
- **Banco de Dados:** SQLite
- **Templates:** Jinja2
- **Controle de Versão:** Git


## 🚀 Começando
### Pré-requisitos
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes do Python)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (opcional, mas recomendado)

### Instalação
1. #### Clone o repositório
    ```bash
     git clone https://github.com/vitoriabarbosa/ots_python_web.git
    ```

2. #### Navegar até o Diretório do Projeto:
    ```bash
     cd ots_python_web
    ```

3. #### Criar um Ambiente Virtual:
    ```bash
     python -m venv venv
    ```

4. #### Ativar o Ambiente Virtual:
    - No MacOS/Linux:
        ```bash
         source venv/bin/activate
        ```
    - No Windows:
        ```bash
         venv\Scripts\activate
        ```

5. #### Instalar as Dependências:
    ```bash
     pip install -r requirements.txt
    ```

6. #### Executar a Aplicação:
    ```bash
     flask run
    ```


### Observações
- O **Banco de Dados** é criado automaticamente ao rodar a aplicação. Portanto, não é necessário criar o banco manualmente ou executar scripts SQL adicionais para a configuração inicial.


## 📝 Licença
Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.