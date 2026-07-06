# PBL 11 - Qualidade em Metodologias Ágeis

> **Equipa:** asgurias (Amanda Duarte, Eduarda Costa e Luísa Rabassa)
> **Sistema Alvo:** LocalEats

## 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
| :--- | :---: | :--- | :--- |
| Planeamento iterativo | Parcial | O desenvolvimento decorre por PBLs (entregas focadas). | Adotar Sprints curtas (Scrum). |
| Priorização de funcionalidades | Sim | Baseado na criticidade (ex: busca e login). | Usar uma matriz de valor/esforço. |
| Entregas incrementais | Sim | Entrega de automação camada a camada (Unitária -> E2E). | Automatizar o deploy (CI/CD). |
| Feedback frequente | Parcial | Feedback concentrado na revisão do professor. | Fazer Dailies ou revisões com stakeholders. |
| Trabalho colaborativo | Sim | Equipa gere e consolida o código via Git. | Adotar Pair Programming (XP). |
| Controle visual das atividades | Parcial | Uso básico de repositórios. | Utilizar GitHub Projects (Kanban). |
| Melhoria contínua | Parcial | Refatoração de código com TDD. | Realizar Retrospectivas formais. |

**Conclusão:**
O processo tem pontos fortes no desenvolvimento técnico iterativo, especialmente devido à adoção precoce de TDD e automação, típicos do Extreme Programming (XP). Contudo, a organização e o fluxo ágil (gestão visual e cerimónias) são as principais lacunas. O processo carece de mecanismos visuais de gestão e de rotinas de feedback rápido, impedindo uma verdadeira colaboração cross-funcional.

## 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
| :--- | :--- | :--- |
| **Adotar um quadro Kanban (GitHub Projects)** | Kanban | Maior visibilidade do andamento das atividades, limitando o WIP (Work In Progress). |
| **Pair Programming em código crítico** | XP (Extreme Programming) | Reduzir defeitos e partilhar conhecimento de domínio, essencial no TDD. |
| **Realizar Reuniões Diárias (Daily)** | Scrum | Identificar rapidamente impedimentos (blocos) da equipa. |
| **Redução de Desperdícios (Lean)** | Lean Software Development | Eliminar passos manuais repetitivos automatizando fluxos no repositório. |

## 3. Definition of Ready (DoR)
Critérios para que uma tarefa esteja pronta para iniciar o desenvolvimento:
1. O requisito possui critérios de aceitação claramente definidos e acordados.
2. A dependência técnica (ex: APIs e endpoints) está mapeada.
3. O design de interface (UI/UX) correspondente (se aplicável) está disponível.
4. A tarefa foi estimada pela equipa.
5. A "Issue" está registada no GitHub com todas as informações necessárias.

## 4. Definition of Done (DoD)
Critérios para considerar uma funcionalidade 100% concluída:
1. O código foi implementado e está versionado na "branch" principal.
2. Os testes unitários (TDD) e E2E/BDD foram criados e passaram com sucesso.
3. Não existem linter errors ou falhas apontadas no pipeline de CI.
4. A funcionalidade atende a todos os critérios de aceitação estipulados no DoR.
5. A funcionalidade foi validada na interface da aplicação sem quebrar o layout (Mobile/Desktop).