---
name: bom-lifecycle-auditor
description: >-
  Auditor de ciclo de vida e estoque de componentes na JLCPCB / LCSC utilizando banco local offline de 513k peças.
  Use ao selecionar componentes e antes de gerar a BOM para evitar custos extras de montagem ($3/linha) ou peças em falta.
---

# JLCPCB / LCSC BOM Lifecycle & Sourcing Auditor

Esta skill valida a disponibilidade de estoque, custo de montagem SMT e ciclo de vida dos componentes eletrônicos do projeto contra a base offline de dados da JLCPCB.

---

## 1. Regras de Seleção Econômica de Componentes

1. **Prioridade Mandatória: `Basic Parts`**
   - Na montagem SMT da JLCPCB, componentes classificados como **Basic Parts** estão permanentemente instalados nos alimentadores das máquinas *pick-and-place*.
   - **Vantagem:** Não há cobrança de taxa de substituição de alimentador ($3.00 por linha).
   - Componentes passivos comuns (resistores 0603/0805, capacitores 100nF, 10uF, diodos 1N4148, transistores 2N3904) DEVEM ser sempre selecionados como *Basic Parts*.
2. **Componentes `Extended Parts`:**
   - Usar somente quando não houver equivalente funcional em *Basic Parts* (ex: microcontroladores específicos, relés industriais, CIs de fonte chaveada).
3. **Checagem de Ciclo de Vida:**
   - Componentes marcados como `Discontinued`, `EOL` (End of Life) ou `NRND` (Not Recommended for New Designs) são **estritamente proibidos**.

---

## 2. Procedimento de Auditoria Programática

1. Consultar a peça via ferramenta `search_jlcpcb_parts` ou consulta direta ao banco SQLite local.
2. Inserir a propriedade `LCSC Part #` no símbolo correspondente com `set_schematic_component_property`.
3. Ao finalizar o circuito, exportar a lista de materiais padronizada via `export_bom` no formato:
   `Designator, Value, Package, LCSC Part #, Type`
