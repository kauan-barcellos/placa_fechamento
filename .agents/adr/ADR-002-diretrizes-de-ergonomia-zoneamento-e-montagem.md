# ADR-002: Diretrizes de Ergonomia, Zoneamento de I/O e Facilidade de Montagem

- **Data:** 2026-11-16
- **Status:** Aprovado
- **Autoridade / Decisor:** Usuário (Diretriz de Usabilidade e Montagem)
- **Componentes Afetados:** Layout da PCB, Posicionamento de Conectores, Silkscreen e Test Points

---

## 1. Contexto e Problema de Engenharia

Placas compactas que utilizam múltiplos módulos e fiação externa frequentemente sofrem de problemas ergonômicos graves:
- Cabos de entrada e saída cruzando por cima de componentes, dificultando manutenção ou substituição de módulos.
- Parafusos de bornes bloqueados fisicamente pela altura de componentes vizinhos.
- Dificuldade de diagnóstico em bancada por falta de pontos acessíveis de teste de tensão e terra.
- Risco de inversão de polaridade ou ligação errada por falta de identificação nítida na serigrafia.

---

## 2. Decisões de Design e Layout

Para garantir **eficiência máxima, facilidade de montagem e usabilidade superior**, o layout da `placa_fechamento` adotará as seguintes regras de projeto:

1. **Zoneamento Periférico de Entradas e Saídas (I/O Floorplanning):**
   - **Borda de Entrada:** Bornes de alimentação principal e entradas de sensores/sinais agrupados em um setor exclusivo da borda da placa.
   - **Borda de Saída:** Bornes de acionamento (relés/cargas de potência) agrupados no setor oposto.
   - **Acesso Livre:** Todos os bornes a parafuso voltados para o exterior da placa, garantindo que os fios saiam diretamente para o chicote sem sobrepor nenhum módulo.
   - **Acesso à Chave de Fenda:** Folga vertical e horizontal garantida sobre os parafusos dos bornes para permitir aperto/desaperto sem remover módulos ou placas.

2. **Facilidade de Montagem e Manutenção:**
   - Soquetes de barras de pinos (passo 2.54 mm) com tolerância de inserção para permitir encaixe e desencaixe manual dos módulos.
   - Espaçamento de no mínimo 3.0 mm entre módulos vizinhos para evitar colisões mecânicas e permitir ventilação natural.

3. **Pontos de Teste (Test Points) & Diagnóstico Visual:**
   - **Test Points de Bancada:** Inclusão de ilhas/pads acessíveis com marcação nítida para ponta de prova: `GND`, `VIN`, `VCC` (5V/3.3V) e sinais-chave de controle.
   - **LEDs Indicadores:**
     - LED de alimentação ativa (Power OK).
     - LEDs indicadores de acionamento de saída (ex: status de relé ligado).

4. **Serigrafia (Silkscreen) de Alta Legibilidade:**
   - Todo borne e pino de módulo terá rotulação textual clara (ex: `VIN+`, `GND`, `SENS1`, `NO`, `COM`, `NC`).
   - Marcação visível do **Pino 1** de cada barra de pinos para impedir inversão de módulos na montagem.

---

## 3. Consequências no Projeto

- Layout altamente organizado, intuitivo para operadores de campo e seguro contra erros de montagem ou curtos-circuitos acidentais.
- Preservação da compacidade sem estrangular o acesso físico às conexões elétricas.
