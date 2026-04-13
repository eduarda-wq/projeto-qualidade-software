# Testes Funcionais vs Estruturais - LocalEats

**Funcionalidade Escolhida:** Busca de Restaurantes por Culinária

## 1. Visão do Utilizador (Teste Caixa-Preta)
Focamos nos requisitos funcionais e na experiência final sem analisar o código interno:
* **Cenário Positivo:** Inserir "Italiana" no campo de busca. **Esperado:** Listagem de pizzarias e cantinas italianas.
* **Cenário de Limite:** Inserir termos muito longos ou com emojis. **Esperado:** O sistema deve sanitizar a entrada e não quebrar o layout.
* **Cenário de Erro:** Busca sem resultados. **Esperado:** Exibir mensagem clara "Nenhum restaurante encontrado para este termo".

## 2. Visão do Desenvolvedor (Teste Caixa-Branca)
Focamos na estrutura lógica e caminhos do código:
* **Cobertura de Decisão:** Testar se o `if` que filtra a categoria é *Case Insensitive* (aceita "pizza" e "PIZZA").
* **Tratamento de Exceções:** Validar se o código possui um `try-catch` para quando o banco de dados demora a responder (Timeout), evitando a "tela branca".
* **Lógica de Ordenação:** Garantir que o loop de resultados prioriza restaurantes abertos sobre os fechados.

## 3. Reflexão Crítica
A análise técnica (evidenciada no print `inspecao_tecnica.png`) sugere que os problemas de "resultados incorretos" decorrem de falhas na lógica de filtragem da API. Enquanto a Caixa-Preta valida se o utilizador está satisfeito, a Caixa-Branca é o que permitirá à equipa encontrar o erro de lógica no backend que mistura categorias de restaurantes.