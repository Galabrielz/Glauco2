# Refatoração do Problema da Mochila com Algoritmo Genético

## Análise do Código Original

- **Pontos Identificados para Melhorias:**
  - Código altamente procedural, sem organização orientada a objetos.
  - Código duplicado nas funções de teste para diferentes tamanhos de entrada.
  - Alta coesão entre funções, mas baixo encapsulamento.
  - Ausência de testes automatizados.
  - Funções com parâmetros excessivos.
  - Falta de separação entre lógica do algoritmo e lógica de execução de testes.

## Planejamento da Refatoração

- **O que será refatorado:**
  - Encapsular o algoritmo em uma classe.
  - Remover duplicação nos testes.
  - Implementar testes unitários com pytest.
  - Melhorar nomeação de variáveis e funções.
  - Modularizar o código.

- **Por que será refatorado:**
  - Melhorar legibilidade, manutenibilidade e escalabilidade do código.
  - Permitir reaproveitamento e expansão do algoritmo.
  - Permitir testes automatizados para garantir qualidade.

- **Técnicas Utilizadas:**
  - **Encapsulate Function** (Refactoring Guru)
  - **Extract Class** (Martin Fowler)
  - **Rename Method** (Refactoring Guru)
  - **Parameter Object** (Refactoring Guru)
  - **Remove Duplicate Code** (Refactoring Guru)

## Ferramentas de Apoio

- pylint
- flake8
- pytest
- ChatGPT
