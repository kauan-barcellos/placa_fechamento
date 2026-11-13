# Diretrizes Obrigatórias de Engenharia e DFM - Projeto placa_fechamento

Este documento define os padrões rigorosos de engenharia eletrônica, layout e Design for Manufacturing (DFM) voltados para fabricação padrão **JLCPCB (PCB de 2 camadas)**. Todas as etapas de projeto devem seguir estritamente estas diretrizes.

---

## 1. Regras de Design for Manufacturing (DFM - JLCPCB 2 Camadas)

- **Largura Mínima de Trilha (Trace Width):**
  - **Sinais gerais:** Mínimo de `0.15 mm` (6 mil).
  - **Alimentação e Potência:** Entre `0.5 mm` e `1.0 mm` (ou superior, dimensionado conforme corrente e cálculo de elevação de temperatura IPC-2152).
- **Espaçamento Mínimo (Clearance):**
  - Mínimo de `0.15 mm` (6 mil) entre cobre-cobre (trilha-trilha, trilha-pad, pad-pad).
- **Vias:**
  - **Furo mínimo de via (Drill):** `0.3 mm` (12 mil).
  - **Diâmetro mínimo do anel de cobre (Diameter / Pad):** `0.6 mm` (24 mil) — anel anular de no mínimo `0.15 mm`.

---

## 2. Organização e Net Classes no KiCad

É obrigatório o uso de **Net Classes** distintas e configuradas tanto no esquemático quanto no layout de PCB:
1. **`Default / Signals`:**
   - Trilha: `0.15 mm` a `0.20 mm`
   - Espaçamento (Clearance): `0.15 mm` a `0.20 mm`
   - Via: Furo `0.3 mm` / Diâmetro `0.6 mm`
2. **`Power` (VCC, 3V3, 5V, 12V, etc.):**
   - Trilha: `0.50 mm` a `1.00 mm` (conforme demanda de corrente)
   - Espaçamento (Clearance): `0.20 mm` a `0.25 mm`
   - Via: Furo `0.4 mm` / Diâmetro `0.8 mm` (ou múltiplas vias em paralelo para reduzir indutância/resistência)
3. **`Differential Pairs` (se aplicável - USB, RS485, etc.):**
   - Roteamento diferencial com impedância e espaçamento acoplado conforme especificação.

---

## 3. Diretrizes de Layout e Integridade de Sinal (SI/PI/EMC)

- **Capacitores de Desacoplamento:**
  - Capacitores de desacoplamento cerâmicos (ex: 100 nF) devem obrigatoriamente ser posicionados a **menos de 2 mm** dos pinos de alimentação dos CIs, com conexões de menor impedância possível (via direta ao plano ou trilha curta e grossa).
- **Plano de Terra (Ground Plane):**
  - Plano de terra contínuo em cobre (*GND Pour*) na camada inferior (**B.Cu**).
  - Evitar ao máximo cortar o plano inferior com trilhas longas para não interromper o caminho de retorno das correntes de alta frequência.
  - Se for necessário rotear na camada inferior, manter trilhas curtas e pontuais.
- **Stitching Vias (Vias de Costura de Terra):**
  - Distribuir stitching vias de GND em toda a borda da placa (espaçamento regular de ~3 a 5 mm).
  - Adicionar stitching vias adjacentes a componentes críticos, conectores e transições de sinal entre camadas.

---

## 4. Fluxo de Validação Obrigatório (Zero Erros)

O fluxo de trabalho deve ser incremental e rigidamente validado:
1. **Esquemático:**
   - Realizar o projeto em blocos lógicos claros, com conectores, desacoplamentos e anotações.
   - **Regra:** Após cada alteração no esquemático, rodar o **ERC (Electrical Rules Check)**. Zerar 100% dos erros e avisos antes de sincronizar com a PCB.
2. **Layout PCB:**
   - Definir contorno da placa, regras de design (DRC rules) conforme JLCPCB, posicionamento estratégico e roteamento.
   - **Regra:** Após cada alteração ou lote de roteamento na PCB, rodar o **DRC (Design Rules Check)**. Zerar **100%** das violações (clearance, furos, courtyards, disconnected nets) antes de considerar a etapa concluída.
