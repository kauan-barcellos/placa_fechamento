---
name: kicad10-pcb-designer
description: >-
  Especialista em desenvolvimento de esquemáticos e layout de PCB no KiCad 10.0 integrado com o KiCad MCP Server.
  Use quando for adicionar componentes, conectar pinos, definir net classes, rotear trilhas,
  gerenciar planos de terra, executar validações ERC/DRC e preparar dados de fabricação para JLCPCB.
---

# KiCad 10.0 & JLCPCB Hardware Design Specialist

Este guia operacional orienta a execução precisa e econômica de tarefas no KiCad 10.0 utilizando as ferramentas do KiCad MCP Server.

---

## 1. Regras de Eficiência para o KiCad MCP (Economia de Tokens)

1. **Parâmetros Precisos na Primeira Chamada:**
   - Evitar chamadas exploratórias desnecessárias. Sempre consulte o arquivo de esquema da ferramenta em caso de dúvida antes da invocação.
   - Para abrir o projeto: `open_project(filename: "C:/Projetos_PCB/Novo_Projeto/placa_fechamento.kicad_pro")`.
   - Para salvar alterações: `save_board(force: true)`.

2. **Operações em Lote (*Batch Operations*):**
   - Prefira ferramentas em lote como `batch_add_components` ou `batch_add_and_connect` em vez de múltiplas chamadas individuais para economizar turnos e tokens.

3. **Verificação Imediata:**
   - Sempre rode `run_erc` após modificações no esquemático.
   - Sempre rode `run_drc` após modificações no layout de trilhas ou planos.

---

## 2. Seleção Inteligente de Componentes (JLCPCB PCBA)

1. **Busca na Base Local JLCPCB (513.000 componentes offline):**
   - Utilize `search_jlcpcb_parts` para consultar estoque e preços reais instantaneamente sem requisições HTTP externas lentas.
   - Priorize componentes da categoria **Basic Parts** da JLCPCB (`library_type: "Basic"`). Eles não geram taxa de troca de carretel ($3.00/linha) e estão sempre em estoque.
   - Sempre preencha a propriedade `LCSC Part #` no símbolo esquemático usando `set_schematic_component_property`.

2. **Componentes Incomuns / 3D Bundles:**
   - Para partes sem modelo oficial no KiCad (ex: conectores USB-C específicos, sensores raros), consulte `search_parts_registry` e use `download_registry_part` para importar o bundle com símbolo, pegada e modelo 3D.

3. **Desacoplamento e Conexão:**
   - Cada pino VDD/VCC do MCU ou CI deve ter um capacitor cerâmico de 100 nF a menos de 2.0 mm no layout.
   - Conecte o capacitor na topologia *flow-through*: a trilha de alimentação atinge o pad do capacitor antes de entrar no CI.

---

## 3. Autoroteamento de Sinais Secundários (FreeRouting)

1. **Roteamento Manual Prioritário:** Trilhas de alimentação grossas (0.5 mm a 1.0 mm), diodos TVS na entrada do conector, oscilador/cristal com guard ring e pares diferenciais (USB / RS485) são **sempre roteados manualmente** primeiro.
2. **Autoroteamento em Lote:** Para barramentos secundários densos de GPIOs, LEDs e linhas de controle não críticas, exporte a malha e acione o FreeRouting via `autoroute`.
3. **Pós-Autoroteamento:** Executar `refill_zones` e `run_drc` para certificar que nenhuma regra DFM de clearance (0.15 mm) foi violada.

---

## 4. Inspeção Visual Automática no Chat

- Após cada avanço estrutural no esquemático ou no layout, execute o script:
  `python .agents/scripts/generate_previews.py`
- Esse script gera arquivos vetoriais em `docs/previews/`:
  - [pcb_top.svg](file:///C:/Projetos_PCB/Novo_Projeto/docs/previews/pcb_top.svg)
  - [pcb_bottom.svg](file:///C:/Projetos_PCB/Novo_Projeto/docs/previews/pcb_bottom.svg)
  - [schematic.svg](file:///C:/Projetos_PCB/Novo_Projeto/docs/previews/schematic.svg)
- Forneça os links diretos para que o usuário possa inspecionar visualmente a placa sem abrir o KiCad.

---

## 3. Heurísticas Rápidas de Resolução de ERC no KiCad

- **Erro: "Pin connected to other pins, but not driven by any pin":**
  - Causa: Linhas de alimentação derivadas de conectores, fusíveis ou saídas de reguladores passivos.
  - Correção: Inserir símbolo `power:PWR_FLAG` conectado ao nó de alimentação.
- **Aviso: "Pin not connected":**
  - Causa: Pinos de CIs intencionalmente não utilizados (GPIOs sobrando, pinos NC).
  - Correção: Usar `add_no_connect` nas coordenadas exatas do pino.
- **Aviso: "Different nets connected to the same pin":**
  - Causa: Conexão acidental de dois rótulos com nomes diferentes no mesmo fio.
  - Correção: Renomear ou isolar os segmentos de fio.

---

## 4. Heurísticas Rápidas de Resolução de DRC no KiCad

- **Erro: "Clearance violation":**
  - Causa: Trilha ou via muito próxima de outro elemento condutor (< 0.15 mm).
  - Correção: Deslocar o segmento com `modify_trace` ou re-rotear em 45°.
- **Erro: "Unconnected items":**
  - Causa: Rede com airwire pendente (*ratsnest*).
  - Correção: Completar o roteamento com `route_trace` ou verificar preenchimento de zona com `refill_zones`.
- **Erro: "Courtyard overlap":**
  - Causa: Footprints muito próximos fisicamente (< 0.25 mm).
  - Correção: Reposicionar o componente com `move_component`.
- **Erro: "Annular width violation":**
  - Causa: Via com anel anular < 0.15 mm (diâmetro - furo < 0.30 mm).
  - Correção: Usar sempre via padrão de 0.60 mm de diâmetro para furo de 0.30 mm.

---

## 5. Procedimento de Finalização e Exportação

1. Executar `refill_zones` para preencher os planos de cobre `F.Cu` e `B.Cu`.
2. Executar `save_board(force: true)`.
3. Executar `run_drc` e assegurar 0 violações.
4. Exportar pacote JLCPCB para a pasta `fabrication/`:
   - `export_gerbers` -> `fabrication/gerbers/`
   - `export_drill` -> `fabrication/gerbers/`
   - `export_bom` -> `fabrication/assembly/bom.csv`
   - `export_pos` -> `fabrication/assembly/positions.csv`
   - `export_sch_pdf` -> `fabrication/pdf/schematic.pdf`
   - `export_pcb_pdf` -> `fabrication/pdf/pcb.pdf`
