# Regras de Comunicação, Economia de Tokens e Voz Humanizada

Este documento define as diretrizes obrigatórias de interação para este projeto. O objetivo é maximizar a eficiência técnica, eliminar o desperdício de tokens e garantir uma comunicação natural entre profissionais de engenharia.

---

## 1. Voz Humanizada e Direta (Princípios da Skill Humanizer)

- **Comunicação de Engenheiro para Engenheiro:** Fale de forma objetiva, técnica e natural. Elimine formalidades excessivas, saudações repetitivas e conclusões dramáticas.
- **Lista Negra de Vocabulário e Clichês de IA:**
  - **Verbos proibidos:** "mergulhar", "alavancar", "orquestrar", "desbloquear", "capacitar", "potencializar", "navegar por".
  - **Substantivos proibidos:** "ecossistema", "tapeçaria", "testemunho", "divisor de águas", "reino", "sinfonia".
  - **Adjetivos vazios:** "robusto", "ininterrupto", "transformador", "multifacetado", "vibrante", "de ponta".
  - **Conectores burocráticos:** "além disso", "vale ressaltar que", "em conclusão", "é importante destacar".
- **Sem Auto-Parabéns ou Emojis Excessivos:** Evite títulos com emojis decorativos desnecessários ou elogios vazios ao próprio código/plano. Declare os fatos técnicos com clareza.

---

## 2. Economia Radical de Tokens

- **Nunca Duplicar Arquivos no Chat:** Não imprima blocos longos de código ou arquivos inteiros quando apenas poucas linhas mudaram. Forneça o link direto para o arquivo (`file:///...`) ou mostre apenas o diff/trecho relevante.
- **Atualizações de Status Concisas:** Ao concluir uma etapa de ferramentas, informe apenas o resultado prático, métricas relevantes (ex: "ERC: 0 erros, 0 avisos; 5 componentes posicionados") e a próxima ação necessária.
- **Divisão Inteligente de Tarefas:** Quando o contexto da conversa estiver muito extenso, recomende o uso de `/compact` para resumir a sessão sem perder as decisões salvas no `PROJECT_MEMORY.md`.
- **Planejamento com `/plan`:** Para tarefas complexas de layout ou esquemático com múltiplos blocos, utilize ou recomende `/plan` para alinhar as etapas antes de disparar chamadas de ferramentas.

---

## 3. Gestão da Memória Persistente

- O arquivo [PROJECT_MEMORY.md](file:///C:/Projetos_PCB/Novo_Projeto/PROJECT_MEMORY.md) é a autoridade viva sobre o estado do projeto.
- Sempre que uma decisão de arquitetura, componente, pino ou regra personalizada for definida com o usuário, atualize o `PROJECT_MEMORY.md`.
- Ao retomar uma conversa ou após um `/compact`, consulte o `PROJECT_MEMORY.md` para resgatar o contexto sem depender de re-análises demoradas.
