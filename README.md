# Placa de Fechamento - Hardware & PCB Design

[![KiCad Version](https://img.shields.io/badge/KiCad-10.0-blue.svg)](https://www.kicad.org/)
[![Manufacturing Standard](https://img.shields.io/badge/DFM-JLCPCB%202--Layer-orange.svg)](https://jlcpcb.com/)
[![License](https://img.shields.io/badge/Status-In%20Development-yellow.svg)]()

Projeto de hardware e circuito impresso (PCB) desenvolvido para alta confiabilidade industrial, seguindo rigorosos padrões de **Design for Manufacturing (DFM)** e **Design for Assembly (DFA)** da JLCPCB (2 camadas, 1 oz Cu).

---

## 📁 Estrutura do Repositório

```text
├── .gitignore                  # Regras de exclusão e retenção de arquivos KiCad / Git
├── GEMINI.md                   # Diretrizes técnicas completas de DFM, EMC, Net Classes e MCP
├── README.md                   # Visão geral e documentação do projeto
├── placa_fechamento.kicad_pro  # Arquivo principal do projeto KiCad 10.0
├── placa_fechamento.kicad_sch  # Esquemático elétrico em blocos lógicos
├── placa_fechamento.kicad_pcb  # Layout de circuito impresso 2 camadas
├── docs/                       # Documentação técnica, pinouts e especificações
│   └── README.md
├── libraries/                  # Símbolos, pegadas (footprints) e modelos 3D locais
│   └── README.md
└── fabrication/                # Arquivos prontos para produção (Gerbers, BOM, CPL, PDFs)
    └── README.md
```

---

## ⚙️ Especificações de Engenharia e DFM (JLCPCB 2 Camadas)

| Parâmetro | Valor de Projeto | Observação |
| :--- | :--- | :--- |
| **Camadas** | 2 camadas (F.Cu / B.Cu) | Espessura 1.6 mm / 1 oz (35 µm) |
| **Largura de Trilha (Sinais)** | 0.15 mm a 0.20 mm | 6 a 8 mil |
| **Largura de Trilha (Potência)** | 0.50 mm a 1.50 mm | Dimensionada por corrente (IPC-2152) |
| **Isolamento Mínimo (Clearance)** | 0.15 mm a 0.20 mm | Cobre-cobre, pad-trilha, pad-pad |
| **Vias Padrão (Sinais)** | Furo 0.30 mm / Diâmetro 0.60 mm | Anel anular de 0.15 mm |
| **Vias de Potência** | Furo 0.40 mm / Diâmetro 0.80 mm | Suporta ~1.5A contínuos |
| **Plano de Terra** | Contínuo em B.Cu e preenchimento em F.Cu | Malha de stitching vias com passo de 4.0 mm |
| **Integridade de Sinal / ESD** | TVS in-line (*Flow-Through*) | Capacitores de desacoplamento < 2.0 mm dos CIs |

Para a especificação técnica integral, consulte o documento [GEMINI.md](file:///C:/Projetos_PCB/Novo_Projeto/GEMINI.md).

---

## 🛠️ Ferramentas e Automação

- **Software CAD:** KiCad 10.0
- **Automação & Verificação:** KiCad MCP Server (integração programática com ferramentas de ERC/DRC)
- **Critério de Aceitação:** 0 erros no ERC do esquemático e 0 violações no DRC do layout antes de cada release.
