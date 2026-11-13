---
name: token-optimization
description: >-
  Workflows e técnicas validadas pela comunidade (baseado em bm629/agent-skills e alexgreensh/token-optimizer)
  para minimizar consumo de tokens, eliminar saídas verbosas e manter alta fidelidade de contexto.
  Use ao processar relatórios longos, executar lotes de ferramentas ou compactar sessões.
---

# Token Optimization for Autonomous Agents

Este padrão operacional baseia-se em metodologias consolidadas de engenharia de contexto open-source para manter agentes enxutos, rápidos e de baixo custo.

---

## 1. Princípios de Redução de Contexto (Context Pruning)

1. **Evitar Eco de Arquivos (No Code Echoing):**
   - Nunca reimprimir arquivos completos quando apenas linhas específicas forem modificadas.
   - Fornecer links diretos no formato `file:///caminho#Lxx-Lyy` e exibir apenas o bloco diff necessário.

2. **Supressão de Saídas Verbosas de Ferramentas:**
   - Em saídas de DRC/ERC com dezenas de itens, resumir por categorias e severidades em vez de despejar logs brutos.
   - Apontar o relatório em disco (`file:///.../drc_report.rpt`) para auditoria sob demanda.

3. **Operações em Lote (*Batch Invocation*):**
   - Agrupar múltiplos componentes, conexões e modificações em chamadas compostas para reduzir a quantidade de turnos e cabeçalhos repetidos da API.

---

## 2. Sobrevivência à Compactação (Compaction Resilience)

1. **Memória Fora da Janela (Externalized State):**
   - Estado permanente, decisões arquiteturais e tabelas de pinagem residem em arquivos Markdown rastreados (`PROJECT_MEMORY.md`), e não no histórico de mensagens.
2. **Recomendação de `/compact`:**
   - Quando o histórico da conversa crescer, acionar o `/compact` para liberar espaço na janela de contexto mantendo a memória persistente intacta.
