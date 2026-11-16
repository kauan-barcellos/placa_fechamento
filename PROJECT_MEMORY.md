# Memória Persistente do Projeto - placa_fechamento

Este documento mantém o estado vivo do hardware, decisões técnicas, componentes selecionados e preferências de projeto. Ele serve como ponto central de contexto persistente entre conversas e compactações de histórico.

---

## 1. Identificação e Metadados do Projeto
- **Nome do Projeto:** `placa_fechamento`
- **Ambiente CAD:** KiCad 10.0
- **Fabricante Alvo:** JLCPCB (2 Camadas, 1 oz / 35 µm Cu, 1.6 mm FR-4)
- **Repositório:** [github.com/kauan-barcellos/placa_fechamento](https://github.com/kauan-barcellos/placa_fechamento)
- **Status Atual:** Infraestrutura e regras configuradas; aguardando requisitos do circuito.

---

## 2. Decisões de Arquitetura de Hardware
*(Esta seção é atualizada continuamente à medida que definimos o circuito)*

- **Filosofia de Arquitetura (Regra de Ouro):** **Carrier Board Ultracompacta para Módulos COTS**. A placa atua como placa-mãe de interconexão compacta, utilizando barras de pinos (2.54 mm) para encaixe de módulos comerciais pré-montados e bornes a parafuso (KRE) para fiação externa de campo (Ref: [ADR-001](.agents/adr/ADR-001-arquitetura-baseada-em-modulos-cots.md)).
- **Meta de Fator de Forma:** **Máxima Compacidade Possível**, agrupando os módulos e bornes de forma densa e organizada, sem comprometer a eficiência elétrica (regras IPC-2152 de corrente, isolamento térmico e plano de terra contínuo em `B.Cu`).
- **Usabilidade e Montagem (Regra de Ouro):** Zoneamento periférico de I/O (Entradas em uma borda, Saídas de potência na borda oposta), parafusos de bornes KRE 100% desobstruídos sem cabos passando sobre módulos, Test Points de bancada acessíveis (GND, trilhos de tensão) e serigrafia explicativa com marcação de Pino 1 (Ref: [ADR-002](.agents/adr/ADR-002-diretrizes-de-ergonomia-zoneamento-e-montagem.md)).
- **Segregação Potência vs. Sinais & Estilo Módulo Comercial:** Separação física rígida entre bornes/pads de alimentação/potência e linhas de sinal/comunicação em extremidades opostas. Layout ultracompacto e denso com acabamento de módulo comercial de mercado (Ref: [ADR-003](.agents/adr/ADR-003-segregacao-potencia-sinais-modulo-ultracompacto.md)).
- **Módulos do Circuito:** *A definir com base na função específica da placa de fechamento.*
- **Trilhos de Alimentação (Power Rails):** *A definir conforme requisitos dos módulos e atuadores.*
- **Microcontrolador / Processador:** *A definir.*
- **Entradas e Saídas (I/O):** Bornes a parafuso KRE para conexão externa de alimentação, sensores e atuadores.

---

## 3. Registro de Componentes Críticos (BOM Ativa)
| Ref | Valor | Descrição | Footprint | LCSC Part # | Tipo (Basic/Ext) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | - | - | - | - | - | - |

---

## 4. Mapeamento de Pinos e Funções (Pinout Matrix)
| Pino | Sinal / Net | Função | Net Class | Observações / Filtro |
| :--- | :--- | :--- | :--- | :--- |

---

## 5. Preferências e Restrições Registradas pelo Usuário
- **DFM:** Padrão JLCPCB 2 camadas estrito (traço mín 0.15mm, furo via 0.3mm / pad 0.6mm).
- **Arquitetura de Módulos Prontos & Alta Compacidade:** Mandatório adotar barras de pinos/soquetes para módulos comerciais pré-montados (COTS), bornes a parafuso para chicotes externos e buscar a máxima compacidade física da PCB, garantindo integridade térmica (IPC-2152) e plano de terra contínuo em `B.Cu`.
- **Ergonomia e Usabilidade Física:** Bornes voltados para o exterior com acesso livre à chave de fenda, separação física entre entradas de sinal e saídas de potência, inclusão de Test Points acessíveis (GND/Tensões) e serigrafia de alta nitidez com identificação pino a pino e marcação do Pino 1.
- **Validação:** ERC e DRC com 0 erros/violações mandatórios antes de qualquer commit/avanço.
- **Voz e Comunicação:** Peer-to-peer técnico, sem subserviência, sem rodeios ou clichês de IA.
- **Formato BLUF:** Resumo/conclusão na primeira linha, seguido de detalhamento conciso e próximas ações.
- **Decisões Guiadas:** Apresentação de opções estruturadas em múltipla escolha com `(Recomendado)`.
- **Autonomia Operacional:** Execução silenciosa de checagens não destrutivas (ERC, DRC, previews), autodiagnóstico via `diagnostico.bat` e commits semânticos atômicos.
- **Rollback de Segurança:** Rollback automático (`circuit_checkpoint.py --rollback`) caso o ERC/DRC não convirja em 2 tentativas.
- **Commits em pt-BR:** Todas as mensagens de commit DEVEM ser escritas em português do Brasil (`pt-BR`) no padrão Conventional Commits (`feat(escopo): descrição`). Proibido commits em inglês.
- **Economia de Tokens & Subagentes:** Diffs pontuais, links clicáveis `file:///...`, supressão de logs de sucesso verbosos, subagentes com modelo `flash` para pesquisas de catálogo/datasheet, GEMINI.md enxuto (5.2 KB) e indicação proativa de `/compact`.
- **Tema Visual e IDE:** Preset Catppuccin Mocha com ícones Catppuccin, tipografia Cascadia Code com ligaduras (`fontLigatures: true`), cursor suave e diffs visuais aprimorados em tons pastel.

---

## 6. Histórico de Lições Aprendidas e Soluções DRC/ERC
- **Headless CLI vs GUI (Task 450):** Nunca importar módulos gráficos do KiCad (`pcbnew`) diretamente em scripts headless sem GUI; usar exclusivamente `kicad-cli.exe` com timeout de 15s para evitar diálogos invisíveis de asserção wxWidgets (`assert PgmOrNull`).
- **Orçamento de Regras (Rule Budget):** Manter `GEMINI.md` estritamente focado em parâmetros DFM numéricos (~5 KB) e delegar procedimentos extensos para a skill sob demanda `kicad10-pcb-designer`.

---

## 7. Catálogo de Skills Modulares Ativas (.agents/skills)
1. `kicad10-pcb-designer`: Procedimentos avançados KiCad MCP, heurísticas de layout e exportação JLCPCB.
2. `kicad-regime-classifier`: Classificação física e térmica de nets (IPC-2152, alta velocidade, analógico, potência).
3. `embedded-pinout-planner`: Validação de funções alternativas de MCU e prevenção de conflitos de strapping pins.
4. `bom-lifecycle-auditor`: Auditoria contra base SQLite JLCPCB de 513k peças e priorização de Basic Parts.
5. `systematic-debugging`: Protocolo determinístico em 4 fases para investigar causa raiz de falhas ERC/DRC.
6. `evidence-backed-verification`: Validação mandatória de 0 erros/violações e previews antes da entrega.
7. `hardware-adr`: Registros formais de decisões de arquitetura de circuito em `.agents/adr/`.
8. `git-hygiene-and-secrets`: Filtragem de arquivos temporários do KiCad e proteção contra vazamento de chaves.
9. `agent-memory`: Padrão de memória persistente viva para hardware.
10. `token-optimization`: Técnicas de economia de contexto e supressão de ruído de ferramentas.
11. `project-architect`: Planejamento arquitetural formal e engenharia guiada por especificação (SPEC.md).
12. `systematic-code-reviewer`: Auto-auditoria crítica adversarial de código, diffs e casos de borda.
13. `tdd-cycle-orchestrator`: Ciclo estrito Red-Green-Refactor com testes automatizados de comportamento.
14. `task-decomposition-and-tracking`: Decomposição atômica de tarefas e checklist vivo persistente.
15. `shell-safety-and-guardrails`: Execução determinística não-interativa e timeouts obrigatórios no terminal.
16. `secret-sanitizer-and-privacy`: Mascaramento em tempo de execução de chaves de API, senhas e tokens.
17. `subagent-orchestrator-mapreduce`: Delegação paralela leve (flash) e agregação sem poluição de contexto.
