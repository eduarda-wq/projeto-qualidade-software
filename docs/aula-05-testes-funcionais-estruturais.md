# Testes Funcionais vs Estruturais - LocalEats

**Funcionalidade Escolhida:** Busca de Restaurantes

## 1. Visão do Usuário (Teste Caixa-Preta)
Validamos o comportamento esperado sem acesso ao código:
* **Cenário de Sucesso:** Buscar "Italiana" em "Pelotas". Resultado: Listagem apenas de restaurantes italianos ativos na cidade.
* **Cenário de Erro:** Busca por termos com caracteres especiais ou nulos. Resultado: O sistema deve sanitizar a entrada e não exibir erro de servidor.
* **Cenário de Performance:** Realizar busca simultânea com múltiplos filtros. Resultado: Retorno em menos de 2 segundos.

## 2. Visão do Desenvolvedor (Teste Caixa-Branca)
Validamos a estrutura lógica interna:
* **Lógica de Comparação:** Testar se a query SQL utiliza `LIKE %termo%` e se o código trata diferenças entre maiúsculas e minúsculas (*Case Insensitive*).
* **Cobertura de Fluxo:** Garantir que o `if/else` que valida o status do restaurante (Aberto/Fechado) está funcionando para não exibir locais inativos na busca.
* **Tratamento de Exceções:** Validar se existe um `try-catch` para erros de conexão com o banco de dados, evitando a "tela branca" relatada.

## 3. Reflexão Crítica
O teste de Caixa-Preta é vital para garantir que o morador local encontre o que deseja. No entanto, para resolver o bug de "resultados incorretos", o teste de **Caixa-Branca** é superior, pois permite identificar falhas na lógica de filtragem da API que a visão externa não consegue mapear.