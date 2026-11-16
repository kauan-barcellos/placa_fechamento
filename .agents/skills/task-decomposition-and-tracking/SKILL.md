---
name: task-decomposition-and-tracking
description: >-
  Decomposicao atomica de tarefas e rastreamento persistente de progresso via checklist vivo.
  Use em solicitacoes de multiplos passos para estruturar o roadmap, evitar esquecimento de etapas e reportar status claro.
---

# Atomic Task Decomposition & Live Progress Tracking

Esta skill orienta a decomposição sistemática de solicitações complexas em tarefas atômicas e rastreáveis, mantendo um checklist vivo de execução para eliminar a perda de contexto (*attention drift*) em conversas longas.

---

## 1. Princípios de Decomposição Atômica

1. **Fatiamento Vertical (Vertical Slicing):**
   - Cada subtarefa deve produzir um resultado funcional e testável de ponta a ponta, e não apenas uma camada incompleta.
2. **Definição de Pronto (Definition of Done):**
   - Cada item do checklist deve ter uma condição objetiva de sucesso (ex: *"Teste automatizado verde"*, *"Arquivo gerado e validado"*, *"Commit registrado"*).
3. **Limite de Escopo:**
   - Evitar tarefas com mais de 5 subtarefas simultâneas sem marcos intermediários. Agrupar em fases se o volume for extenso.

---

## 2. Padrão de Comunicação do Checklist Vivo

Sempre que executar uma sequência com 3 ou mais etapas:

1. **Apresentar o Roadmap Inicial:**
   ```markdown
   ### Plano de Execução da Tarefa
   - [ ] 1. Isolar dados de entrada e validar dependências
   - [ ] 2. Implementar módulo principal com testes
   - [ ] 3. Executar validação de conformidade e auto-auditoria
   - [ ] 4. Gerar documentação e registrar commit
   ```
2. **Atualização Dinâmica de Status:**
   - Ao concluir uma etapa, marque `- [x]` e informe o resultado em 1 linha executiva.
   - Em caso de bloqueio ou erro, indique imediatamente o item afetado e a causa técnica.
