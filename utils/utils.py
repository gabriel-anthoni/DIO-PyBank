import os

# ======================= LIMPAR TERMINAL =======================
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")