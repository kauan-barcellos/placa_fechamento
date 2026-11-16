---
name: systematic-code-reviewer
description: >-
  Revisor critico adversarial de codigo, scripts e configuracoes antes do commit.
  Use ao finalizar qualquer implementacao para auditar casos de borda, complexidade, vazamento de recursos e seguranca.
---

# Systematic & Adversarial Code Reviewer

Esta skill define o protocolo de auto-auditoria crítica que o agente deve aplicar sobre qualquer código, script ou diff gerado antes de submetê-lo ou apresentá-lo como concluído.

---

## 1. A Matriz dos 5 Pilares de Revisão

Todo diff gerado deve ser inspecionado ativamente contra as 5 categorias de vulnerabilidade e débito técnico:

| Pilar | Foco de Inspeção | Sintomas Críticos a Corrigir |
| :--- | :--- | :--- |
| **1. Casos de Borda e Entradas** | Validação de limites e tipos | Falta de verificação de `None`/nulo, listas vazias, divisões por zero, strings com caracteres especiais. |
| **2. Concorrência e Processos** | Isolamento e travamentos | Processos sem `timeout`, locks sem context manager (`with`), variáveis compartilhadas não thread-safe. |
| **3. Recursos do Sistema** | Ciclo de vida de I/O | Arquivos, sockets ou conexões de banco de dados sem fechamento garantido no bloco `finally`. |
| **4. Complexidade e Design** | Princípio da Responsabilidade Única | Funções acumulando múltiplas responsabilidades (*god functions*), aninhamento de `if/else` superior a 3 níveis. |
| **5. Segurança e Robustez** | Superfície de ataque | Execução de shell sem escape seguro, injeção de comandos, caminhos com concatenação manual de strings. |

---

## 2. Protocolo de Ação Pré-Commit

1. **Auto-Crítica Ativa:** Não pergunte "o que está certo?", mas sim: *"Se este código falhar em produção daqui a 3 meses, qual será a causa raiz?"*.
2. **Correção Silenciosa:** Se um caso de borda for detectado durante a revisão, refatore imediatamente o código antes de entregar ao usuário.
3. **Resumo Executivo:** Informe apenas as proteções adicionadas (ex: `✓ Inserido timeout de 15s e tratamento de FileNotFoundError`).
