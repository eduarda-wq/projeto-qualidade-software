# Estratégia Inicial de Testes - LocalEats

**Integrantes:** Eduarda, Amanda e Luísa

## 1. Funcionalidades Principais e Priorização
Identificamos as funcionalidades críticas baseando-nos no impacto direto na experiência do utilizador e na conversão de vendas:

1.  **Motor de Busca:** Crítico para resolver o problema de resultados irrelevantes.
2.  **Checkout e Finalização de Pedido:** Vital para o negócio; qualquer falha aqui impede a receita.
3.  **Login e Sessão:** Necessário para manter o utilizador autenticado e evitar erros de permissão.
4.  **Sistema de Avaliações:** Foco em corrigir a persistência de dados (evitar que sumam após refresh).

## 2. Análise de Risco (RBT - Risk Based Testing)
| Funcionalidade | Risco Identificado | Impacto | Prioridade |
| :--- | :--- | :--- | :--- |
| **Checkout** | Falha técnica impede a conclusão da compra. | Alto | Crítica |
| **Busca** | Resultados incorretos geram desconfiança na plataforma. | Alto | Alta |
| **Performance** | Lentidão em picos causa abandono do site/app. | Médio | Alta |
| **Favoritos** | Erro funcional incomoda, mas não impede a compra. | Baixo | Baixa |

## 3. Estratégia de Pirâmide de Testes
Decidimos distribuir o esforço de teste da seguinte forma para otimizar custos e velocidade:
* **Testes Unitários (60%):** Validar as funções de filtro de busca e lógica de cálculo de preços de forma isolada.
* **Testes de Integração (30%):** Garantir que a comunicação entre o Frontend e a API de avaliações não perca dados.
* **Testes E2E (10%):** Simular o fluxo completo: "Turista busca restaurante -> Seleciona prato -> Finaliza pedido".

## 4. Testes em Produção
Propomos o uso de **Feature Flags** para testar o novo algoritmo de busca com 5% dos utilizadores. Além disso, as evidências coletadas (ver pasta de artefatos) demonstram que o monitoramento de erros em tempo real é urgente para mitigar a lentidão relatada nos horários de pico.