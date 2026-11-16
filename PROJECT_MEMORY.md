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

- **Trilhos de Alimentação (Power Rails):**
  - A definir.
- **Microcontrolador / Processador:**
  - A definir.
- **Interfaces e Barramentos:**
  - A definir.
- **Entradas e Saídas (I/O):**
  - A definir.

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
- **Validação:** ERC e DRC com 0 erros/violações mandatórios antes de qualquer commit/avanço.
- **Voz e Comunicação:** Peer-to-peer técnico, sem subserviência, sem rodeios ou clichês de IA.
- **Formato BLUF:** Resumo/conclusão na primeira linha, seguido de detalhamento conciso e próximas ações.
- **Decisões Guiadas:** Apresentação de opções estruturadas em múltipla escolha com `(Recomendado)`.
- **Autonomia Operacional:** Execução silenciosa de checagens não destrutivas (ERC, DRC, previews), autodiagnóstico via `diagnostico.bat` e commits semânticos atômicos.
- **Rollback de Segurança:** Rollback automático (`circuit_checkpoint.py --rollback`) caso o ERC/DRC não convirja em 2 tentativas.
- **Commits em pt-BR:** Todas as mensagens de commit DEVEM ser escritas em português do Brasil (`pt-BR`) no padrão Conventional Commits (`feat(escopo): descrição`). Proibido commits em inglês.
- **Economia de Tokens & Subagentes:** Diffs pontuais, links clicáveis `file:///...`, supressão de logs de sucesso verbosos, subagentes com modelo `flash` para pesquisas de catálogo/datasheet, GEMINI.md enxuto (5.2 KB) e indicação proativa de `/compact`.

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
