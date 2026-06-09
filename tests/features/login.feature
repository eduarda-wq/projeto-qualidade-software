Feature: Autenticação de Usuário
  Como um cliente do LocalEats
  Desejo fazer login no sistema
  Para acessar minha conta e realizar buscas

  Scenario: Login com credenciais válidas
    Given que eu acesso o sistema LocalEats
    When sou redirecionado para a tela de login
    And preencho o email "amanda@teste.com" e a senha "12345"
    And clico no botão Entrar
    Then devo ser autenticado com sucesso e ver a barra de busca