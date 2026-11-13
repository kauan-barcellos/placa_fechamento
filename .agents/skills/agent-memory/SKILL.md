---
name: agent-memory
description: >-
  Padrão de arquitetura de memória persistente validado (baseado em sunnyvempati/agent-memory-skill e memodb-io/Acontext).
  Use para registrar decisões de hardware, pinouts, escolhas de componentes e preferências do usuário em arquivos de estado vivos.
---

# Agent Memory Architecture

Este guia implementa uma arquitetura de memória persistente baseada no sistema de arquivos para agentes de engenharia, eliminando o esquecimento de contexto entre sessões.

---

## 1. Camadas de Memória

1. **Memória de Trabalho (Working Memory - Curto Prazo):**
   - Contexto da conversa ativa, ferramentas imediatas em execução e raciocínio transitório.
2. **Memória Semântica (Semantic Memory - Longo Prazo):**
   - Diretrizes de DFM, regras de integridade de sinal e especificações do fabricante (`GEMINI.md`).
3. **Memória Episódica do Projeto (Episodic Project Memory):**
   - Arquivo vivo [PROJECT_MEMORY.md](file:///C:/Projetos_PCB/Novo_Projeto/PROJECT_MEMORY.md).
   - Registra o histórico das decisões técnicas, o microcontrolador selecionado, os pinos já ocupados, os códigos LCSC validados e as lições aprendidas em erros de DRC anteriores.

---

## 2. Protocolo de Sincronização

1. **Ao Iniciar a Sessão:** Ler `PROJECT_MEMORY.md` para carregar imediatamente o estado atual do circuito sem reprocessar histórico.
2. **Ao Concluir um Bloco Funcional:** Atualizar a tabela de pinos e componentes no `PROJECT_MEMORY.md`.
3. **Ao Corrigir um Erro de DRC/ERC:** Documentar a causa raiz e a solução na seção de Lições Aprendidas para evitar reincidência.
