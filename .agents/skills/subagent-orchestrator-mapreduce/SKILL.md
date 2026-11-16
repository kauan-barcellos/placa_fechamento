---
name: subagent-orchestrator-mapreduce
description: >-
  Orquestracao de tarefas volumosas via subagentes efemeros e agregacao Map-Reduce.
  Use quando a tarefa exigir leitura de muitos arquivos, analise extensiva de logs ou pesquisas pesadas sem queimar contexto.
---

# Subagent Orchestration & Map-Reduce Context Architecture

Esta skill padroniza a delegação de tarefas de alta densidade de leitura para subagentes efêmeros leves, garantindo escalabilidade de processamento sem saturar a janela de contexto da conversa principal.

---

## 1. O Padrão Elephant & Goldfish (Map-Reduce)

```
[Coordenador Principal: "Elephant"] ──► Planejamento e Estruturação
                 │
                 ├──► Despacha Subagente 1 (flash): Analisa Lote A ──► Retorna Resumo Enxuto
                 ├──► Despacha Subagente 2 (flash): Analisa Lote B ──► Retorna Resumo Enxuto
                 │
                 ▼
[Consolidação Final: "Reduce"] ──► Síntese executiva limpa no chat principal
```

1. **Fase Map (Delegação Fatiada):**
   - Ao analisar mais de 5 arquivos extensos, múltiplos datasheets ou tabelas volumosas, não faça a leitura completa na sessão principal.
   - Dispare subagentes utilizando `invoke_subagent` com `Model: "flash"` ou `"flash_lite"`, definindo o escopo estrito de arquivos e a pergunta objetiva que ele deve responder.
2. **Fase Reduce (Retorno Sintetizado):**
   - O subagente deve devolver estritamente a resposta final ou tabela estruturada (máximo 5 a 10 linhas), sem despejar a trilha bruta de leituras.
   - O coordenador principal absorve apenas a conclusão consolidada, mantendo o histórico da conversa limpo e focado em decisões.

---

## 2. Critérios de Ativação

Ative a delegação para subagentes quando:
1. Uma busca exigir navegar por dezenas de pastas ou arquivos de log.
2. For necessário extrair pinagens de múltiplos PDFs ou datasheets de centenas de páginas.
3. For realizada uma varredura de vulnerabilidades ou code review em múltiplos repositórios.
