# ADR-003: Segregação Física de Potência vs. Sinais em Fator de Forma de Módulo Ultracompacto

- **Data:** 2026-11-16
- **Status:** Aprovado
- **Autoridade / Decisor:** Usuário (Diretriz Crítica de EMC e Fator de Forma)
- **Componentes Afetados:** Layout da PCB, Zoneamento de Cobre, Posicionamento de Bornes e Dimensões Físicas

---

## 1. Contexto e Problema de Engenharia

Em placas controladoras com atuadores e relés, correntes de comutação elevadas ($di/dt$) e picos indutivos geram ruído eletromagnético e transientes térmicos. Se as trilhas de alimentação e acionamento de potência ficarem adjacentes a linhas de sinal, dados ou barramentos de comunicação (I2C, UART, SPI, RS485), há alto risco de corrupção de dados, travamento de microcontrolador e queima de circuitos lógicos.

Ao mesmo tempo, o usuário exige que a placa seja projetada no **menor tamanho possível, com o acabamento e a densidade de um módulo comercial vendido pronto**.

---

## 2. Decisões de Design e Layout

Para conciliar **isolamento eletromagnético rigoroso** com **compacidade máxima**:

1. **Zoneamento em Quadrantes / Extremidades Opostas:**
   - **Setor de Potência e Alimentação Bruta:** Localizado em uma extremidade da placa. Concentra bornes de entrada de tensão, proteções de alta energia e saídas de acionamento de carga.
   - **Setor Lógico, Sinais e Comunicação:** Localizado na extremidade oposta. Concentra microcontrolador, sensores, barramentos de comunicação e periféricos sensíveis.
   - **Distanciamento de Segurança:** Nenhuma trilha de potência ou comutação cruza ou corre paralela a trilhas de sinal de baixa tensão.

2. **Fator de Forma "Módulo Comercial Pronto" (Ultra-Dense Form Factor):**
   - Agrupamento milimétrico dos soquetes dos módulos COTS, eliminando espaços vazios ou "ilhas mortas" de placa.
   - Alinhamento uniforme dos bornes KRE formando uma régua periférica compacta.
   - Furos de fixação M3 estrategicamente posicionados nos cantos sem expandir a área desnecessariamente.

3. **Plano de Terra Segmentado por Fluxo de Retorno:**
   - A corrente de retorno da carga de potência flui diretamente para o borne negativo/GND de potência sem circular por baixo do microcontrolador ou dos módulos de sinal.

---

## 3. Consequências no Projeto

- A PCB final terá aparência de um módulo industrial comercial acabado (estilo *plug-and-play*).
- Imunidade eletromagnética máxima sem necessidade de aumentar a área física da placa.
