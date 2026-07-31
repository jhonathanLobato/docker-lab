# Docker Intensive — 7 Dias

> **Objetivo:** deixar de apenas usar comandos do Docker para pensar como um engenheiro DevOps ao projetar, construir, executar e manter aplicações containerizadas.

# Sobre este projeto

Este repositório documenta um intensivão de 7 dias focado em aprender Docker da forma que ele é utilizado no mercado.

O objetivo não é decorar comandos, mas compreender:

- Como o Docker funciona internamente.
- Por que determinadas práticas existem.
- Como tomar decisões arquiteturais.
- Como construir ambientes reais.
- Como resolver problemas de infraestrutura.

Ao final do desafio, a expectativa é ser capaz de analisar uma aplicação e responder perguntas como:

- Como essa aplicação deveria ser containerizada?
- Quais serviços precisam existir?
- Como esses serviços se comunicam?
- Onde os dados devem ser persistidos?
- Como essa aplicação seria implantada em produção?
- Quais boas práticas precisam ser aplicadas?

# Filosofia do intensivão

Durante este desafio existe apenas uma regra:

> **Nunca fazer algo apenas porque um tutorial mandou fazer.**

Toda decisão deve responder perguntas como:

- Por quê?
- Existe outra forma?
- Qual problema isso resolve?
- Quais são as vantagens?
- Quais são as desvantagens?
- O que acontece se eu remover essa configuração?

O objetivo não é aprender Docker.

O objetivo é aprender Engenharia utilizando Docker.

# Estrutura dos desafios

Cada desafio possui a seguinte estrutura:

## Contexto

Apresenta uma situação semelhante ao ambiente de uma empresa.

## Problema

Define exatamente o que precisa ser resolvido.

## Restrições

Limitações impostas para evitar soluções prontas e incentivar o aprendizado.

## Desafio

Parte prática onde toda a implementação será realizada.

## Perguntas de Arquitetura

Questões que obrigam a entender o motivo de cada decisão tomada.

## Missão Bônus

Desafios extras para aprofundar o conhecimento.

## Reflexão

Registro dos aprendizados obtidos durante o desafio.

# Organização do repositório

```text
docker-intensive/

│
├── README.md
├── docs/
│
│   ├── dia-01.md
│   ├── dia-02.md
│   ├── dia-03.md
│   ├── dia-04.md
│   ├── dia-05.md
│   ├── dia-06.md
│   ├── dia-07.md
│   │
│   ├── aprendizados.md
│   ├── erros.md
│   ├── arquitetura.md
│   └── decisoes.md
│
├── desafios/
│
├── projetos/
│
└── projeto-final/
```

# Regras do desafio

## Não copiar Dockerfiles prontos

Sempre construir do zero.

## Não decorar comandos

Sempre entender:

- por que existe;
- quando utilizar;
- quando não utilizar.

## Experimentar

Grande parte do aprendizado acontecerá através de erros.

É esperado quebrar containers, apagar dados e reconstruir ambientes diversas vezes.

## Documentar tudo

Cada decisão importante deve ser registrada.

Por exemplo:

- Por que utilizar Alpine?
- Por que abandonar Alpine?
- Por que utilizar Multi-stage?
- Por que criar uma network?
- Por que utilizar volumes?

## Explicar como se estivesse ensinando

Se uma decisão não consegue ser explicada para outra pessoa, provavelmente ela ainda não foi completamente compreendida.

# Objetivos de aprendizado

Durante os sete dias serão explorados os seguintes tópicos.

- Docker Engine
- Containers
- Images
- Dockerfile
- Layers
- Build Cache
- Volumes
- Bind Mounts
- Networks
- DNS Interno
- Docker Compose
- Multi-stage Builds
- Healthchecks
- Variáveis de Ambiente
- Logs
- Observabilidade
- Reverse Proxy
- Persistência
- Segurança
- Arquitetura de aplicações containerizadas

Mais importante do que aprender cada ferramenta será compreender o motivo de sua existência.

# Competências desenvolvidas

Ao concluir o intensivão espera-se desenvolver capacidade para:

- Projetar ambientes Docker completos.
- Criar Dockerfiles profissionais.
- Otimizar builds.
- Reduzir tamanho de imagens.
- Estruturar ambientes de desenvolvimento.
- Estruturar ambientes de produção.
- Identificar problemas de arquitetura.
- Investigar erros de containers.
- Escolher entre diferentes abordagens técnicas.

# Projeto Final

O último desafio consiste na construção de uma plataforma completa utilizando Docker.

O projeto deverá incluir:

- Frontend
- Backend
- Banco de Dados
- Cache
- Mensageria
- Worker
- Reverse Proxy
- Monitoramento
- Persistência
- Docker Compose
- Dockerfiles otimizados
- Healthchecks
- Redes customizadas
- Volumes
- Variáveis de ambiente
- Documentação técnica

O foco não será apenas entregar uma aplicação funcionando, mas justificar todas as decisões arquiteturais adotadas.

