---
name: project-architect
description: >-
  Engenharia guiada por especificacao e planejamento arquitetural formal (Spec-Driven Development).
  Use antes de iniciar qualquer funcionalidade ou projeto complexo para congelar requisitos no SPEC.md e evitar retrabalho.
---

# Project Architect & Spec-Driven Development

Esta skill estabelece a metodologia de planejamento formal antes da codificação ou edição de arquivos, garantindo que requisitos, contratos de interface e critérios de aceite estejam completamente definidos.

---

## 1. O Protocolo das 3 Fases

Diante de uma tarefa complexa ou novo projeto, o agente DEVE executar as 3 fases sequenciais:

```
[Fase 1: Discovery] ──► [Fase 2: Especificação (SPEC.md)] ──► [Fase 3: Plano de Execução]
```

### Fase 1: Discovery (Fronteiras e Restrições)
- Identificar as entradas, saídas, dependências de hardware/software e restrições operacionais.
- Em vez de perguntas abertas genéricas, apresentar perguntas objetivas com opções técnicas recomendadas.

### Fase 2: Especificação Formal (`SPEC.md`)
- Consolidar a arquitetura em um arquivo `SPEC.md` contendo:
  - **Objetivo Geral:** 1 a 2 parágrafos objetivos.
  - **Requisitos Funcionais:** Lista numerada de comportamentos obrigatórios.
  - **Requisitos Não-Funcionais:** Latência, consumo, limites térmicos, restrições DFM/físicas.
  - **Contratos de Interface:** Pinagem, assinaturas de funções, esquemas JSON ou protocolos de comunicação.
  - **Critérios de Aceite (Definition of Done):** Condições mensuráveis para declarar a entrega finalizada.

### Fase 3: Plano de Execução em Fases Independentes
- Decompor a implementação em blocos atômicos que possam ser testados e validados isoladamente.
- Obter a validação do usuário antes de iniciar a primeira etapa de modificação.
