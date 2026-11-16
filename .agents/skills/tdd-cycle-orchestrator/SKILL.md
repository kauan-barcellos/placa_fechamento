---
name: tdd-cycle-orchestrator
description: >-
  Orquestrador de desenvolvimento orientado a testes (TDD - Test-Driven Development).
  Use ao implementar modulos, scripts e logica de negocio para assegurar o ciclo Red-Green-Refactor e cobertura empirica.
---

# Test-Driven Development (TDD) Cycle Orchestrator

Esta skill impõe o ciclo rigoroso de desenvolvimento orientado a testes, proibindo a entrega de código funcional sem que haja testes automatizados demonstrando a transição do estado de falha para o estado de sucesso.

---

## 1. O Ciclo Inegociável Red-Green-Refactor

```
[1. RED: Escrever Teste que Falha] ──► [2. GREEN: Código Mínimo que Passa] ──► [3. REFACTOR: Limpar e Otimizar]
                ▲                                                                             │
                └────────────────────────── Próximo Requisito ────────────────────────────────┘
```

1. **Fase RED (Falha Comprovada):**
   - Escrever um teste automatizado focado no comportamento observável da função ou módulo.
   - Executar o teste e comprovar que ele **falha exatamente pelo motivo esperado** (ex: `NameError`, asserção de retorno incorreto).
2. **Fase GREEN (Sucesso Rápido):**
   - Escrever a implementação mínima necessária para satisfazer a asserção do teste.
   - Não adicionar funcionalidades extras ou prever futuros requisitos nessa fase.
   - Executar o teste e certificar que a suíte está verde.
3. **Fase REFACTOR (Design Limpo):**
   - Eliminar duplicações de código, melhorar nomenclatura e extrair funções auxiliares.
   - Re-executar os testes após cada refatoração para garantir que nenhuma regressão foi introduzida.

---

## 2. Princípios de Alta Fidelidade de Testes

- **Testar Comportamento, Não Detalhes Privados:** Os testes devem validar entradas e saídas de contratos públicos, permitindo que a estrutura interna seja refatorada sem quebrar os testes.
- **Isolamento de Efeitos Colaterais:** Testes unitários devem usar diretórios temporários (`tmp_path`) ou mocks de rede para nunca poluir o workspace real do usuário.
