# Estratégia Inicial de Testes - LocalEats

**Integrantes:** Eduarda, Amanda e Luísa

## 1. Funcionalidades Críticas e Priorização
Com base nos problemas relatados (lentidão, busca incorreta e falhas mobile), priorizamos:

1. **Busca de Restaurantes:** Alta Prioridade. É a porta de entrada do usuário; falhas aqui geram abandono imediato.
2. **Finalização de Pedido (Checkout):** Crítica. Qualquer erro aqui impede o faturamento dos restaurantes parceiros.
3. **Login e Cadastro:** Alta Prioridade. Essencial para a personalização e segurança dos dados.
4. **Sistema de Avaliações:** Média Prioridade. Foco em corrigir a persistência de dados (bug do refresh).

## 2. Análise de Risco
* **Risco Técnico:** Lentidão em horários de pico (escala).
* **Risco de Negócio:** Resultados de busca irrelevantes diminuem a confiança dos comerciantes locais.
* **Risco de UI:** Inconsistência entre Web e Mobile prejudica a imagem da marca.

## 3. Pirâmide de Testes
Nossa estratégia foca na automação eficiente:
* **Testes Unitários (60%):** Validar isoladamente os filtros de busca e lógica de cálculo de frete. São rápidos e garantem que o "coração" do código funcione.
* **Testes de Integração (30%):** Garantir que a API de avaliações se comunique corretamente com o banco de dados para evitar perda de dados.
* **Testes E2E (10%):** Validar apenas os fluxos críticos de compra, simulando um usuário real desde a busca até o pagamento.

## 4. Testes em Produção
Propomos o uso de **Feature Flags** (lançamento gradual) para novas versões da busca e **Monitoramento Ativo (Sentry)** para capturar erros de timeout em tempo real durante os horários de pico, permitindo uma resposta rápida da equipe técnica.