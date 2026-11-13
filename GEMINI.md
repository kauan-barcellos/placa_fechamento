# Diretrizes de Engenharia de Hardware, DFM e Layout KiCad 10.0 (Padrão JLCPCB 2 Camadas)

Este documento estabelece as diretrizes técnicas, padrões de engenharia eletrônica, regras de **Design for Manufacturing (DFM)** e **Design for Assembly (DFA)** para fabricação na **JLCPCB (2 camadas)**.

Ele foi estruturado com parâmetros explícitos para consumo humano e execução programática automatizada via ferramentas do **KiCad MCP Server**.

---

## 1. Tabela de Especificações DFM JLCPCB (2 Camadas - 1 oz / 35 µm Cu)

A tabela abaixo define os limites absolutos do fabricante e os valores de projeto recomendados (*Safe Production Values*). Todas as regras de design no KiCad devem adotar os **Valores Recomendados**.

| Parâmetro Físico | Limite Absoluto JLCPCB | Valor Recomendado de Projeto | Observações de Engenharia |
| :--- | :--- | :--- | :--- |
| **Largura mínima de trilha (Sinais)** | 0.10 mm (4 mil) | **0.15 mm a 0.20 mm** (6 a 8 mil) | Maximiza rendimento e evita sub-corrosão química. |
| **Largura de trilha (Alimentação lógica < 0.5A)** | 0.10 mm | **0.50 mm** (20 mil) | Baixa queda de tensão e impedância reduzida. |
| **Largura de trilha (Potência 1.0A a 2.0A)** | - | **1.00 mm a 1.50 mm** (40 a 60 mil) | Conforme cálculo IPC-2152 para $\Delta T \le 10^\circ\text{C}$. |
| **Espaçamento mínimo (Clearance Cu-Cu)** | 0.10 mm (4 mil) | **0.15 mm** (padrão) / **0.20 mm** (seguro) | Trilha-trilha, trilha-pad e pad-pad. |
| **Espaçamento Cobre à Borda (Board Edge)** | 0.20 mm | **0.40 mm a 0.50 mm** | Evita exposição do cobre durante corte V-cut / fresa. |
| **Furo mínimo de Via (Drill Size)** | 0.15 mm | **0.30 mm** (12 mil) | Broca padrão sem custo adicional de furação fina. |
| **Diâmetro do Pad da Via (Diameter)** | Drill + 0.26 mm | **0.60 mm** (24 mil) | Garante anel anular seguro de $0.15\text{ mm}$. |
| **Anel Anular Mínimo (Annular Ring)** | 0.13 mm | **0.15 mm** | Previne rompimento (*breakout*) por tolerância de furação. |
| **Via de Potência (Individual)** | - | **Drill 0.40 mm / Pad 0.80 mm** | Suporta ~1.5A contínuos por via; usar múltiplas em paralelo. |
| **Barragem de Máscara (Soldermask Dam)** | 0.08 mm (3.1 mil) | **0.10 mm** | Mínimo entre pads vizinhos para evitar pontes de solda. |
| **Abertura de Máscara (Mask Clearance)** | 0.00 mm | **0.05 mm** (2 mil) | Expansão de máscara ao redor dos pads de cobre. |
| **Largura de traço de Silkscreen** | 0.15 mm (6 mil) | **0.15 mm a 0.20 mm** | Evita textos ilegíveis ou borrados na serigrafia. |
| **Altura mínima de texto de Silkscreen** | 0.80 mm (32 mil) | **1.00 mm a 1.20 mm** | Garante legibilidade clara a olho nu e AOI. |
| **Distância Silkscreen para Pad de Solda** | 0.15 mm | **0.20 mm** | Silkscreen NUNCA pode sobrepor cobre estanhado. |

---

## 2. Configurações Programáticas do KiCad MCP

Para garantir que o modelo e o agente executem as alterações sem erros, utilize diretamente as definições estruturadas abaixo nas ferramentas do KiCad MCP.

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
As conexões do esquemático e da PCB devem pertencer a uma das seguintes classes padronizadas:

| Nome da Classe | Trilha (`traceWidth`) | Espaçamento (`clearance`) | Furo Via (`viaDrill`) | Diâmetro Via (`viaDiameter`) | Aplicação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`Default`** | 0.20 mm | 0.15 mm | 0.30 mm | 0.60 mm | Sinais digitais gerais, GPIOs, LEDs, barramentos de controle. |
| **`Power_Low`** | 0.50 mm | 0.20 mm | 0.30 mm | 0.60 mm | Trilhas de alimentação local (+3V3, +5V, VDD) $\le 500\text{ mA}$. |
| **`Power_High`** | 1.00 mm | 0.25 mm | 0.40 mm | 0.80 mm | Entradas principais de alimentação, barramento de potência, relés. |
| **`Diff_USB`** | 0.25 mm | 0.18 mm | 0.30 mm | 0.60 mm | Par diferencial USB D+/D- (gap 0.18 mm, $Z_{diff} \approx 90\,\Omega$). |
| **`Diff_RS485`** | 0.30 mm | 0.25 mm | 0.30 mm | 0.60 mm | Par diferencial industrial A/B ($Z_{diff} \approx 120\,\Omega$). |
| **`Analog`** | 0.25 mm | 0.25 mm | 0.30 mm | 0.60 mm | Sinais analógicos de sensores e referências de ADC (baixo ruído). |

---

## 3. Boas Práticas no Esquemático (KiCad Eeschema)

1. **Modularização por Blocos Funcionais:**
   - Agrupar os circuitos visualmente em blocos delimitados: **Entrada e Proteção**, **Regulação de Tensão**, **Processamento / MCU**, **Interfaces de Comunicação**, **Acionamentos / Saídas**.
2. **Alimentação e `PWR_FLAG`:**
   - Todo trilho de alimentação derivado de conector externo, fusível, regulador LDO ou DC-DC deve receber explicitamente um símbolo `PWR_FLAG` no pino de saída correspondente, eliminando erros do tipo *"Pin connected to other pins, but not driven by any pin"* durante o ERC.
3. **Pinos Não Utilizados:**
   - Todo pino intencionalmente deixado sem conexão deve receber o marcador **No Connect** (`add_no_connect`).
4. **Metadados Obrigatórios nos Componentes:**
   - Cada símbolo no esquemático deve ter os seguintes campos preenchidos:
     - `Reference` (ex: `R1`, `C5`, `U2`, `D3`, `J1`).
     - `Value` (ex: `100nF`, `10k 1%`, `STM32F401CEU6`, `USBLC6-2SC6`).
     - `Footprint` (footprint padrão oficial do KiCad, ex: `Capacitor_SMD:C_0603_1608Metric`).
     - `LCSC Part #` (código de componente JLCPCB / LCSC, ex: `C14663`, facilitando SMT PCBA imediata).
5. **Capacitores de Desacoplamento no Esquemático:**
   - Devem ser desenhados adjacentes aos pinos de alimentação do respectivo circuito integrado, e não acumulados em um canto isolado da folha, garantindo clareza de projeto.

---

## 4. Diretrizes de Layout, Integridade de Sinal (SI) e EMC

### 4.1. Princípio do Caminho de Retorno (Current Return Path)
- Em sinais de alta velocidade ou bordas rápidas ($t_r < 5\text{ ns}$), o sinal de retorno não segue o caminho de menor resistência ôhmica, mas sim **o caminho de menor indutância de malha**, correndo diretamente sob a trilha no plano de referência adjacente.
- **Plano de Terra Contínuo (B.Cu):** A camada inferior (`B.Cu`) deve ser mantida prioritariamente como um **plano de terra sólido ininterrupto**.
- **Proibição de Fendas (*Slot Antennas*):** Nunca passe trilhas compridas na camada `B.Cu` que cortem transversalmente o plano de terra. Se for estritamente necessário rotear em `B.Cu`, utilize segmentos curtos e retorne imediatamente para `F.Cu`.

### 4.2. Capacitores de Desacoplamento (Power Integrity)
- **Distância Física:** Posicionar os capacitores cerâmicos de 100 nF a **menos de 2.0 mm** dos pinos de alimentação ($V_{DD}$ / $V_{CC}$) dos CIs.
- **Topologia de Conexão:** Conectar diretamente o pino do CI ao capacitor antes da via de alimentação, ou posicionar a via colada ao pad do capacitor (*flow-through*).
- **Indutância de Malha:** A via de terra do capacitor deve estar imediatamente ao lado do seu pad de terra, minimizando a área do loop transitório.

### 4.3. Proteção contra Transientes e ESD (TVS Diodes)
- **Localização:** Diodos TVS e varistores de proteção contra descarga eletrostática (IEC 61000-4-2) devem ser posicionados **imediatamente na entrada do conector externo**.
- **Roteamento In-Line (*Flow-Through*):** A trilha de sinal vinda do conector DEVE entrar obrigatoriamente no pad do diodo TVS e sair do pad em direção ao circuito interno.
  - **PROIBIDO:** Criar ramificações em T (*stubs*) para o diodo TVS. O pico de corrente de ESD sobe em menos de 1 ns e a indutância do stub torna o diodo ineficaz.
- **Terra do TVS:** O pad de terra do diodo TVS deve possuir no mínimo **2 vias de terra** conectando diretamente ao plano de terra para diminuir a indutância transitória ($V = L \cdot di/dt$).
- **Isolamento Físico:** Nunca roteie trilhas internas protegidas paralelamente às trilhas de entrada desprotegidas antes do TVS, evitando acoplamento capacitivo/indutivo mútuo.

### 4.4. Geometria de Trilhas e Supressão de Ruído
- **Curvas:** Roteamento a **45°** ou com cantos chanfrados. Proibido o uso de cantos vivos a 90° para evitar armadilhas de corrosão química (*acid traps*) e descontinuidades de impedância.
- **Regra 3W:** Trilhas de sinais críticos (clocks, PWM, SPI, barramentos de interrupção) devem manter espaçamento mínimo de $3 \times W$ (onde $W$ é a largura da trilha) em relação a outras trilhas para eliminar diafonia (*crosstalk*).

---

## 5. Planos de Cobre, Dissipação Térmica e Vias de Costura

### 5.1. Planos de Cobre (`add_copper_pour`)
- **Camada Inferior (`B.Cu`):** Plano de terra contínuo (`net: "GND"`, `padConnection: "thermal"`, `clearance: 0.20`, `minWidth: 0.20`, `priority: 0`).
- **Camada Superior (`F.Cu`):** Preenchimento de cobre conectado ao terra (`GND`) em todas as áreas não ocupadas por trilhas de sinal e componentes.
- **Alívio Térmico (*Thermal Relief*):**
  - Obrigatório em todos os pads de componentes PTH e passivos SMD ligados ao plano de terra para possibilitar a soldagem sem absorção excessiva de calor.
  - Pads térmicos de CIs (ex: PowerPAD de reguladores, pads inferiores expostos de MOSFETs e QFNs) devem usar conexão **sólida** (`padConnection: "solid"`) com matriz de vias térmicas.

### 5.2. Vias de Costura de Terra (`add_gnd_stitching_vias`)
A ferramenta do KiCad MCP deve ser configurada e executada com a seguinte estratégia combinada:
- **Estratégias:** `["grid", "around_refs", "in_zones"]`
- **Espaçamento da Malha (`spacing`):** `4.0 mm`
- **Furo (`viaDrill`):** `0.30 mm` / **Diâmetro (`viaSize`):** `0.60 mm`
- **Margem da Borda (`edgeMargin`):** `0.50 mm`
- **Densificação (`densifyRefs`):** Incluir os designadores de MCUs, reguladores de comutação (DC-DC) e conectores de entrada para cercar as áreas de ruído com barreira de vias de baixa impedância.

---

## 6. Diretrizes de Montagem Automatizada (JLCPCB SMT / DFA)

1. **Fiducials Globais:**
   - Adicionar **3 fiducials globais** de alinhamento óptico posicionados de forma assimétrica próximos aos cantos da PCB.
   - Especificação do Pad: Círculo de cobre sólido com diâmetro de `1.0 mm` e abertura de máscara de solda de `2.0 mm`.
   - Distância da borda da placa: Mínimo de `3.5 mm` para não ser obstruído pelos trilhos de transporte das máquinas pick-and-place.
2. **Prevenção de Tombstoning em Componentes Passivos (0402 / 0603 / 0805):**
   - Garantir simetria térmica nos dois pads do componente. Se um pad estiver ligado ao plano de terra, a conexão deve ser feita por alívio térmico (*thermal relief*) ou trilha com largura compatível à trilha do pad oposto.
3. **Indicação Clara de Polaridade no Silkscreen:**
   - **CIs e CIs QFN/SOIC:** Marcação visível do Pino 1 (ponto de serigrafia com diâmetro $\ge 0.5\text{ mm}$ ou chanfro).
   - **Diodos e LEDs:** Linha espessa ou faixa indicando o terminal de **cátodo**.
   - **Capacitores Eletrolíticos e de Tântalo:** Marcação nítida do polo positivo (`+`).
   - **Conectores:** Identificação clara de cada pino (ex: `GND`, `VCC`, `TX`, `RX`, `IN`, `OUT`).
4. **Furos de Fixação (Mounting Holes):**
   - Utilizar furos padrão M3 (furo `3.2 mm` com anel de cobre estanhado de `6.0 mm`), posicionados nos cantos da placa com folga mínima de `1.5 mm` para a cabeça do parafuso, isolados de trilhas de sinal e interligados ao terra (`GND`) se apropriado para proteção de chassi.

---

## 7. Fluxo Obrigatório de Validação Incremental (Zero Violações)

Todo o fluxo de desenvolvimento pelo agente e ferramentas de automação deve seguir estritamente o seguinte pipeline:

```
[Definição de Requisitos]
          │
          ▼
[Desenho do Esquemático] ──► [Executar run_erc] ──► Erros/Avisos? ──► [Corrigir no Esquemático]
                                    │ (Zero Erros)
                                    ▼
                          [Sincronizar com PCB]
                                    │
                                    ▼
[Roteamento & Planos]    ──► [Executar run_drc] ──► Violações?   ──► [Ajustar Trilha/Clearance]
                                    │ (Zero Violações)
                                    ▼
                          [Exportar Gerbers/BOM]
```

1. **Validação Elétrica (`run_erc`):**
   - Executada a cada bloco do esquemático finalizado. Não é permitido avançar para o layout de PCB enquanto houver qualquer erro ou aviso pendente no ERC.
2. **Validação de Regras de Design (`run_drc`):**
   - Executada a cada etapa de roteamento e inserção de planos. Toda violação de espaçamento, furos não conectados, colisões de *courtyard* ou anel anular insuficiente deve ser resolvida imediatamente até que o DRC retorne 0 violações.
