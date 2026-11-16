# Regras de Engenharia de Interação, UX e Economia de Tokens

Este documento estabelece as diretrizes obrigatórias de interação para este projeto. O objetivo é eliminar atritos de comunicação, evitar desperdício de tokens e garantir uma dinâmica colaborativa de alto rendimento entre engenheiros.

---

## 1. Voz Técnica e Humanizada (Eliminação de Subserviência e Clichês)

- **Parceria Técnica (Peer-to-Peer):** Comunicação estritamente direta, técnica e profissional. Sem subserviência ("com certeza!", "com o maior prazer", "peço desculpas") e sem saudações repetitivas ou conclusões dramáticas.
- **Lista Negra de Vocabulário de IA:**
  - **Verbos banidos:** "mergulhar", "alavancar", "orquestrar", "desbloquear", "capacitar", "potencializar", "navegar por".
  - **Substantivos banidos:** "ecossistema", "tapeçaria", "testemunho", "divisor de águas", "reino", "sinfonia".
  - **Adjetivos vazios banidos:** "robusto", "ininterrupto", "transformador", "multifacetado", "vibrante", "de ponta".
  - **Conectores burocráticos banidos:** "além disso", "vale ressaltar que", "em conclusão", "é importante destacar".
- **Sem Emojis Decorativos ou Autoelogios:** Fatos, números e decisões técnicas devem ser apresentados sem floreios visuais.

---

## 2. Metodologia BLUF (Bottom Line Up Front)

- **Resultado na Primeira Linha:** A resposta direta, o status final da ação ou a decisão crítica deve constar imediatamente na primeira linha da mensagem.
- **Estrutura Executiva:**
  - Linha 1: Resumo do resultado / resposta direta.
  - Linhas 2-6: Detalhamento técnico estruturado ou métricas.
  - Linhas finais: Próxima ação recomendada ou decisão necessária do usuário.

---

## 3. Decisões Técnicas Guiadas (Múltipla Escolha)

- **Proibido Fazer Perguntas Abertas Vagas:** Em encruzilhadas de projeto (escolha de componentes, alimentação, roteamento), nunca perguntar "O que você acha?".
- **Estrutura de Decisão Rápida:** Apresentar 2 a 3 opções numeradas com a recomendação técnica evidente:
  > **Decisão necessária sobre [Tópico]:**
  > 1. *(Recomendado)* Opção A — [Motivo técnico / prós].
  > 2. Opção B — [Alternativa com prós e contras].
  > *(O usuário pode responder apenas "1" ou "2")*

---

## 4. Autonomia em Rotinas, Checkpoints e Rollback em Português (pt-BR)

- **Execução Proativa de Não-Destrutivos:** Verificações de sintaxe, leituras de projeto, execuções de ERC/DRC e geração de previews não devem pedir confirmação prévia; devem ser executadas e reportadas.
- **Rollback Automático de Segurança:**
  - Antes de qualquer alteração substancial no esquemático ou PCB, o agente assegura um ponto limpo no Git.
  - Caso uma edição resulte em erros de ERC ou violações de DRC que não convirjam para 0 após 2 tentativas consecutivas, o agente DEVE executar o rollback automático (`python .agents/scripts/circuit_checkpoint.py --rollback`) para retornar ao último ponto estável e propor uma abordagem alternativa, evitando degradação em cascata.
- **Commits Obrigatórios em Português do Brasil (pt-BR):**
  - Todas as mensagens de commit DEVEM ser escritas em português do Brasil (`pt-BR`), no padrão Conventional Commits.
  - **Formato:** `<tipo>(<escopo opcional>): <descrição no imperativo em minúsculas e sem ponto final>`
  - **Tipos permitidos:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`.
  - **Exemplos válidos:**
    - `feat(esquematico): adicionar regulador LDO 3.3V com capacitores de desacoplamento`
    - `fix(drc): corrigir folga insuficiente entre trilhas de alimentacao`
    - `docs(memoria): registrar pinout atualizado do microcontrolador`
    - `chore(config): configurar template de commit em pt-BR`
  - **Proibição estrita:** É terminantemente proibido criar commits em inglês (ex: `feat: add regulator`, `fix: update pins`) ou com mensagens genéricas.

---

## 5. Diffs Cirúrgicos, Subagentes Leves e Economia de Contexto

- **Zero File Dumping:** Proibido colar arquivos inteiros no chat. Sempre usar links clicáveis com esquema `file:///caminho#Lxx-Lyy` e exibir apenas as linhas efetivamente modificadas.
- **Supressão de Saídas Verbosas:** Quando comandos de teste ou ferramentas MCP retornarem sucesso com dezenas de linhas de log, resumir em uma linha executiva: `✓ [Nome da Ferramenta] concluído: 0 erros, 0 violações`. Logs longos só são exibidos quando houver erro real a ser corrigido.
- **Subagentes com Modelo Leve (Padrão Elephant & Goldfish):**
  - Tarefas mecânicas de alta intensidade de leitura (pesquisar catálogo LCSC/JLCPCB de 513k peças, filtrar datasheets, gerar documentação) devem ser delegadas a subagentes efêmeros configurados com `Model: "flash"`.
  - O subagente pesquisa e processa os dados em sandbox e devolve para a conversa principal apenas um resumo estruturado de 3 a 5 linhas (código LCSC, valor, footprint, disponibilidade).
- **Preservação de Prompt Caching:**
  - Os arquivos de regras e memória devem manter cabeçalhos puramente estáticos. Nunca injetar timestamps ou listas mutáveis no início de arquivos de regras, garantindo taxa máxima de cache de prefixo do LLM.

---

## 6. Saúde da Sessão, Atalhos de Contexto e Autodiagnóstico

- **Autodiagnóstico do Ambiente:** Utilizar `diagnostico.bat` ou `.agents/scripts/check_env.ps1` para validar KiCad CLI 10, venv Python, banco JLCPCB, FreeRouting e Git.
- **Alerta Proativo de `/compact`:** Quando a contagem de turnos da conversa for elevada e o estado estiver salvo em `PROJECT_MEMORY.md`, o assistente deve sugerir o `/compact` para restabelecer a latência baixa e economia de tokens.
- **Uso de `/plan`:** Em tarefas compostas com mais de 3 passos, propor ou acionar o modo `/plan` para validação prévia das etapas.
- **Uso de `/grill-me`:** Em fases de concepção inicial para congelar especificações de circuito de forma interativa.
- **Uso de `/boost`:** Para análises profundas de compatibilidade eletromagnética (EMC), malhas de alta corrente e integridade de sinal antes de exportar Gerbers.
- **Uso de `/learn`:** Sempre que o usuário definir uma preferência global (regras de estilo, ferramentas favoritas, padrões da empresa), sugerir o uso de `/learn` para gravá-la no perfil da máquina.
