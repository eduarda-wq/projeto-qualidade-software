# Diagnóstico de Qualidade – Startup Local Eats

> Disciplina: Qualidade de Software  
> Aula 3 – Papéis, Responsabilidades e Práticas de QA  
> Equipe: asgurias
> Integrantes: Amanda Duarte e Eduarda Costa 

---

# 1. Diagnóstico da Situação Atual

## 1.1 Papéis atuais identificados

Liste quais papéis vocês acreditam que existem atualmente na startup.

- Desenvolvedores: Focados em "codar" funcionalidades, mas sem um processo de teste estruturado.
- Gestão de Produto/Negócio: Pressionando por crescimento rápido ("hipercrescimento"), possivelmente negligenciando a estabilidade.
- Suporte/Operações: Provavelmente lidando com o "caos técnico" e reclamações de usuários em produção.

---

## 1.2 Quem é responsável pela qualidade hoje?

Descreva como vocês acreditam que a qualidade está sendo tratada atualmente.

> Atualmente, a qualidade parece ser reativa e não preventiva. Responsabilidade diluída entre desenvolvedores que entregam código com falhas críticas para produção. A qualidade é tratada como um "acidente" ou algo a ser verificado apenas após o erro ocorrer, caracterizando um estado de caos técnico.

---

## 1.3 Problemas identificados

Liste os principais problemas relacionados à falta de organização da qualidade.

- Falhas Críticas em Produção: O sistema apresenta erros severos que impedem o uso básico.
- Instabilidade no Checkout: Processo de finalização de compra interrompido ("Checkout Quebrado").
- Erros de Pagamento: Falhas no processamento financeiro, impactando diretamente a receita.
- Performance Degradada: Carregamento lento das páginas e funcionalidades.

---

## 1.4 Impactos desses problemas

Explique quais são as consequências desses problemas para o sistema e para os usuários.

> O Prejuízo financeiro, que por conta das falhas como o "Checkout Quebrado" e o "Erro de Pagamento" impedem a conclusão das vendas, impactando a receita imediata da plataforma, a degradação da experiência do usuário como problemas de "Carregamento Lento" e "Falha no Sistema" geram frustração, reduzindo os índices de satisfação que a empresa busca manter e a incerteza operacional com a falta de estabilidade comprometendo a confiança no ecossistema da LocalEats.

---

## 1.5 A qualidade é responsabilidade de quem?

Explique se a qualidade deve ser responsabilidade de uma pessoa ou de toda a equipe.

> A qualidade não é um acidente, é um método que deve ser compartilhado por toda a equipe, indo além de apenas achar bugs para garantir a confiança no sistema. Ela envolve o compromisso de engenheiros de qualidade, desenvolvedores e gestores em diagnosticar falhas e reestruturar processos , utilizando ferramentas como TDD e BDD para criar uma especificação executável e um código manutenível. Assim, a responsabilidade estende-se desde o planejamento e design até a automação e o monitoramento contínuo em produção.

---

# 2. Papéis da Equipe Propostos

Definam quais papéis deveriam existir na equipe da Local Eats.

---

## 2.1 Lista de papéis

- Engenheiro de Qualidade
- Desenvolvedor
- Analista de Testes

---

## 2.2 Descrição dos papéis

Preencha a tabela abaixo:

| Papel | Responsabilidades principais | Relação com a qualidade |
|------|------|------|
|Engenheiro de Qualidade|Diagnosticar falhas, estruturar processos e automação de confiança|Garante a engenharia da confiança e estabilidade do ecossistema|
|Desenvolvedor |Implementar funcionalidades e realizar testes unitários/TDD|Responsável pela qualidade estrutural e correção do código|
|Analista de Testes |Elaborar casos de teste focados em regras de negócio e testes manuais|Garante que o produto atende às necessidades do usuário final|

---

# 3. Práticas de QA Sugeridas

Sugira práticas que a startup pode adotar para melhorar a qualidade.

---

## 3.1 Lista de práticas

- Implementação de TDD (Test-Driven Development).
- Adoção de BDD (Behavior-Driven Development).
- Pipeline de CI/CD com Critérios de Aprovação.
- Gestão de Defeitos e Métricas.

---

## 3.2 Explicação das práticas

Explique brevemente cada prática sugerida.

### Prática 1: TDD (Test-Driven Development)
> Utilizar o ciclo Red-Green-Refactor, onde o teste é escrito antes do código funcional, garantindo código manutenível e testado desde a origem.

### Prática 2: BDD (Behavior-Driven Development)
> Criar especificações executáveis em linguagem Gherkin (Given-When-Then), alinhando o entendimento entre negócio, desenvolvimento e testes.

### Prática 3: Automação de Interface e API
> Implementar testes funcionais automatizados utilizando o padrão Page Object Model para reduzir regressões e aumentar a velocidade de feedback.

---

# 4. Anúncios de Contratação

A startup decidiu contratar novos profissionais. Crie anúncios de vagas.

> Mínimo: 2 vagas

---

## 4.1 Vaga 1 – Engenheiro de QA (Automação)

### Descrição da vaga
> Responsável por elevar a maturidade dos processos da Local Eats seguindo padrões internacionais de qualidade.

### Responsabilidades
- Realizar diagnóstico baseado na norma ISO/IEC 25000.
- Gerir o ciclo de vida de defeitos, analisando severidade e prioridade.
- Monitorar indicadores de densidade de defeitos e maturidade.

### Requisitos obrigatórios
- Experiência em planejamento de testes e elaboração de casos de teste.

- Domínio de modelos de maturidade de software.

- Habilidade em análise estatística e métricas de qualidade.


### Requisitos desejáveis
- Conhecimento em auditorias técnicas.

- Familiaridade com normas ISO de qualidade de produto.


### Certificações desejáveis
- 

---

## 4.2 Vaga 2 – Analista de Qualidade e Processos

### Descrição da vaga
> Responsável por elevar a maturidade dos processos da Local Eats seguindo padrões internacionais de qualidade.

### Responsabilidades
- Realizar diagnóstico baseado na norma ISO/IEC 25000.
- Gerir o ciclo de vida de defeitos, analisando severidade e prioridade.
- Monitorar indicadores de densidade de defeitos e maturidade 


### Requisitos obrigatórios
- Experiência em planejamento de testes e elaboração de casos de teste.

- Domínio de modelos de maturidade de software.

- Habilidade em análise estatística e métricas de qualidade.


### Requisitos desejáveis
- Conhecimento em auditorias técnicas.

- Familiaridade com normas ISO de qualidade de produto.


### Certificações desejáveis
- 

---

# 5. Conclusão da Equipe

Descreva brevemente:

- O que a equipe aprendeu com a atividade
- Principais dificuldades encontradas
- Principais melhorias propostas para a startup

> Com a realização desta atividade, a equipe compreendeu que a qualidade de software não é um evento acidental, mas sim um método rigoroso e estruturado que deve permear todo o ciclo de desenvolvimento. Identificamos que o cenário de "caos técnico" da LocalEats, marcado por falhas críticas em produção como checkouts quebrados e erros de pagamento, exige uma transição imediata para a "Engenharia da Confiança". As principais dificuldades residiram em diagnosticar como uma startup em hipercrescimento pode reestruturar seus papéis de QA sem interromper sua agilidade. Como solução, propusemos a implementação de uma pirâmide de testes baseada em TDD e BDD, além da adoção de modelos de maturidade como CMMI e ISO 25000 para garantir que o produto final seja estável, usável e verdadeiramente focado nas necessidades do usuário.

---

