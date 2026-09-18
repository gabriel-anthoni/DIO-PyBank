<div align="center">
  <a href="https://github.com/gabriel-anthoni">
    <img src="https://capsule-render.vercel.app/api?type=soft&height=180&color=0D1117&text=DIO%20PyBank&fontColor=38BDF8&fontSize=42&stroke=38BDF8&strokeWidth=1" width="100%" alt="Banner DIO PyBank" />
  </a>

  <h3>💻 Sistema Bancário CLI com POO e Arquitetura Modular em Python</h3>

  <p>
    <a href="https://github.com/gabriel-anthoni"><img src="https://img.shields.io/badge/Desenvolvedor-Gabriel%20Anthoni-181717?style=flat-square&logo=github&logoColor=white" alt="Desenvolvedor Gabriel Anthoni" /></a>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python Version" />
    <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-2ea44f?style=flat-square" alt="Status Concluído" />
    <img src="https://img.shields.io/badge/Licen%C3%A7a-MIT-green?style=flat-square" alt="Licença MIT" />
    <img src="https://img.shields.io/badge/Bootcamp-Suzano%20Python-orange?style=flat-square" alt="Bootcamp Suzano Python" />
  </p>

  <br />

  <p align="center">
      <img src="https://skillicons.dev/icons?i=python" alt="Python Logo" width="90" />
  </p>
</div>

---

## 📌 Sobre o Projeto

O **DIO PyBank** é um sistema bancário em linha de comando (CLI) que simula as operações fundamentais de uma instituição financeira digital. O sistema conta com arquitetura modularizada, validações estritas de dados e controle temporal de transações.

Desenvolvido durante o bootcamp **Suzano - Python Developer** na plataforma **DIO (Digital Innovation One)**, o repositório reflete a evolução prática do aprendizado, passando dos conceitos fundamentais da linguagem (estruturas de repetição, listas e dicionários) até abstrações avançadas utilizando **Programação Orientada a Objetos (POO)**.

---

## ✨ Funcionalidades e Regras de Negócio

### 🏦 1. Operações Bancárias
| Operação | Descrição e Regras |
| :--- | :--- |
| **Identificação** | Exige o número da conta para vincular a transação à conta correta do cliente. |
| **Depósito** | Registra entradas financeiras. Aceita apenas valores positivos e armazena a data/hora exata do evento no histórico. |
| **Saque** | Valida o saldo disponível, o limite financeiro por operação (ex: R$ 500,00) e o número de saques diários permitidos. |
| **Extrato** | Apresenta o histórico cronológico detalhado de todas as movimentações e exibe o saldo atualizado. |

### 👥 2. Gestão de Clientes e Contas

#### 👤 Cadastrar Usuário
* 📌 **Entradas:** `Nome` • `Data de Nascimento` • `CPF` • `Endereço`
* 🛡️ **Regra:** Valida maioridade (18+ anos) e impede CPFs duplicados.

#### 💳 Cadastrar Conta Corrente
* 📌 **Requisito:** Vínculo obrigatório a um `CPF` já existente.
* ⚙️ **Regra:** Agência fixa em `001` com incremento automático do número da conta (`1, 2, 3...`).

#### 📋 Exibir Contas
* 📊 **Saída:** Relatório estruturado com número da conta, agência e titular associado.

---

## 🛠️ Tecnologias e Conceitos Utilizados

| Domínio | Recurso / Tecnologia | Aplicação Prática |
| :--- | :--- | :--- |
| **Linguagem Base** | `Python 3.10+` | Construção do fluxo principal e CLI interativa |
| **Paradigma** | `Orientação a Objetos` | Abstração de entidades (`Cliente`, `PessoaFisica`, `Conta`, `Historico`) |
| **Arquitetura** | `Modular Clean Code` | Separação em camadas para modelos, utilitários e regras de negócio |
| **Auditoria** | `Módulo datetime` | Rastreamento temporal exato de cada movimentação financeira |

---

## 📂 Arquitetura do Projeto

```text
dio_pybank/
├── main.py                 # Interface CLI, menu interativo e controle do fluxo
├── utils/
│   ├── bank_operations.py  # Regras de negócio das transações (saque, depósito, extrato)
│   ├── models.py           # Modelagem de classes (Cliente, PessoaFisica, Conta, Extrato)
│   └── utils.py            # Funções auxiliares (validações, formatações e mensagens)
├── .gitignore
├── LICENSE                 # Licença MIT
└── README.md               # Documentação do repositório
