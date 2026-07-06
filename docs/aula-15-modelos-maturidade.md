# PBL 10 - Modelos de Maturidade

> **Equipa:** asgurias (Amanda Duarte, Eduarda Costa e Luísa Rabassa)
> **Sistema Alvo:** LocalEats

## 1. Diagnóstico de Maturidade

| Critério | Sim | Parcial | Não |
| :--- | :---: | :---: | :---: |
| Os requisitos são documentados? | | X | |
| Existe controle de mudanças? | X | | |
| Há atividades de teste definidas? | X | | |
| Os defeitos são registrados? | | X | |
| O processo de desenvolvimento é conhecido por toda a equipe? | X | | |
| As tarefas são planejadas e acompanhadas regularmente? | | X | |
| Existe padronização para implementação de funcionalidades? | X | | |
| Os testes são executados antes da entrega das funcionalidades? | X | | |
| Há revisão de código ou validação por outro integrante da equipe? | | X | |
| A equipe utiliza ferramentas para gerenciamento das atividades? | X | | |
| Os artefatos do projeto são organizados e versionados? | X | | |
| Existe rastreabilidade entre requisitos e funcionalidades implementadas? | | X | |
| A equipe realiza reuniões de retrospectiva para identificar melhorias? | | | X |
| Existem indicadores ou métricas para acompanhar a qualidade do projeto? | | X | |

**Classificação Atual: Nível 2 - Gerenciado (MPS.BR / CMMI)**
**Justificação:** O processo da LocalEats abandonou o nível Inicial (Ad-hoc), pois agora a equipa planeia testes, utiliza automação (TDD/BDD) e efetua o versionamento (Git). No entanto, não atinge o Nível 3 (Definido) por faltar maior rigor na documentação, rastreabilidade completa de requisitos, métricas robustas de gestão e rotinas formais de melhoria contínua (como retrospetivas).

## 2. Identificação de Lacunas

| Lacuna | Impacto |
| :--- | :--- |
| **Falta de métricas e rastreabilidade** | Dificulta a medição exata do impacto dos defeitos e a cobertura real dos testes frente aos requisitos. |
| **Ausência de Integração Contínua (CI)** | Testes são executados localmente, permitindo que código falho seja inserido no repositório por lapso humano. |
| **Falta de Retrospetivas** | A equipa não possui um momento formal para debater falhas de processo, limitando a melhoria contínua. |

## 3. Propostas de Melhoria

| Melhoria | Benefício |
| :--- | :--- |
| **Implementar GitHub Actions (CI)** | Automatização das validações de TDD e BDD a cada push, bloqueando regressões. |
| **Formalizar Issues e Labels no GitHub** | Criar um padrão de rastreabilidade (User Stories ligadas a Commits e PRs) para gestão de defeitos. |
| **Realizar Sprint Retrospectives** | Criar um ciclo de feedback constante para rever os processos da equipa e adotar boas práticas colaborativas. |