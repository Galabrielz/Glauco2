# Processo de Refatoração

## Estratégia Adotada

- Foi realizado um clone do repositório original em um repositório separado, evitando modificações no código original da outra equipe.

## Etapas Realizadas

1. **Análise:** Estudo detalhado do código recebido, identificando pontos de melhoria.
2. **Planejamento:** Definição de técnicas de refatoração com base em Martin Fowler e Refactoring Guru.
3. **Refatoração:** Criação da classe `GeneticAlgorithmKnapsack`, remoção de código duplicado, aplicação de boas práticas de PEP8.
4. **Testes:** Implementação de testes automatizados com pytest.
5. **Validação:** Execução dos testes para garantir que a refatoração preservou o comportamento correto.
6. **Documentação:** Criação dos arquivos `refatoracao.md` e `processo.md`.

## Ferramentas Utilizadas

- GitHub (clone e versionamento)
- pylint
- flake8
- pytest
- ChatGPT como apoio para sugestões e organização do código

## Desafios e Aprendizados

- Desafio na separação da lógica procedural em estrutura orientada a objetos.
- Aprendizado no uso de ferramentas de análise de código e testes automatizados.
