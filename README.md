<div align="center">
  <a href="https://github.com/gabriel-anthoni/DIO-PyBank">
    <img src="https://capsule-render.vercel.app/api?type=soft&height=100&color=0D1117&text=DIO%20PyBank&fontColor=FFFFFF&fontSize=35&fontAlignY=60&animation=fadeIn" alt="DIO PyBank Banner" />
  </a>

  <br />

  <a href="https://github.com/gabriel-anthoni">
    <img src="https://img.shields.io/badge/gabriel--anthoni-000000?style=for-the-badge&logo=github" alt="GitHub Profile" />
  </a>

  <br /><br />

  ![Python Version](https://img.shields.io/badge/python-3.14.5-blue.svg)
  ![License](https://img.shields.io/badge/license-MIT-green.svg)
  ![Status](https://img.shields.io/badge/status-em_desenvolvimento-orange.svg)
</div>

<br />

<table>
  <tr>
    <td><img src="https://skillicons.dev/icons?i=python" width="150"/></td>
    <td><p align="center">O <strong>DIO PyBank</strong> é um sistema bancário em linha de comando (CLI) desenvolvido em Python que simula a operação de uma instituição financeira digital com arquitetura modularizada, validações estritas e controle temporal.</p></td>
  </tr>
</table>

## ⚙️ Funcionalidades e Regras de Negócio

### 1. Operações Bancárias
* **Depósito:** Aceita apenas valores positivos. Registra a data/hora exata da transação.
* **Saque:** Respeita o saldo disponível, o valor máximo por saque (ex: R$ 500,00) e o limite de saques diários.
* **Extrato:** Lista o histórico completo de movimentações e exibe o saldo final.

### 2. Gestão de Clientes e Contas
* **Cadastrar Usuário:** Solicita nome, data de nascimento, CPF e endereço. Não permite CPFs duplicados e exige idade mínima de 18 anos.
* **Cadastrar Conta Corrente:** Cria uma conta vinculada a um CPF já existente. Agência padrão é `"001"` e o número da conta é gerado sequencialmente (`1, 2, 3...`).
* **Exibir Contas:** Formatação em tabela exibindo número da conta, agência e dados do titular correspondente.

---

## 📂 Arquitetura de Diretórios

```text
dio_pybank/
├── main.py                 # Interface CLI, menu principal e controle de fluxo
├── utils/
│   ├── bank_operations.py  # Lógica central das transações (saque, depósito, extrato)
│   └── utils.py            # Funções utilitárias (formatação de erro, validações)
├── .gitignore
└── README.md               # Documentação do repositório
```

## 🔮 Próximos Passos

- [ ] Transição para Orientação a Objetos (POO) (Cliente, ContaCorrente, Historico, Transacao).<br/>
- [ ] Persistência de dados em banco de dados SQLite / PostgreSQL.<br/>
- [ ] Interface gráfica (GUI) com Tkinter/PyQt ou API REST com FastAPI.
