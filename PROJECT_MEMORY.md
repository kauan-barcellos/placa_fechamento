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
- **Autonomia Operacional:** Execução silenciosa de checagens não destrutivas (ERC, DRC, previews) e commits semânticos atômicos.
- **Commits em pt-BR:** Todas as mensagens de commit DEVEM ser escritas em português do Brasil (`pt-BR`) no padrão Conventional Commits (`feat(escopo): descrição`). Proibido commits em inglês.
- **Economia de Tokens:** Diffs pontuais, links clicáveis `file:///...`, supressão de logs de sucesso verbosos e indicação proativa de `/compact`.

---

## 6. Histórico de Lições Aprendidas e Soluções DRC/ERC
- *Anotações sobre eventuais conflitos resolvidos serão salvas aqui para evitar reincidência.*
