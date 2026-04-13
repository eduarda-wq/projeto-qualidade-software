# Planejamento e Execução de Testes - LocalEats

**Sistema Alvo:** [LocalEats Vercel](https://local-eats-unisenac.vercel.app/)
**Integrantes:** Eduarda, Amanda e Luísa

## 1. Plano de Testes
* **Objetivo:** Validar a funcionalidade de busca e a responsividade mobile.
* **Escopo:** Busca, Detalhes do Restaurante e Layout.
* **Ferramenta:** Google Chrome DevTools (Inspeção e Simulação Mobile).

## 2. Registro de Execução e Evidências

| ID | Caso de Teste | Status | Observações | Evidência |
| :--- | :--- | :--- | :--- | :--- |
| **CT-01** | Busca por Culinária | **FALHOU** | Resultados irrelevantes (Busca 'Pizza' trouxe 'Churrascaria'). | ![Busca](../artefatos/evidencias/busca_incorreta.png) |
| **CT-02** | Responsividade (Login) | **FALHOU** | Botões sobrepostos e textos cortados no mobile. | ![Layout 1](../artefatos/evidencias/layout_mobile_quebrado_01.png) |
| **CT-03** | Menu Mobile | **FALHOU** | Dificuldade em clicar nos campos de busca. | ![Layout 2](../artefatos/evidencias/layout_mobile_quebrado_02.png) |
| **CT-04** | Inspeção Técnica | **ANALISADO** | Identificados erros de rede (404/500) e lentidão na API. | ![Técnico](../artefatos/evidencias/inspecao_tecnica.png) |

## 3. Análise de Resultados
Os testes confirmam que os problemas relatados pelos usuários são reais e críticos. A falha de busca (CT-01) desmoraliza a função principal do sistema. As falhas de layout (CT-02 e CT-03) tornam o aplicativo inutilizável para turistas que dependem do mobile.

## 4. Recomendações de QA
Recomendamos a priorização da correção das *Media Queries* no CSS para dispositivos móveis e a refatoração da lógica de busca no backend para garantir que as categorias de restaurantes sejam respeitadas.