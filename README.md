# Malware Simulado em Python: Ransomware & Keylogger

Este repositório documenta um laboratório prático em Python para **simular** o funcionamento de dois tipos de malware em ambiente 100% controlado e com fins educacionais:

- **Ransomware simulado** – criptografa e descriptografa arquivos de teste;  
- **Keylogger simulado** – registra entradas digitadas em console.

> **Aviso importante:**  
> Este projeto é **exclusivamente educacional**. Não utilize nenhum código aqui apresentado em máquinas de terceiros, em ambientes de produção ou sem autorização explícita.

---

## 1. Entendendo o Projeto

Este projeto foi desenvolvido como parte de um desafio da DIO, com foco em:

- Compreender o funcionamento prático de **ransomware** e **keylogger**;  
- Programar scripts simples em Python que simulam comportamentos maliciosos em **ambiente controlado**;  
- Refletir sobre **estratégias de defesa e prevenção** contra malwares;  
- Utilizar o **GitHub como portfólio técnico**, documentando a jornada de aprendizado.

---

## 2. Estrutura do Repositório

    .
    ├── ransomware_simulado.py     # Script de ransomware simulado
    ├── keylogger_simulado.py      # Script de keylogger simulado
    └── README.md                  # Este arquivo

---

## 3. Ransomware Simulado (ransomware_simulado.py)

### 3.1 Objetivo

Simular o funcionamento básico de um **ransomware**, mostrando:

- Geração de uma **chave simétrica**;  
- **Criptografia** de arquivos `.txt` de teste;  
- **Descriptografia** dos arquivos usando a mesma chave;  
- Criação de uma **mensagem de “resgate”** com caráter totalmente didático.

### 3.2 Funcionamento

- A pasta de trabalho do script é `arquivos_teste/`;  
- Apenas arquivos com extensão `.txt` são processados;  
- Ao criptografar:
  - Os arquivos `.txt` viram arquivos `.txt.enc`;  
  - É criado o arquivo `MENSAGEM_RESGATE.txt` explicando que se trata de um **laboratório educacional**;  
- Ao descriptografar:
  - Os arquivos `.enc` são restaurados para o conteúdo original.

### 3.3 Código Utilizado

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

---

## 4. Keylogger Simulado (keylogger_simulado.py)

### 4.1 Objetivo

Simular um **keylogger** de forma segura, registrando o que for digitado **apenas no console** em um arquivo de log.

> Não há captura de teclado em background, nem fora do terminal.  
> Tudo acontece com o usuário ciente, como parte do laboratório.

### 4.2 Funcionamento

- Tudo o que é digitado no prompt (`>`) é salvo em `log_teclas.txt`;  
- Cada linha recebe um carimbo de **data e hora**;  
- A simulação termina quando o usuário digita `SAIR`;  
- Ao final, o script oferece a opção de **“simular” o envio do log por e-mail**, apenas exibindo uma mensagem (sem envio real).

### 4.3 Código Utilizado

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

---

## 5. Execução – Requisitos e Resumo de Comandos

### 5.1 Pré-requisitos

- Python 3.x;  
- Biblioteca `cryptography`:

    pip install cryptography

### 5.2 Comandos de execução

- **Ransomware simulado:**

    python ransomware_simulado.py

- **Keylogger simulado:**

    python keylogger_simulado.py

---

## 6. Reflexão sobre Defesa & Prevenção

Ao observar o funcionamento desses malwares simulados, fica mais fácil entender como ataques reais podem causar danos.

### 6.1 Riscos observados

- **Ransomware**
  - Sequestro de arquivos importantes;  
  - Dependência de backups para recuperação;  
  - Impacto crítico em ambientes sem política de backup ou segmentação adequada.

- **Keylogger**
  - Captura de credenciais e dados sensíveis;  
  - Possibilidade de comprometimento de contas, sistemas e informações pessoais.

### 6.2 Medidas de mitigação

Algumas estratégias de defesa:

- **Antivírus / EDR**
  - Detecção de assinaturas e, principalmente, de comportamentos suspeitos (criptografia em massa, monitoramento de teclado, etc.);  

- **Firewall**
  - Bloqueio de conexões de saída suspeitas (exfiltração de dados, envio de logs);  

- **Sandboxing**
  - Execução de anexos e arquivos desconhecidos em ambientes isolados;  

- **Backup e Recuperação**
  - Rotinas de backup frequentes e testadas periodicamente;  

- **Conscientização do Usuário**
  - Cuidado com phishing, anexos desconhecidos e engenharia social;  
  - Não executar scripts ou binários de origem duvidosa.

---

## 7. Principais Aprendizados

Com este projeto foi possível:

- Entender, na prática, o funcionamento básico de:
  - um **ransomware** (criptografia de arquivos);  
  - um **keylogger** (registro de entradas);  

- Programar scripts simples em **Python** para simular cenários reais em um laboratório controlado;  

- Perceber como esses malwares exploram tanto falhas técnicas quanto **brechas humanas**;  

- Exercitar a **documentação técnica** de forma clara e estruturada;  

- Utilizar o **GitHub** como portfólio técnico, registrando scripts, evidências e conclusões.

---
