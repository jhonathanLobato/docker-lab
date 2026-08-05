# Docker Intensive — Dia 04

# Docker Compose e Orquestração Local

> **Objetivo do dia:** aprender a descrever toda a infraestrutura da aplicação em um único arquivo, automatizando a criação, configuração e gerenciamento de múltiplos containers.

# Contexto

Nos últimos dias você construiu uma pequena arquitetura composta por múltiplos serviços.

Até agora, toda essa infraestrutura foi criada manualmente.

Cada container exigia um comando diferente.

Era necessário lembrar:

- qual imagem utilizar;
- quais portas publicar;
- quais volumes montar;
- qual nome atribuir ao container;
- em qual rede conectá-lo;
- quais variáveis de ambiente configurar.

À medida que a aplicação cresce, esse processo rapidamente se torna inviável.

Imagine um ambiente contendo:

- Frontend
- API
- Banco de Dados
- Redis
- Worker
- Nginx

Seria necessário executar diversos comandos `docker run`, sempre na ordem correta e utilizando exatamente as mesmas configurações.

Além disso, qualquer novo desenvolvedor da equipe precisaria conhecer todos esses comandos para conseguir executar o projeto.

A empresa decidiu resolver esse problema.

Toda a infraestrutura deverá ser descrita em um único arquivo, permitindo que qualquer pessoa recrie todo o ambiente com apenas um comando.

# Problema

A aplicação deixou de ser composta por apenas um container.

Agora existe uma infraestrutura completa.

Seu desafio será transformar toda essa configuração manual em um ambiente declarativo utilizando Docker Compose.

O objetivo será compreender o conceito de Infraestrutura como Código (Infrastructure as Code).

# Objetivos de Aprendizado

Ao concluir este desafio você deverá compreender:

- O que é Docker Compose.
- Qual problema ele resolve.
- O conceito de infraestrutura declarativa.
- Como definir serviços.
- Como compartilhar redes automaticamente.
- Como compartilhar volumes.
- Como configurar variáveis de ambiente.
- Como organizar aplicações compostas por múltiplos containers.
- Como funciona a dependência entre serviços.
- Como subir e destruir toda uma infraestrutura com poucos comandos.

# Restrições

Durante este desafio você **não poderá**:

- criar containers utilizando `docker run`;
- criar redes manualmente;
- criar volumes manualmente para a aplicação;
- iniciar serviços individualmente.

Toda a infraestrutura deverá ser criada exclusivamente através do Docker Compose.

# Desafio

Você deverá migrar toda a arquitetura construída no Dia 03 para Docker Compose.

Ao final do desafio, toda a aplicação deverá ser inicializada utilizando apenas um comando.

Toda configuração deverá estar documentada no arquivo `compose.yaml`.

---

# Missão 01 — Conhecendo o Docker Compose

Antes de escrever qualquer configuração, investigue:

- O que é Docker Compose.
- Qual problema ele resolve.
- Por que ele surgiu.
- Qual a diferença entre containers e serviços.
- O que significa dizer que a infraestrutura é declarativa.

# Missão 02 — Criando o Primeiro compose.yaml

Agora descreva sua aplicação em um único arquivo.

Investigue:

- Estrutura do arquivo.
- Versão do Compose.
- Definição de serviços.
- Build de imagens.
- Nome dos containers.

Ao final desta missão, toda a aplicação deverá iniciar utilizando apenas um comando.

# Missão 03 — Redes Compartilhadas

No Dia 03 você criou redes manualmente.

Agora investigue:

- Como o Compose cria redes.
- Quantas redes são criadas.
- Como os serviços passam a se comunicar.
- Como descobrir o nome da rede criada automaticamente.

Compare cuidadosamente esse comportamento com o que foi feito manualmente no dia anterior.

# Missão 04 — Volumes no Compose

Sua aplicação já utiliza persistência.

Agora investigue:

- Como declarar volumes no Compose.
- Como associá-los aos serviços.
- Como reutilizá-los.
- O que acontece quando a infraestrutura é removida.

# Missão 05 — Variáveis de Ambiente

Nenhuma aplicação profissional possui configurações escritas diretamente no código.

Investigue:

- Como definir variáveis de ambiente.
- Como acessá-las na aplicação.
- Como separar configuração de código.
- Como utilizar arquivos `.env`.

Ao final da missão, sua aplicação deverá funcionar sem depender de valores fixos escritos no código.

# Missão 06 — Dependências entre Serviços

Agora surge um novo problema.

Nem sempre todos os serviços iniciam ao mesmo tempo.

Investigue:

- Como o Compose controla a ordem de inicialização.
- O que faz `depends_on`.
- Quais limitações ele possui.
- Por que ele não garante que um serviço esteja realmente pronto para receber conexões.

# Missão 07 — Organização da Infraestrutura

Agora observe todo o ambiente criado.

Identifique:

- Quantos containers existem.
- Quantas redes foram criadas.
- Quantos volumes existem.
- Como todos esses recursos se relacionam.

Construa um diagrama representando toda a arquitetura.

---

# Perguntas de Arquitetura

Ao concluir este desafio responda:

## Sobre Docker Compose

- Qual problema ele resolve?
- Quando utilizá-lo?
- Quando ele não é suficiente?

## Sobre Serviços

- O que diferencia um serviço de um container?
- Por que o Compose trabalha com serviços e não apenas containers?

## Sobre Redes

- Por que os serviços conseguem se comunicar automaticamente?
- Quem cria essa rede?

## Sobre Persistência

- Como o Compose gerencia volumes?
- Os dados sobrevivem após a remoção dos containers?

## Sobre Configuração

- Por que utilizar variáveis de ambiente?
- Quais vantagens isso oferece para desenvolvimento e produção?

---

# Missão Bônus

Pesquise e documente:

- compose.yaml
- docker compose up
- docker compose down
- docker compose ps
- docker compose logs
- docker compose exec
- docker compose config
- Perfis (profiles)
- Arquivo `.env`

# Critério de Sucesso

Ao concluir este desafio você deverá ser capaz de:

- iniciar toda a aplicação com um único comando;
- compreender cada seção do arquivo `compose.yaml`;
- explicar como Compose cria redes, volumes e serviços;
- modificar a infraestrutura sem utilizar comandos manuais.

Mais importante do que utilizar Docker Compose será compreender como a infraestrutura passa a ser descrita como código.