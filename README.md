# Sistema de CRUD de Veículos com Sockets
Este repositório contém um projeto de exemplo utilizando **Pyro5** para comunicação remota entre um servidor e um cliente. O objetivo é demonstrar a criação de um sistema distribuído simples onde o servidor expõe métodos que podem ser acessados remotamente pelo cliente.

---

## 📋 Pré-requisitos

Antes de começar, você precisa ter o seguinte instalado:

- **Python 3.8+**
- **Pyro5** (Instalável via `pip install Pyro5`)

---

## 🚀 Como Executar

### 1️ - Instale as dependências

```bash
    ## No diretório raiz do projeto, execute:
    pip install -r requirements.txt
```

### 2 - Inicie o name server

```bash
    ## No diretório raiz do projeto, execute:
    python -m Pyro5.nameserver
```

### 3 - Inicie o servidor

```bash
    ## No diretório raiz do projeto, execute:
    python src/server.py
```

### 4 - Inicie o cliente

```bash
    ## No diretório raiz do projeto, execute:
    python src/client.py
```

