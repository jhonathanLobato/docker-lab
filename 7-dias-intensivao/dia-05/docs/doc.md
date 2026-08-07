# Docker Intensive — Dia 05

# Construção Profissional de Imagens Docker

> *Objetivo do dia:* compreender como construir imagens Docker eficientes, pequenas, seguras e reproduzíveis, aplicando as mesmas práticas utilizadas em ambientes de produção.

# Contexto

Até este momento do intensivão, sua aplicação já é composta por múltiplos serviços executados através do Docker Compose.

A infraestrutura funciona.

Os containers conseguem se comunicar.

Os dados são persistidos.

Tudo parece pronto.

Entretanto, durante uma revisão da arquitetura, a equipe percebeu um novo problema.

As imagens produzidas estão muito maiores do que deveriam.

O tempo de build é elevado.

Cada pequena alteração no código força a reinstalação de dependências.

Além disso, a imagem contém arquivos que nunca serão utilizados em produção.

A empresa decidiu iniciar um processo de otimização das imagens.

Seu objetivo não será alterar a aplicação.

Seu objetivo será melhorar a forma como ela é construída.

# Problema

Uma imagem Docker pode funcionar perfeitamente e, ainda assim, possuir diversos problemas arquitetônicos.

Imagens grandes consomem mais espaço.

Demoram mais para serem enviadas para registries.

Demoram mais para serem baixadas em servidores.

Aumentam a superfície de ataque.

E tornam todo o processo de implantação mais lento.

Você deverá reconstruir seus Dockerfiles aplicando técnicas utilizadas em ambientes profissionais.

# Objetivos de Aprendizado

Ao concluir este desafio você deverá compreender:

- Como o Docker utiliza Layers durante o build.
- Como funciona o Build Cache.
- Como reduzir o tamanho de imagens.
- Como organizar corretamente um Dockerfile.
- O conceito de Multi-stage Build.
- Diferença entre imagens de desenvolvimento e produção.
- Como evitar arquivos desnecessários dentro da imagem.
- Como tornar builds mais rápidos.
- Como produzir imagens reproduzíveis.

Mais importante do que decorar boas práticas será compreender por que elas existem.

# Restrições

Durante este desafio você não poderá:

- modificar o comportamento da aplicação;
- remover funcionalidades para reduzir tamanho;
- instalar ferramentas desnecessárias na imagem final.

Toda otimização deverá ocorrer apenas através da construção da imagem.

# Desafio

Você deverá revisar completamente os Dockerfiles construídos até agora.

Ao final do desafio suas imagens deverão ser menores, mais rápidas de construir e mais organizadas.

Toda decisão deverá ser documentada e justificada.

---

# Missão 01 — Investigando o Processo de Build

Antes de otimizar qualquer coisa, investigue:

- Como o Docker constrói uma imagem.
- Como as Layers são reutilizadas.
- O que invalida o cache.
- Por que a ordem das instruções influencia o tempo de build.

Realize experimentos alterando diferentes partes do Dockerfile e observe quais Layers são reconstruídas.

# Missão 02 — Dominando o Build Cache

Agora investigue como o Docker decide reutilizar uma Layer.

Descubra:

- Quando uma Layer pode ser reaproveitada.
- Quando ela precisa ser reconstruída.
- Como pequenas alterações impactam todo o processo.
- Como organizar o Dockerfile para aproveitar melhor o cache.

Documente todos os experimentos realizados.

# Missão 03 — Imagens Enxutas

Sua missão agora será reduzir o tamanho das imagens.

Investigue:

- Diferença entre imagens base.
- Quando utilizar imagens slim.
- Quando utilizar imagens alpine.
- Quais vantagens e limitações cada abordagem possui.

Justifique a escolha da imagem utilizada.

# Missão 04 — Multi-stage Build

Agora imagine uma aplicação que precisa ser compilada.

Ferramentas de compilação são necessárias durante o build, mas não durante a execução.

Investigue:

- O que é um Multi-stage Build.
- Qual problema ele resolve.
- Como separar ambiente de build e ambiente de execução.
- Como copiar apenas os artefatos necessários para a imagem final.

Mesmo que sua aplicação não exija compilação complexa, implemente um Multi-stage Build para compreender seu funcionamento.

# Missão 05 — .dockerignore

Agora investigue como controlar quais arquivos participam do build.

Descubra:

- Qual a função do .dockerignore.
- Como ele influencia o contexto de build.
- Quais arquivos nunca deveriam ser enviados ao Docker.
- Como isso afeta desempenho e segurança.

# Missão 06 — Segurança Básica

Toda imagem Docker representa um ambiente de execução.

Investigue:

- Por que evitar executar aplicações como root.
- Como reduzir privilégios.
- Como diminuir a superfície de ataque.
- Quais informações não devem estar presentes na imagem.

O objetivo não é aprofundar segurança, mas começar a desenvolver essa preocupação.

# Missão 07 — Comparando as Imagens

Compare a primeira imagem construída no Dia 01 com a imagem atual.

Analise:

- Tamanho.
- Tempo de build.
- Organização do Dockerfile.
- Quantidade de Layers.
- Facilidade de manutenção.

Documente todas as diferenças.

# Perguntas de Arquitetura

Ao concluir este desafio responda:

## Sobre Layers

- Como o Docker utiliza Layers durante o build?
- Por que a ordem das instruções importa?

## Sobre Cache

- Como o Docker decide reutilizar uma Layer?
- O que invalida o cache?

## Sobre Imagens

- O que torna uma imagem profissional?
- Quais critérios você utilizaria para escolher uma imagem base?

## Sobre Multi-stage

- Qual problema essa técnica resolve?
- Quando ela deve ser utilizada?

## Sobre Segurança

- Por que não devemos executar aplicações como root?
- Como pequenas decisões no Dockerfile influenciam a segurança da aplicação?

# Missão Bônus

Pesquise e documente:

- BuildKit
- Cache de Build
- Multi-stage Builds
- Imagens Distroless
- docker history
- docker image inspect
- docker builder prune

# Documentação Obrigatória

Durante este desafio registre:

## Decisões

Por que cada otimização foi realizada?

## Experimentos

Quais testes foram feitos?

Quais resultados foram obtidos?

## Comparações

Compare cada Dockerfile antes e depois da otimização.

Explique por que cada alteração foi realizada.

## Descobertas

Quais conceitos mais impactaram sua forma de construir imagens?

# Critério de Sucesso

Ao concluir este desafio você deverá ser capaz de:

- construir imagens menores;
- aproveitar corretamente o Build Cache;
- utilizar Multi-stage Builds;
- organizar Dockerfiles profissionais;
- justificar cada decisão tomada durante a construção da imagem.

Mais importante do que reduzir alguns megabytes será compreender como o processo de build influencia desempenho, manutenção e segurança.

# Reflexão

Ao finalizar este desafio registre:

- Qual otimização gerou maior impacto?
- O que mais chamou sua atenção sobre o Build Cache?
- Em quais situações um Dockerfile mal estruturado pode causar problemas?
- Como esse conhecimento será utilizado em projetos reais?