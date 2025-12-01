
"""
Script educacional para simular o comportamento de um "keylogger" de forma
SEGURA, usando apenas input() em console.

Tudo o que o usuário digitar será gravado em um arquivo de log, até que ele
digite SAIR. Não há captura de teclas em segundo plano ou em outras janelas.
"""

import datetime
import os

ARQUIVO_LOG = "log_teclas.txt"


def registrar_entrada(texto: str) -> None:
    """Registra a entrada do usuário com carimbo de data/hora."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{timestamp}] {texto}\n"
    with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
        f.write(linha)


def simular_envio_email():
    """
    Função meramente ilustrativa para simular o envio do log por e-mail.
    Aqui, apenas informamos ao usuário que o "envio" seria realizado.

    Em um cenário real (ex.: para monitoramento autorizado), seria necessário
    configurar um servidor SMTP, credenciais e cuidados de segurança.
    """
    tamanho = 0
    if os.path.exists(ARQUIVO_LOG):
        tamanho = os.path.getsize(ARQUIVO_LOG)
    print(
        f"[SIMULACAO] Enviando arquivo '{ARQUIVO_LOG}' (tamanho: {tamanho} bytes)"
        " para um e-mail de teste..."
    )


def main():
    print("""
=== LAB EDUCACIONAL - KEYLOGGER SIMULADO ===

Tudo o que você digitar abaixo será gravado no arquivo 'log_teclas.txt'.
Digite SAIR para encerrar a simulação.
""")

    while True:
        texto = input("> ")
        if texto.strip().upper() == "SAIR":
            break
        if not texto.strip():
            continue
        registrar_entrada(texto)

    print("[+] Simulação encerrada. Verifique o arquivo log_teclas.txt.")

    # Pergunta se o usuário deseja simular envio por e-mail
    opcao = input("Deseja SIMULAR o envio do log por e-mail? (s/n) ").strip().lower()
    if opcao == "s":
        simular_envio_email()
    else:
        print("Envio não simulado.")


if __name__ == "__main__":
    main()
