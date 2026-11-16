---
name: secret-sanitizer-and-privacy
description: >-
  Filtro ativo de sanitizacao de segredos, tokens de API, senhas e caminhos sensiveis.
  Use ao manipular arquivos de configuracao, logs e commits para impedir vazamento de credenciais privadas.
---

# Secret Sanitizer & Privacy Protection Guardrail

Esta skill estabelece a detecção ativa e interceptação de credenciais e chaves criptográficas em arquivos, logs e mensagens do assistente, impedindo a exposição involuntária de dados privados.

---

## 1. Padrões de Credenciais Monitorados

O agente deve interceptar e mascarar qualquer sequência que corresponda a:

1. **Tokens de Plataformas:**
   - GitHub Personal Access Tokens (`ghp_[A-Za-z0-9]{36}`, `github_pat_*`).
   - Chaves de API de IA (`sk-[A-Za-z0-9]{32,}`, `sk-ant-*`).
   - Chaves de Nuvem (AWS `AKIA[0-9A-Z]{16}`, GCP Service Accounts).
2. **Chaves Criptográficas:**
   - Blocos de texto contendo `-----BEGIN [A-Z ]*PRIVATE KEY-----`.
3. **Strings de Conexão com Credenciais em Texto Aberto:**
   - URLs no formato `protocolo://usuario:senha@servidor`.

---

## 2. Protocolo de Ação e Bloqueio

1. **Mascaramento em Tempo de Execução:**
   - Se uma credencial for exibida em resposta a um comando de diagnóstico ou leitura de log, substitua imediatamente os caracteres centrais por `[REDACTED_SECRET]`.
2. **Bloqueio de Commit:**
   - É expressamente proibido realizar `git commit` de arquivos que contenham chaves privadas, senhas ou tokens gravados em texto plano.
   - O commit deve ser abortado e o usuário instruído a mover a credencial para variáveis de ambiente locais ou arquivo `.env` protegido por `.gitignore`.
