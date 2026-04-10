# Diagnóstico de Qualidade – Startup Local Eats

> Disciplina: Qualidade de Software
> Aula 2 – Atributos de qualidade da ISO 25000
> Equipe: asgurias
> Integrantes: Amanda Duarte, Eduarda Costa e Luísa Rabassa

---

## Análise de Qualidade

| Problema identificado | Atributo de qualidade afetado | Justificativa técnica |
| :--- | :--- | :--- |
| O sistema fica lento em horários de pico | **Eficiência de Desempenho** (Comportamento em tempo) | O tempo de resposta elevado prejudica a UX e indica problemas de escalabilidade na arquitetura para lidar com alta concorrência de requisições. |
| Algumas telas são confusas e pouco intuitivas | **Usabilidade** (Estética da interface / Apreensibilidade) | A falta de clareza visual dificulta que novos usuários engajem na plataforma e dificulta os antigos a realizarem tarefas simples.|
| Certas buscas retornam resultados incorretos | **Adequação Funcional** (Acurácia funcional) | O sistema falha em entregar o resultado correto conforme a regra de negócio, o que quebra a confiança do usuário na confiabilidade da busca. |
| O aplicativo apresenta falhas em determinados modelos de smartphone | **Compatibilidade** (Coexistência) ou **Portabilidade** | O software não consegue executar suas funções adequadamente em diferentes ambientes de hardware/software, limitando a base de usuários. |
| Usuários encontram dificuldade para concluir ações simples | **Usabilidade** (Operabilidade) | A navegação possui gargalos que geram retrabalho e frustração, impedindo que o usuário atinja seus objetivos com facilidade. |
| Avaliações desaparecem após atualização da página | **Confiabilidade** (Maturidade) / **Adequação Funcional** | A perda de informações no front-end ou falha na persistência no banco de dados indica defeitos graves na estabilidade e integridade dos dados da aplicação. |
| Há inconsistências entre a versão web e a versão mobile | **Adequação Funcional** / **Usabilidade** | A discrepância de comportamento ou de features entre plataformas confunde o usuário e prejudica a padronização e a identidade do sistema. |