# 📚 Sistema de Gerenciamento de Biblioteca

Projeto acadêmico desenvolvido para praticar o padrão de arquitetura **MVC (Model-View-Controller)**, com interface gráfica construída em **Qt (PySide6)** a partir do **Qt Designer**.

## 🎯 Objetivo

Aplicar na prática os conceitos de MVC, separando claramente:

- **Model**: entidades do domínio (`Livro`, `Usuario`, `Emprestimo`) e todas as regras de negócio.
- **View**: telas geradas a partir de arquivos `.ui` do Qt Designer, responsáveis apenas por exibição e captura de entrada.
- **Controller**: orquestra a comunicação entre View e Model, sem conter lógica de negócio nem de exibição.

## ⚙️ Funcionalidades

- Cadastro, listagem e remoção de livros
- Cadastro de usuários
- Registro de empréstimos, com validação de disponibilidade e limite por usuário
- Registro de devoluções, com cálculo de multa por atraso
- Listagem de empréstimos ativos e histórico
- Exclusão segura de livros/usuários (desativação automática quando há empréstimos ativos vinculados)

## 🧱 Estrutura do projeto

A branch `main` contém apenas as camadas **Model** e **Controller**, além da infraestrutura de dados — a camada **View** é implementada em branches específicas (veja a seção [Branches e Views](#-branches-e-views) abaixo).

```
biblioteca-mvc/
├── .vscode/
│   └── launch.json
├── controllers/
│   ├── book_controller.py
│   ├── loan_controller.py
│   └── user_controller.py
├── database/
│   ├── data.json
│   └── db.py
├── datamodels/
│   ├── enums.py
│   └── exceptions.py
├── models/
│   ├── book.py
│   ├── loan.py
│   └── user.py
├── .gitignore
└── README.md
```

- **`models/`** — entidades do domínio (`Book`, `Loan`, `User`) e todas as regras de negócio.
- **`controllers/`** — orquestram a comunicação entre a View (implementada em outra branch) e os Models, um controller por entidade.
- **`datamodels/`** — tipos de apoio ao domínio: `enums.py` (enumeradores usados pelos models, ex: status de empréstimo) e `exceptions.py` (exceções customizadas do domínio, ex: `LoanActiveError`).
- **`database/`** — camada de persistência (`db.py`) e o arquivo de dados (`data.json`), isolada da lógica de negócio dos Models.

## 🌿 Branches e Views

Este projeto testa múltiplas implementações de interface sobre o mesmo núcleo de Model/Controller. Por isso, a separação entre camadas também acontece a nível de branch:

| Branch | Conteúdo |
|---|---|
| `main` | Models, Controllers, exceptions/enums e camada de persistência (independente de interface) |
| `view-qt` | Interface gráfica desktop com Qt Designer/PySide6 (`views/`, arquivos `.ui`, `main.py`) |
| *(futuras branches)* | Outras implementações de View (ex: web, terminal, mobile) reutilizando os mesmos Models/Controllers |

Cada branch de View importa `models/` e `controllers/` da estrutura base e adiciona sua própria pasta `views/` (ou equivalente) e o `main.py` de entrada da aplicação, sem alterar Model/Controller — reforçando que essas camadas são independentes de interface.

## 🖥️ Requisitos

- Python 3.10+
- Dependências específicas de cada View ficam documentadas no README da respectiva branch (ex: `PySide6` na branch `view-qt`)

## 🚀 Instalação

```bash
git clone https://github.com/vitorhngo/Biblioteca-MVC.git
cd biblioteca-mvc
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Execução

A branch `main` não possui ponto de entrada (`main.py`) por si só, pois não contém nenhuma View. Para rodar a aplicação completa, faça checkout da branch de interface desejada:

```bash
git checkout view-qt
python main.py
```

## 🎨 Trabalhando com a interface Qt (branch `view-qt`)

Na branch `view-qt`, as telas são construídas com Qt Designer e convertidas em código Python. Após qualquer alteração visual no Designer, é necessário regenerar o arquivo correspondente:

```bash
pyside6-uic designer_files/tela_principal.ui -o views/ui_tela_principal.py
```

> ⚠️ Os arquivos `ui_*.py` são gerados automaticamente e não devem ser editados manualmente. Toda lógica de conexão de sinais/slots fica nas classes que herdam dessas interfaces.

## 🧩 Arquitetura MVC aplicada

| Camada | Localização | Responsabilidade | Não deve conter |
|---|---|---|---|
| **Model** | `models/` | Regras de negócio, validações, relacionamento entre entidades | Lógica de exibição ou de interface |
| **View** | branches específicas | Exibição de dados e captura de eventos do usuário | Regras de negócio |
| **Controller** | `controllers/` | Orquestração entre View e Model | Regras de negócio complexas |
| **Persistência** | `database/` | Leitura/escrita dos dados | Regras de negócio |
| **Apoio ao domínio** | `datamodels/` | Enums e exceptions usados pelos Models | Lógica de persistência ou exibição |

Um princípio seguido no projeto: se uma regra de negócio puder ser testada isoladamente, chamando apenas o Model (sem instanciar Controller ou View), ela está na camada correta.

## 🧪 Testes

```bash
python -m unittest discover tests
```

## 📄 Licença

Projeto de fins acadêmicos, sem licença específica definida.
