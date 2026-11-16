---
name: hardware-adr
description: >-
  Gerador e mantenedor de Registros de Decisao de Arquitetura de Hardware (Hardware Architecture Decision Records).
  Use ao tomar decisoes criticas de topologia, escolha de componentes ou protecao para documentar justificativas tecnicas.
---

# Hardware Architecture Decision Records (Hardware ADR)

Esta skill padroniza o registro formal de decisões críticas de engenharia eletrônica em arquivos leves (`.agents/adr/ADR-xxx-titulo.md`), garantindo rastreabilidade histórica e contexto ininterrupto sem saturar a memória do modelo.

---

## 1. Estrutura Padrão de um Hardware ADR

Cada registro de decisão técnica deve seguir a estrutura:

```markdown
# ADR-001: [Título Conciso da Decisão Técnica]

- **Data:** AAAA-MM-DD
- **Status:** Proposto | Aprovado | Substituído por ADR-xxx
- **Componentes Afetados:** [ex: Bloco de Alimentação, MCU U1]

## 1. Contexto e Problema de Engenharia
[Descrição clara do desafio técnico, restrições elétricas, térmicas ou de custo.]

## 2. Alternativas Avaliadas
- **Opção A:** [Descrição, prós e contras técnicos/econômicos]
- **Opção B:** [Descrição, prós e contras técnicos/econômicos]

## 3. Decisão Escolhida e Justificativa
[Qual opção foi selecionada e o motivo técnico exato (ex: menor ruído para ADC, menor custo SMT, disponibilidade na JLCPCB).]

## 4. Consequências e Restrições de Layout
[Impactos diretos no esquemático, roteamento, dissipação térmica ou código de firmware.]
```

---

## 2. Quando Criar um Hardware ADR

Crie um ADR sempre que:
1. Definir a arquitetura da fonte de alimentação (LDO vs. Buck vs. Linear).
2. Escolher a família ou modelo de microcontrolador.
3. Definir a estratégia de proteção ESD / sobretensão externa.
4. Definir regras especiais de isolamento de alta tensão ou terras separados.
