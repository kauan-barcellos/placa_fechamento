# ADR-001: Arquitetura Carrier Board Baseada em Módulos Prontos (COTS)

- **Data:** 2026-11-16
- **Status:** Aprovado
- **Autoridade / Decisor:** Usuário (Regra Fundamental de Hardware)
- **Componentes Afetados:** Todos os blocos (Alimentação, MCU, DAC, Comunicação, Atuadores)

---

## 1. Contexto e Problema de Engenharia

O desenvolvimento de circuitos impressos industriais a partir de componentes de silício discretos (chips crus, indutores para conversores chaveados, redes de realimentação sensíveis, transceivers RS485 com polarização manual) introduz alta complexidade de cálculo, riscos térmicos, ruído por layout inadequado e dificuldade de manutenção em bancada.

O usuário estabeleceu a regra mandatória de simplificar o desenvolvimento utilizando **módulos prontos comerciais (Commercial Off-The-Shelf - COTS)**.

---

## 2. Alternativas Avaliadas

- **Opção A: Design Discreto Integral**
  - Desenhar conversores chaveados (ex: LM2596 SMD com indutor, diodo Schottky e capacitores discretos), CI DAC avulso e transceiver RS485 na própria placa.
  - *Desvantagens:* Alto tempo de projeto, maior risco de ruído eletromagnético, testes complexos de homologação, custo de prototipagem elevado e retrabalho em caso de queima.
- **Opção B: Carrier Board / Placa-Mãe com Soquetes para Módulos Prontos (Escolhida)**
  - A PCB atua como placa de interconexão (*Carrier Board*).
  - Cada subsistema crítico é conectado via barras de pinos (pin headers 2.54 mm ou bornes):
    - Módulo Step-Down de tensão (ex: LM2596, MP1584).
    - Módulo de conversão DAC (ex: MCP4725 I2C).
    - Módulo de comunicação (ex: MAX485 / RS485).
    - Módulo de processamento (ex: ESP32 DevKit, BluePill STM32, RP2040).
  - *Vantagens:* Circuitos pré-calibrados e testados de fábrica, facilidade de montagem, substituição rápida de módulos com defeito em campo, zero complexidade de roteamento de nós de alta frequência de fontes chaveadas.

---

## 3. Decisão Escolhida e Justificativa

**Aprovada a Opção B.**
A placa `placa_fechamento` será projetada como uma **Carrier Board de Alta Densidade / Ultracompacta**.
- O esquemático e layout do KiCad utilizarão barras de pinos (passo 2.54 mm) para encaixe dos módulos comerciais definidos para o projeto, e bornes a parafuso (KRE) para fiação externa.
- A meta de layout é **a máxima compacidade física viável**, agrupando os módulos e bornes de forma eficiente, sem comprometer folgas elétricas, dissipação térmica (IPC-2152) e continuidade do plano de terra em `B.Cu`.

---

## 4. Consequências no Layout e Esquemático

1. **Esquemático KiCad:** Símbolos de conectores/pin headers com rótulos semânticos claros correspondentes aos pinos dos módulos que forem definidos pelo usuário.
2. **Layout KiCad:** Footprints padronizados de barras de pinos (`Connector_PinHeader_2.54mm`) com espaçamento físico exato entre fileiras e arranjo espacial compacto.
3. **Robustez:** A Carrier Board cuidará das conexões externas (bornes a parafuso KRE para chicotes elétricos de campo, fusíveis de proteção na entrada e trilhas de potência reforçadas).
