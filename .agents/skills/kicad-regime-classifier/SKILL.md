---
name: kicad-regime-classifier
description: >-
  Classificador de regimes físicos e elétricos de trilhas no KiCad 10.0 (IPC-2152, alta velocidade, analógico e potência).
  Use antes de rotear qualquer circuito para garantir larguras corretas, folgas 3W e integridade de retorno de terra.
---

# KiCad Physical & Electrical Regime Classifier

Esta skill estabelece a classificação física e térmica obrigatória de todas as conexões (*nets*) de uma placa antes do início do roteamento, prevenindo sobreaquecimento por efeito Joule, perda de impedância e diafonia (*crosstalk*).

---

## 1. Matriz de Classificação de Regimes

Todo sinal gerado no esquemático DEVE ser enquadrado em um dos quatro regimes físicos abaixo:

| Regime | Identificadores Típicos | Largura Recomendada | Folga Mínima | Vias Recomendadas | Regra Especial |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Potência Alta (`Power_High`)** | `VIN`, `+12V`, `+24V`, `VRELAY`, `GND_PWR` | **1.00 mm a 1.50 mm** | 0.25 mm | Furo 0.40 / Pad 0.80 mm (ou múltiplas) | Cálculo IPC-2152 para $\Delta T \le 10^\circ\text{C}$ ($\ge 1.5\text{A}$). |
| **Alimentação Lógica (`Power_Low`)** | `+5V`, `+3V3`, `VDD`, `VCC` | **0.50 mm** | 0.20 mm | Furo 0.30 / Pad 0.60 mm | Queda de tensão $< 2\%$ e baixa impedância. |
| **Alta Velocidade / Diferencial** | `USB_D+`, `USB_D-`, `RS485_A`, `RS485_B`, `CLK` | **0.25 mm a 0.30 mm** | 0.18 mm a 0.25 mm | Furo 0.30 / Pad 0.60 mm | Roteamento pareado com tolerância de comprimento $\le 1.0\text{ mm}$. |
| **Analógico Sensível (`Analog`)** | `ADC_*`, `VREF`, `SENSE_*` | **0.25 mm** | 0.25 mm | Furo 0.30 / Pad 0.60 mm | Isolamento de nós $SW$ de fontes e planos chaveados. |
| **Lógica Geral (`Default`)** | `GPIO_*`, `LED_*`, `ENABLE`, `RELAY_CTRL` | **0.20 mm** | 0.15 mm | Furo 0.30 / Pad 0.60 mm | Roteamento livre respeitando DFM da JLCPCB. |

---

## 2. Procedimento de Aplicação no KiCad MCP

1. **Criação das Net Classes:** Chamar `create_netclass` com os parâmetros numéricos exatos de cada regime.
2. **Atribuição das Redes:** Associar cada net à sua respectiva classe com `assign_net_to_class`.
3. **Ordem Estrita de Roteamento:**
   - 1º: Diodos TVS in-line e barramentos de potência de entrada.
   - 2º: Pares diferenciais e relógios de alta frequência (com plano contínuo em `B.Cu`).
   - 3º: Sinais analógicos sensíveis.
   - 4º: Sinais digitais secundários e controle de atuadores.
4. **Regra 3W para Clocks e PWM:** Trilhas de chaveamento rápido devem manter distância mínima de $3 \times W$ em relação a qualquer outro condutor vizinho.
