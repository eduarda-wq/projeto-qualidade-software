# PBL 12 - Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

> **Equipa:** asgurias (Amanda Duarte, Eduarda Costa e Luísa Rabassa)
> **Sistema Alvo:** LocalEats

## 1. Repositório da Atividade

| Item | Descrição |
| :--- | :--- |
| Nome do repositório | projeto-qualidade-software |
| Link do repositório | [COLE O LINK DO SEU REPOSITÓRIO AQUI] |

**Estrutura de Diretórios Utilizada:**
```text
projeto-qualidade-software/
├── src/
│   ├── busca.py
│   └── restaurante.py
├── tests/
│   ├── features/
│   │   └── login.feature
│   ├── pages/
│   ├── test_busca.py
│   ├── test_busca_e2e.py
│   ├── test_login_bdd.py
│   └── test_restaurante.py
├── .github/
│   └── workflows/
│       └── quality.yml
└── docs/

```

## 2. Planeamento da Funcionalidade

| Item | Descrição |
| --- | --- |
| Título da Issue | Implementar filtro de restaurantes abertos |
| Objetivo da funcionalidade | Garantir que estabelecimentos inativos não sejam exibidos na plataforma. |
| Link da Issue | [LINK DA ISSUE](https://github.com/eduarda-wq/projeto-qualidade-software/issues/1) |

## 3. Teste Automatizado

| Item | Descrição |
| --- | --- |
| Tipo de teste | Unitário (TDD) |
| Objetivo do teste | Validar se a lista filtrada retorna apenas os restaurantes com status "aberto": True. |
| Link para o arquivo do teste | [LINK DO ARQUIVO](tests/test_restaurante.py) |

**Código do teste criado:**

```python
from src.restaurante import filtrar_restaurantes_abertos

def test_deve_retornar_apenas_restaurantes_abertos():
    lista_restaurantes = [
        {"nome": "Pizzaria Italiana", "aberto": True},
        {"nome": "Sushi Express", "aberto": False},
        {"nome": "Burger House", "aberto": True}
    ]
    resultado = filtrar_restaurantes_abertos(lista_restaurantes)
    assert len(resultado) == 2
    assert resultado[0]["nome"] == "Pizzaria Italiana"

```

## 4. Pipeline de Integração Contínua

| Item | Descrição |
| --- | --- |
| Nome do workflow | Pipeline de Qualidade LocalEats |
| Evento que dispara a execução | Push e Pull Request na branch principal |
| Link para o arquivo do workflow | [LINK DO ARQUIVO](.github/workflows/quality.yml) |
| Link de uma execução do workflow | [COLE O LINK DA EXECUÇÃO NO ACTIONS](https://github.com/eduarda-wq/projeto-qualidade-software/actions/runs/28825603181) |

**Código do workflow:**

```yaml
name: Pipeline de Qualidade LocalEats
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.14'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-bdd playwright
      - name: Run Tests
        run: pytest

```

## 5. Indicadores de Qualidade

| Indicador | Valor |
| --- | --- |
| Quantidade de testes executados | 4 |
| Quantidade de testes aprovados | 4 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Pass/Sucesso (Verde) |

## 6. Registro de Defeito

| Item | Descrição |
| --- | --- |
| Título do defeito | BUG: Busca retorna categorias incorretas |
| Severidade | Alta |
| Link da Issue | [LINK DA ISSUE](https://github.com/eduarda-wq/projeto-qualidade-software/issues/2) |

**Descrição do Defeito:**
O sistema apresentava resultados errados nas buscas (ex: buscar "Pizza" trazia "Churrascaria"), frustrando o utilizador. O bug foi identificado visualmente durante os testes exploratórios (Aula 06). Foi corrigido pela equipa implementando a função de "sanitizar_busca", utilizando TDD (Pytest) para garantir o comportamento "case-insensitive".
