from .bank_operations import *
from datetime import datetime

# ============= CLIENTE =============
class Cliente():
    def __init__(self,nome:str):
        self.nome   = nome.title()

# ========== PESSOA FÍSICA ==========
class PessoaFisica(Cliente):
    def __init__(self,nome:str,data_nascimento:str,cpf:str,endereco:str):
        super().__init__(nome)
        self.data_nascimento = data_nascimento
        self.cpf             = cpf
        self.endereco        = endereco

# ============= EXTRATO =============
class Extrato():
    def __init__(self):
        self.extrato = {}
    
    def adicionar_extrato(self,extrato:dict):
        self.extrato.update(extrato)
    
    def adicionar_extrato_data(self,extrato:str,data:str):
        self.extrato[data].append(extrato)
    
    def ver_chaves(self):
        try:
            return self.extrato.keys()
        except IndexError:
            return []

# ============== CONTA ==============
class Conta():
    def __init__(self,numero_conta:int,cliente:Cliente, limite_saques: int = 3,limite: float = 500):
        self.saldo             = 0
        self.agencia           = "001"
        self.numero_conta      = numero_conta
        self.limite            = limite
        self.limite_saques     = limite_saques
        self.saques_realizados = 0
        self.data_ultimo_saque = datetime.today().date()
        self.cliente           = cliente
        self.extrato           = Extrato()
    
    def retornar_extrato(self):
        return self.extrato.extrato
    
    def aumentar_saques_realizados(self):
        self.saques_realizados += 1

    def alterar_data_ultimo_saque(self):
        self.data_ultimo_saque = datetime.today().date()
    
    def depositar(self,deposito:float):
        self.saldo += deposito
        extrato = buscar_data_transacao(self)
        if extrato[0]:
            self.extrato.adicionar_extrato_data(registrar_transacao(extrato[2],deposito,"Deposito"),extrato[1])
        else:
            self.extrato.adicionar_extrato({extrato[1]:[registrar_transacao(extrato[2],deposito,"Deposito")]})

    def sacar(self,saque:float):
        self.saldo -= saque
        extrato = buscar_data_transacao(self)
        if extrato[0]:
            self.extrato.adicionar_extrato_data(registrar_transacao(extrato[2],saque,"Saque"),extrato[1])
        else:
            self.extrato.adicionar_extrato({extrato[1]:[registrar_transacao(extrato[2],saque,"Saque")]})