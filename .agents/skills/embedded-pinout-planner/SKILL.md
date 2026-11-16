---
name: embedded-pinout-planner
description: >-
  Planejador e validador de pinagem e multiplexação de microcontroladores (STM32, ESP32, RP2040).
  Use antes de ligar fios de MCU no esquemático para evitar colisões de periféricos, strapping pins e incompatibilidades de firmware.
---

# Embedded Pinout & Peripheral Multiplexing Planner

Esta skill orienta a alocação e verificação lógica de pinos de microcontroladores antes da geração das trilhas no KiCad, garantindo que o hardware seja 100% integrável com o código embarcado (C/C++).

---

## 1. Protocolo de Checagem Prévia de Pinos

Antes de atribuir um pino do MCU a qualquer componente, execute a lista de verificação:

1. **Pinos de Boot e Strapping Pins (Crítico):**
   - **ESP32:** Pinos GPIO0, GPIO2, GPIO12 e GPIO15 controlam o modo de boot e tensão da flash. Não conecte cargas que forcem nível lógico incorreto no reset.
   - **STM32:** Pino `BOOT0` deve ter resistor de pull-down (10k) para inicializar da Flash interna.
2. **Periféricos Dedicados de Hardware:**
   - Barramentos rápidos (SPI, I2C, UART) devem utilizar controladores dedicados em vez de bit-banging por software, sempre que possível.
   - Certifique-se de que os pinos selecionados pertencem à mesma instância de periférico (ex: `USART1_TX` e `USART1_RX`).
3. **Pinos Analógicos (ADC):**
   - Verificar tolerância de tensão máxima ($3.3\text{V}$ absoluto em CIs alimentados por $3.3\text{V}$). Sinais de sensores externos devem ter divisor resistivo ou grampeamento por diodo Schottky.
4. **Depuração e Programação:**
   - Reservar sempre pinos para interface de gravação:
     - STM32: `SWDIO`, `SWCLK`, `NRST`.
     - ESP32 / RP2040: `TX`, `RX`, `EN`, `BOOT`.

---

## 2. Registro no Projeto e Exportação de Firmware

Após validar a pinagem:
1. Atualizar a Seção 4 de [PROJECT_MEMORY.md](file:///C:/Projetos_PCB/Novo_Projeto/PROJECT_MEMORY.md#L37-L40) com a tabela de pinos e funções.
2. Gerar opcionalmente o arquivo de constantes `pinout.h` para que a equipe de firmware utilize as mesmas definições do hardware sem divergências.
