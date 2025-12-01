
"""
Script educacional para simular o comportamento de um "ransomware" em um
ambiente CONTROLADO.

Ele APENAS criptografa e descriptografa arquivos .txt dentro da pasta
'arquivos_teste', utilizando uma chave simétrica armazenada em 'chave.key'.

Não use este código em máquinas de terceiros nem em ambientes de produção.
"""

import os
from cryptography.fernet import Fernet

PASTA_ARQUIVOS = "arquivos_teste"
ARQUIVO_CHAVE = "chave.key"
ARQUIVO_MENSAGEM = "MENSAGEM_RESGATE.txt"


def gerar_chave():
    """Gera uma chave simétrica e salva em disco (chave.key)."""
    if os.path.exists(ARQUIVO_CHAVE):
        print(f"[!] A chave '{ARQUIVO_CHAVE}' já existe. Pulando geração.")
        return

    key = Fernet.generate_key()
    with open(ARQUIVO_CHAVE, "wb") as f:
        f.write(key)
    print(f"[+] Chave gerada e salva em '{ARQUIVO_CHAVE}'.")


def carregar_chave():
    """Carrega a chave simétrica a partir do arquivo chave.key."""
    if not os.path.exists(ARQUIVO_CHAVE):
        raise FileNotFoundError(
            f"Arquivo de chave '{ARQUIVO_CHAVE}' não encontrado. Gere a chave primeiro."
        )
    with open(ARQUIVO_CHAVE, "rb") as f:
        return f.read()


def listar_arquivos_txt():
    """Lista apenas arquivos .txt dentro de PASTA_ARQUIVOS."""
    if not os.path.exists(PASTA_ARQUIVOS):
        os.makedirs(PASTA_ARQUIVOS, exist_ok=True)
    arquivos = []
    for nome in os.listdir(PASTA_ARQUIVOS):
        if nome.endswith(".txt"):
            arquivos.append(os.path.join(PASTA_ARQUIVOS, nome))
    return arquivos


def criptografar_arquivos():
    """Criptografa todos os .txt da pasta arquivos_teste, gerando .enc."""
    key = carregar_chave()
    fernet = Fernet(key)

    arquivos = listar_arquivos_txt()
    if not arquivos:
        print("[!] Nenhum arquivo .txt encontrado em 'arquivos_teste'.")
        return

    for caminho in arquivos:
        with open(caminho, "rb") as f:
            dados = f.read()
        dados_cripto = fernet.encrypt(dados)

        caminho_cripto = caminho + ".enc"
        with open(caminho_cripto, "wb") as f:
            f.write(dados_cripto)

        print(f"[+] Arquivo criptografado: {caminho_cripto}")

    # Gera mensagem de "resgate" APENAS para fins educacionais
    with open(ARQUIVO_MENSAGEM, "w", encoding="utf-8") as f:
        f.write(
            "SEUS ARQUIVOS DE TESTE FORAM CRIPTOGRAFADOS (SIMULACAO).\n"
            "Este é um laboratório educacional para entender o funcionamento "
            "básico de um ransomware.\n\n"
            "Para restaurar os arquivos, execute a opção de DESCRIPTOGRAFIA "
            "com a mesma chave.\n"
        )
    print(f"[+] Mensagem de 'resgate' gerada em '{ARQUIVO_MENSAGEM}'.")


def descriptografar_arquivos():
    """Descriptografa todos os arquivos .enc na pasta arquivos_teste."""
    key = carregar_chave()
    fernet = Fernet(key)

    if not os.path.exists(PASTA_ARQUIVOS):
        print("[!] Pasta de arquivos de teste não encontrada.")
        return

    arquivos_enc = [
        os.path.join(PASTA_ARQUIVOS, nome)
        for nome in os.listdir(PASTA_ARQUIVOS)
        if nome.endswith(".enc")
    ]

    if not arquivos_enc:
        print("[!] Nenhum arquivo .enc encontrado para descriptografar.")
        return

    for caminho in arquivos_enc:
        with open(caminho, "rb") as f:
            dados_cripto = f.read()
        try:
            dados = fernet.decrypt(dados_cripto)
        except Exception as e:
            print(f"[!] Falha ao descriptografar {caminho}: {e}")
            continue

        # Remove a extensão .enc para restaurar o nome original
        caminho_original = caminho[:-4]
        with open(caminho_original, "wb") as f:
            f.write(dados)

        print(f"[+] Arquivo restaurado: {caminho_original}")


def menu():
    print("""
=== LAB EDUCACIONAL - RANSOMWARE SIMULADO ===
Pasta de arquivos de teste: arquivos_teste

[1] Gerar chave
[2] Criptografar arquivos .txt
[3] Descriptografar arquivos .enc
[0] Sair
""")

    opcao = input("Escolha uma opção: ").strip()
    if opcao == "1":
        gerar_chave()
    elif opcao == "2":
        criptografar_arquivos()
    elif opcao == "3":
        descriptografar_arquivos()
    elif opcao == "0":
        print("Saindo...")
    else:
        print("[!] Opção inválida.")


if __name__ == "__main__":
    # Garante que a pasta de arquivos de teste exista
    os.makedirs(PASTA_ARQUIVOS, exist_ok=True)
    menu()
