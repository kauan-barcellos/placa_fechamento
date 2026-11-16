# Regras DFM e Especificações de Layout KiCad 10.0 (JLCPCB 2 Camadas)

Este documento define os parâmetros numéricos e regras obrigatórias de **Design for Manufacturing (DFM)** para fabricação na **JLCPCB (2 Camadas, 1 oz / 35 µm Cu, FR-4 1.6 mm)**.

---

## 1. Tabela DFM JLCPCB (Safe Production Values)

Todas as regras de design no KiCad devem adotar os **Valores Recomendados**.

| Parâmetro Físico | Limite JLCPCB | Valor Recomendado | Observações |
| :--- | :--- | :--- | :--- |
| **Largura mínima de trilha (Sinais)** | 0.10 mm (4 mil) | **0.15 mm a 0.20 mm** | Maximiza rendimento de corrosão química. |
| **Largura de trilha (Alimentação lógica < 0.5A)** | 0.10 mm | **0.50 mm** (20 mil) | Baixa impedância e queda de tensão controlada. |
| **Largura de trilha (Potência 1.0A a 2.0A)** | - | **1.00 mm a 1.50 mm** | Conforme IPC-2152 ($\Delta T \le 10^\circ\text{C}$). |
| **Espaçamento mínimo (Clearance Cu-Cu)** | 0.10 mm (4 mil) | **0.15 mm** / **0.20 mm** | Trilha-trilha, trilha-pad e pad-pad. |
| **Espaçamento Cobre à Borda (Board Edge)** | 0.20 mm | **0.40 mm a 0.50 mm** | Previne exposição de cobre no corte/V-cut. |
| **Furo mínimo de Via (Drill Size)** | 0.15 mm | **0.30 mm** (12 mil) | Broca padrão sem custo adicional de furação fina. |
| **Diâmetro do Pad da Via (Diameter)** | Drill + 0.26 mm | **0.60 mm** (24 mil) | Garante anel anular de 0.15 mm. |
| **Anel Anular Mínimo (Annular Ring)** | 0.13 mm | **0.15 mm** | Evita rompimento (*breakout*) por tolerância. |
| **Via de Potência (Individual)** | - | **Drill 0.40 mm / Pad 0.80 mm** | Suporta ~1.5A contínuos por via; usar em paralelo. |
| **Barragem de Máscara (Soldermask Dam)** | 0.08 mm (3.1 mil) | **0.10 mm** | Mínimo entre pads vizinhos para evitar pontes. |
| **Abertura de Máscara (Mask Clearance)** | 0.00 mm | **0.05 mm** (2 mil) | Expansão de máscara ao redor dos pads. |
| **Largura de traço de Silkscreen** | 0.15 mm (6 mil) | **0.15 mm a 0.20 mm** | Garante nitidez e legibilidade na serigrafia. |
| **Altura mínima de texto de Silkscreen** | 0.80 mm (32 mil) | **1.00 mm a 1.20 mm** | Leitura clara a olho nu e câmeras AOI. |
| **Distância Silkscreen para Pad de Solda** | 0.15 mm | **0.20 mm** | Silkscreen NUNCA pode sobrepor cobre estanhado. |

---

## 2. Configurações Programáticas KiCad MCP

### 2.1. Regras Gerais de Design (`set_design_rules`)
```json
{
  "clearance": 0.15,
  "trackWidth": 0.20,
  "minTrackWidth": 0.15,
  "viaDrill": 0.30,
  "minViaDrill": 0.30,
  "viaDiameter": 0.60,
  "minViaDiameter": 0.60,
  "minHoleDiameter": 0.30,
  "courtyardClearance": 0.25,
  "requireCourtyard": true
}
```

### 2.2. Definições de Net Classes (`create_netclass`)
| Nome da Classe | Trilha (`traceWidth`) | Espaçamento (`clearance`) | Furo Via (`viaDrill`) | Diâmetro Via (`viaDiameter`) | Aplicação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`Default`** | 0.20 mm | 0.15 mm | 0.30 mm | 0.60 mm | Sinais digitais gerais, GPIOs, LEDs, barramentos de controle. |
| **`Power_Low`** | 0.50 mm | 0.20 mm | 0.30 mm | 0.60 mm | Trilhas de alimentação local (+3V3, +5V, VDD) $\le 500\text{ mA}$. |
| **`Power_High`** | 1.00 mm | 0.25 mm | 0.40 mm | 0.80 mm | Entradas principais de alimentação, barramento de potência, relés. |
| **`Diff_USB`** | 0.25 mm | 0.18 mm | 0.30 mm | 0.60 mm | Par diferencial USB D+/D- ($Z_{diff} \approx 90\,\Omega$). |
| **`Diff_RS485`** | 0.30 mm | 0.25 mm | 0.30 mm | 0.60 mm | Par diferencial industrial A/B ($Z_{diff} \approx 120\,\Omega$). |
| **`Analog`** | 0.25 mm | 0.25 mm | 0.30 mm | 0.60 mm | Sinais analógicos de sensores e referências de ADC (baixo ruído). |

---

## 3. Diretrizes Críticas de Layout e EMC

1. **Plano de Terra Contínuo em `B.Cu`:**
   - A camada inferior (`B.Cu`) deve ser mantida como plano de terra sólido ininterrupto (`net: "GND"`).
   - Proibido fendas (*slot antennas*): se for estritamente necessário rotear em `B.Cu`, utilize segmentos curtos e retorne imediatamente para `F.Cu`.
2. **Capacitores de Desacoplamento:**
   - Distância máxima de **2.0 mm** dos pinos VDD/VCC do CI com conexão *flow-through* (a alimentação toca o pad do capacitor antes do pino do CI).
3. **Proteção ESD e TVS:**
   - Diodos TVS colados no conector de entrada com roteamento *in-line* obrigatório (proibido criar ramificações/stubs) e no mínimo 2 vias de terra.
4. **Geometria de Trilhas:**
   - Cantos a **45°**; cantos vivos a 90° são proibidos. Regra 3W aplicada a linhas de clock, PWM e SPI.
5. **Fiducials e Montagem (DFA):**
   - 3 fiducials globais (cobre 1.0 mm, máscara 2.0 mm) a $\ge 3.5\text{ mm}$ das bordas.
   - Furos de fixação M3 (furo 3.2 mm / anel 6.0 mm) nos cantos com folga de 1.5 mm para cabeça de parafuso.
   - Polaridade nítida no silkscreen: pino 1 em CIs, cátodo em diodos/LEDs, `+` em capacitores polarizados.

---

## 4. Referência Operacional e Resolução de Erros

Para instruções passo a passo, fluxo de ferramentas MCP, heurísticas de resolução de erros ERC/DRC e diretrizes específicas por subcircuito (Buck, LDO, Cristais), consulte a skill sob demanda:
👉 [.agents/skills/kicad10-pcb-designer/SKILL.md](file:///C:/Projetos_PCB/Novo_Projeto/.agents/skills/kicad10-pcb-designer/SKILL.md)
