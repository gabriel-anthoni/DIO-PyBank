<div align="center">
  <a href="https://github.com/gabriel-anthoni/DIO-PyBank">
    <img src="https://capsule-render.vercel.app/api?type=soft&height=100&color=0D1117&text=DIO%20PyBank&fontColor=FFFFFF&fontSize=35&fontAlignY=60&animation=fadeIn" alt="DIO PyBank Banner" />
  </a>

  <br />

  <a href="https://github.com/gabriel-anthoni">
    <img src="https://img.shields.io/badge/gabriel--anthoni-000000?style=for-the-badge&logo=github" alt="GitHub Profile" />
  </a>

  <br />

  ![Python Version](https://img.shields.io/badge/python-3.14.5-blue.svg)
  ![License](https://img.shields.io/badge/license-MIT-green.svg)
  ![Status](https://img.shields.io/badge/status-em_desenvolvimento-orange.svg)
</div>

<br />

<div align="center">
  <img src="https://skillicons.dev/icons?i=python" width="75" align="center">
  <img src="https://assets.dio.me/VTgUqMiPAIgvsFdSvgSnVAB5lrqnNxY_N8h8LknnQys/f:webp/q:80/w:120/L2Fzc2V0cy9kaW9tZS9sb2dvLWZ1bGwuc3Zn" align="center">
</div>

<p align="center"><br />O <strong>DIO PyBank</strong> é um sistema bancário em linha de comando (CLI) desenvolvido em Python que simula a operação de uma instituição financeira digital com arquitetura modularizada, validações estritas e controle temporal. Criado a partir dos desafios práticos do <strong>bootcamp Suzano - Python Developer</strong>, o projeto acompanhou toda a jornada de aprendizado do curso, desde os fundamentos básicos do Python e o uso de funções até a implementação avançada de Programação Orientada a Objetos (POO).</p>

<div align="center">
  <img src="https://assets.dio.me/B1CaLZqQ5j3QfIQg88bQ9P0J-MX7wJ-jARWwSGky6oI/f:webp/q:80/w:120/L2xhYl9wcm9qZWN0cy9iYWRnZXMvMDQ3Njk5MzQtZTc3YS00YjIwLWE3NzktMWU2ZjdhN2FiMWM4LnBuZw" width="65">
  <img src="https://assets.dio.me/tl4TKVWxfMHPyL8WrSmDM-6maqnDVupbc4LoFPoZX24/f:webp/q:80/w:120/L2xhYl9wcm9qZWN0cy9iYWRnZXMvZDlhMzVkNzEtOGQ2Yy00ODAyLTkyYjQtZDIzZWRiNjk0YmMxLnBuZw" width="65">
  <img src="https://assets.dio.me/jC6gAPAb_jomLKaFXcvfM35RdKFNIQPJ9i5TJv1mA1g/f:webp/q:80/w:120/L2xhYl9wcm9qZWN0cy9iYWRnZXMvZGEwNGFmZGYtNDk3Mi00ZjQ4LWFlYzUtYjU0ZjUyN2Q5OGNkLnBuZw" width="65">
</div>

<!-----
<div>
  <img src="https://skillicons.dev/icons?i=python" width="105" align="left"/>
  <p align="center"><br />O <strong>DIO PyBank</strong> é um sistema bancário em linha de comando (CLI) desenvolvido em Python que simula a operação de uma instituição financeira digital com arquitetura modularizada, validações estritas e controle temporal.</p>
</div>


<br />
<br />

<img src="https://assets.dio.me/VTgUqMiPAIgvsFdSvgSnVAB5lrqnNxY_N8h8LknnQys/f:webp/q:80/w:120/L2Fzc2V0cy9kaW9tZS9sb2dvLWZ1bGwuc3Zn" align="left">

<p align="center">Criado a partir dos desafios práticos do bootcamp Suzano - Python Developer, o projeto acompanhou toda a jornada de aprendizado do curso, desde os fundamentos básicos do Python e o uso de funções até a implementação avançada de Programação Orientada a Objetos (POO).</p>

<div align="center">
  <img src="https://assets.dio.me/B1CaLZqQ5j3QfIQg88bQ9P0J-MX7wJ-jARWwSGky6oI/f:webp/q:80/w:120/L2xhYl9wcm9qZWN0cy9iYWRnZXMvMDQ3Njk5MzQtZTc3YS00YjIwLWE3NzktMWU2ZjdhN2FiMWM4LnBuZw" width="65">
  <img src="https://assets.dio.me/tl4TKVWxfMHPyL8WrSmDM-6maqnDVupbc4LoFPoZX24/f:webp/q:80/w:120/L2xhYl9wcm9qZWN0cy9iYWRnZXMvZDlhMzVkNzEtOGQ2Yy00ODAyLTkyYjQtZDIzZWRiNjk0YmMxLnBuZw" width="65">
  <img src="https://assets.dio.me/jC6gAPAb_jomLKaFXcvfM35RdKFNIQPJ9i5TJv1mA1g/f:webp/q:80/w:120/L2xhYl9wcm9qZWN0cy9iYWRnZXMvZGEwNGFmZGYtNDk3Mi00ZjQ4LWFlYzUtYjU0ZjUyN2Q5OGNkLnBuZw" width="65">
</div>
--->

<br />

## ⚙️ Funcionalidades e Regras de Negócio
### 1. Operações Bancárias
* **Identificação por Conta:** Para realizar qualquer operação (Depósito, Saque ou Extrato), o sistema solicita primeiro o Número da Conta para vincular a transação à conta correta.
* **Depósito:** Solicita o número da conta e o valor. Aceita apenas valores positivos e registra a data/hora exata da transação no extrato específico daquela conta.
* **Saque:** Solicita o número da conta e o valor. Valida o saldo disponível da conta, o limite por operação (ex: R$ 500,00) e o limite de saques diários daquela conta.
* **Extrato:** Solicita o número da conta e exibe o histórico completo de movimentações e o saldo final atualizado correspondente a ela.

### 2. Gestão de Clientes e Contas
* **Cadastrar Usuário:** Solicita nome, data de nascimento, CPF e endereço. Não permite CPFs duplicados e exige idade mínima de 18 anos.
* **Cadastrar Conta Corrente:** Cria uma conta vinculada a um CPF já cadastrado. A agência padrão é `"001"` e o número da conta é gerado de forma sequencial automática (`1, 2, 3...`).
* **Exibir Contas:** Apresenta uma tabela estruturada com o número da conta, agência e os dados do titular associado.

---

## 📂 Arquitetura de Diretórios

```text
dio_pybank/
├── main.py                 # Interface CLI, menu principal e controle de fluxo
├── utils/
│   ├── bank_operations.py  # Lógica central das transações (saque, depósito, extrato)
│   ├── models.py           # Definição das classes da POO (Cliente, PessoaFisica, Conta, Extrato)
│   └── utils.py            # Funções utilitárias (formatação de erro, validações)
├── .gitignore
├── LICENSE                 # Termos da Licença MIT
└── README.md               # Documentação do repositório
```

## 🔮 Próximos Passos

- [x] Transição para Orientação a Objetos (POO) (Cliente, PessoaFisica, Extrato, Conta).<br/>
- [ ] Persistência de dados em banco de dados SQLite / PostgreSQL.<br/>
- [ ] Interface gráfica (GUI) com Tkinter/PyQt ou API REST com FastAPI.
