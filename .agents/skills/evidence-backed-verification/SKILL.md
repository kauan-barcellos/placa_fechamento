---
name: evidence-backed-verification
description: >-
  Protocolo de verificacao empírica obrigatoria ("Deployed is not verified") para entregas de hardware e software.
  Use ao concluir qualquer bloco de circuito ou layout antes de declarar a tarefa como finalizada ao usuario.
---

# Evidence-Backed Verification Protocol

Esta skill estabelece a proibição absoluta de declarações de conclusão sem comprovação objetiva no projeto. O agente não pode afirmar que um esquemático ou PCB está finalizado sem apresentar evidências numéricas e visuais reproduzíveis.

---

## 1. A Tríade da Evidência Obrigatória

Toda entrega de etapa de circuito deve conter no relatório de resposta a **Tríade de Evidência**:

1. **Evidência Elétrica (ERC):**
   - Execução documentada de `run_erc` com retorno explícito de `0 erros` e `0 avisos`.
2. **Evidência Física e DFM (DRC):**
   - Execução documentada de `run_drc` com retorno explícito de `0 violações`, `0 pads desconectados` e `0 áreas isoladas`.
3. **Evidência Visual (Previews Vetoriais):**
   - Execução do script `generate_previews.py` e fornecimento de links diretos clicáveis para inspeção pelo usuário:
     - [Esquemático Atualizado](file:///C:/Projetos_PCB/Novo_Projeto/docs/previews/schematic/placa_fechamento.svg)
     - [PCB Camada Superior (Top)](file:///C:/Projetos_PCB/Novo_Projeto/docs/previews/pcb_top.svg)
     - [PCB Camada Inferior (Bottom)](file:///C:/Projetos_PCB/Novo_Projeto/docs/previews/pcb_bottom.svg)

---

## 2. Tabela de Resumo de Métricas Reais

Em entregas de bloco funcional, apresente uma matriz concisa:

| Métrica | Valor Obtido | Status |
| :--- | :--- | :--- |
| **Componentes Ativos / Passivos** | N componentes | Conforme BOM |
| **Nets / Airwires Pendentes** | 0 pendentes | 100% Roteado |
| **Violações de Folga (< 0.15 mm)** | 0 violações | DFM JLCPCB OK |
| **Integridade de Furação e Vias** | 0 erros de anel | Furos $\ge 0.30\text{ mm}$ |
| **Checkpoint Git** | Commit em pt-BR gerado | Sincronizado |
