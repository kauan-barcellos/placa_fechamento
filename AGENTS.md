# Agent Operational Protocol - Projeto placa_fechamento

Este repositório opera sob um protocolo de engenharia autônomo. Qualquer agente que opere neste workspace deve seguir as diretrizes abaixo sem necessidade de solicitação explícita pelo usuário.

---

## 1. Consulta Obrigatória de Estado (Pre-Action Checklist)

Antes de executar qualquer comando ou alteração de circuito:
1. **Consultar [PROJECT_MEMORY.md](file:///C:/Projetos_PCB/Novo_Projeto/PROJECT_MEMORY.md):** Verificar trilhos de tensão, componentes alocados, pinagem do MCU e decisões prévias.
2. **Consultar [GEMINI.md](file:///C:/Projetos_PCB/Novo_Projeto/GEMINI.md):** Aplicar regras DFM da JLCPCB (trilhas mínimas de 0.15mm, vias 0.3mm/0.6mm, folgas, net classes).
3. **Consultar [.agents/skills/kicad10-pcb-designer/SKILL.md](file:///C:/Projetos_PCB/Novo_Projeto/.agents/skills/kicad10-pcb-designer/SKILL.md):** Seguir os procedimentos de ferramentas KiCad MCP (batching, componentes básicos LCSC, roteamento 45°).
4. **Respeitar Arquitetura Carrier Board (Módulos COTS):** Sempre projetar soquetes/headers para módulos prontos (LM2596, MCP4725, MAX485, etc.), sem desenhar eletrônica discreta desnecessária em volta de chips crus.

---

## 2. Padrões de Comunicação e Tokens (Per-Action Rules)

- **Voz Direta:** Seguir [.agents/rules/communication-and-tokens.md](file:///C:/Projetos_PCB/Novo_Projeto/.agents/rules/communication-and-tokens.md) e a skill `humanizer`. Sem jargões corporativos de IA ("mergulhar", "alavancar", "orquestrar", etc.).
- **Token Economy:** Seguir [.agents/skills/token-optimization/SKILL.md](file:///C:/Projetos_PCB/Novo_Projeto/.agents/skills/token-optimization/SKILL.md). Proibido despejo de arquivos inteiros no chat; usar links diretos `file:///...`.

---

## 3. Pós-Ação e Fechamento de Turno (Post-Action Checklist)

- Atualizar imediatamente [PROJECT_MEMORY.md](file:///C:/Projetos_PCB/Novo_Projeto/PROJECT_MEMORY.md) com novos componentes, pinagens ou regras criadas.
- Executar autonomamente `run_erc` (esquemático) ou `run_drc` (PCB) e corrigir todos os erros antes de concluir o turno.
- **Commits Git em pt-BR:** Toda mensagem de commit DEVE obrigatoriamente seguir o padrão Conventional Commits em português do Brasil (`<tipo>(<escopo>): <descrição em pt-BR>`). Proibido commits em inglês.
