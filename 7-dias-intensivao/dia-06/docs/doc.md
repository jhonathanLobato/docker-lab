# Docker Intensive — Dia 06

# Operação, Observabilidade e Produção

> *Objetivo do dia:* aprender a operar uma aplicação containerizada, identificar problemas, acompanhar a saúde dos serviços e construir uma camada de entrada utilizando um Reverse Proxy.

# Contexto

Nos últimos dias, sua aplicação evoluiu consideravelmente.

Ela deixou de ser um único container e passou a possuir múltiplos serviços.

Agora existe uma infraestrutura composta por containers, redes, volumes e imagens, todos administrados através do Docker Compose.

As imagens também foram revisadas e otimizadas.

A equipe agora possui um novo problema.

A aplicação está funcionando, mas ninguém sabe responder algumas perguntas importantes:

> A API está realmente saudável?

> O banco de dados está disponível?

> O serviço está respondendo corretamente?

> Se um container apresentar um problema, como descobrir o motivo?

> Como saber o que aconteceu há dez minutos?

> Como expor vários serviços através de uma única entrada?

> Como diferenciar uma aplicação que está "rodando" de uma aplicação que está realmente "saudável"?

Em um ambiente de produção, simplesmente executar um container não é suficiente.

É necessário observar, diagnosticar e controlar o comportamento da infraestrutura.

Este será o objetivo do Dia 06.

# Problema

Sua infraestrutura possui diversos serviços, mas atualmente o Docker sabe principalmente se os containers estão executando ou não.

Um processo pode estar vivo e, ainda assim, a aplicação estar completamente quebrada.

Por exemplo:
Container: UP

Processo Python: executando

Aplicação: incapaz de acessar o banco


Do ponto de vista do Docker, o container pode continuar funcionando.

Do ponto de vista do usuário, entretanto, a aplicação está indisponível.

Você precisará criar mecanismos capazes de identificar esse tipo de situação.

Além disso, sua arquitetura possui múltiplos serviços que atualmente podem ser acessados diretamente.

Você deverá introduzir um Reverse Proxy para criar uma única porta de entrada para a aplicação.

# Objetivos de Aprendizado

Ao concluir este desafio você deverá compreender:

- Diferença entre processo em execução e aplicação saudável.
- Healthchecks.
- Estado healthy, unhealthy e starting.
- Logs de containers.
- Estratégias básicas de observabilidade.
- Diagnóstico de problemas em ambientes Docker.
- Reverse Proxy.
- Roteamento de requisições.
- Comunicação entre serviços através de redes Docker.
- Exposição de serviços internos e externos.
- Como estruturar uma arquitetura mais próxima de produção.

# Arquitetura

A arquitetura inicialmente será semelhante à utilizada nos dias anteriores.

                    Docker Network

              ┌─────────────────────┐
              │                     │
              │        API          │
              │                     │
              └──────────┬──────────┘
                         │
                         │
                         ▼
              ┌─────────────────────┐
              │    Notifications    │
              │                     │
              └─────────────────────┘


Ao longo do desafio, essa arquitetura deverá evoluir.

Ao final, deverá existir uma camada responsável por receber as requisições externas e encaminhá-las para os serviços internos.


                    Internet / Host
                           │
                           ▼
                  ┌─────────────────┐
                  │  Reverse Proxy  │
                  │     Nginx       │
                  └────────┬────────┘
                           │
                           ▼
                     ┌───────────┐
                     │    API    │
                     └─────┬─────┘
                           │
                           ▼
                   ┌───────────────┐
                   │ Notifications │
                   └───────────────┘


O objetivo não é simplesmente copiar essa arquitetura.

Você deverá compreender por que ela existe e quais problemas ela resolve.

# Missão 01 — O que significa uma aplicação estar saudável?

Antes de implementar qualquer ferramenta, investigue a seguinte situação:

Um container possui status:
Up


Isso significa necessariamente que a aplicação está funcionando?

Crie situações em que:

- o processo continua executando;
- o container continua Up;
- mas a aplicação não consegue atender corretamente às requisições.

A partir desses experimentos, explique a diferença entre:

Container funcionando e Aplicação saudável


Essa distinção será a base do restante do dia.

# Missão 02 — Healthchecks

Agora investigue o mecanismo de Healthcheck do Docker.

Descubra:

- O que é um Healthcheck.
- Quem executa o Healthcheck.
- Como o Docker determina se o teste passou.
- O que significa healthy.
- O que significa unhealthy.
- O que significa starting.

Sua aplicação já possui uma rota:
/health

Utilize essa rota como parte do mecanismo de verificação da saúde da aplicação.

Não basta configurar o Healthcheck.

Você deverá observar seu comportamento.

# Missão 03 — Criando uma Falha

Uma infraestrutura só pode ser considerada observável se você conseguir detectar problemas.

Depois de configurar o Healthcheck, provoque deliberadamente uma falha.

Por exemplo:

- faça o serviço deixar de responder;
- faça uma dependência ficar indisponível;
- altere temporariamente uma configuração;
- provoque um erro controlado na aplicação.

Observe:

- O que acontece com o status do container?
- Quanto tempo leva para o Docker perceber?
- O que aparece no docker ps?
- O que aparece no docker inspect?

Documente o experimento.

# Missão 04 — Logs

Agora imagine que o Healthcheck informou:
unhealthy


Isso responde apenas uma pergunta:

> Existe algum problema?

Mas não responde:

> Qual é o problema?

Para descobrir isso, você precisará investigar os logs.

Estude:

- Como visualizar logs.
- Como acompanhar logs em tempo real.
- Como limitar a quantidade de logs exibidos.
- Como identificar qual serviço produziu determinado log.
- Como utilizar logs durante troubleshooting.

Investigue também a diferença entre:

stdout e stderr

e por que aplicações containerizadas normalmente escrevem seus logs nesses fluxos.

# Missão 05 — Troubleshooting

Agora será realizado um exercício de investigação.

Você deverá provocar ou simular problemas diferentes na infraestrutura.

Exemplos:

- Serviço parado.
- Serviço na porta errada.
- Serviço fora da rede.
- Endpoint inexistente.
- Healthcheck incorreto.
- Dependência indisponível.
- Variável de ambiente incorreta.

Para cada problema, você deverá tentar descobrir a causa utilizando apenas as ferramentas de diagnóstico disponíveis.

Crie um procedimento próprio de troubleshooting.

Por exemplo:

1. O container está executando?
2. O serviço está saudável?
3. O serviço está na rede correta?
4. A porta está correta?
5. O serviço consegue acessar suas dependências?
6. Existem erros nos logs?
7. O endpoint responde?


O objetivo é começar a desenvolver seu próprio método de investigação.

# Missão 06 — O problema da exposição direta

Observe a arquitetura atual.

Provavelmente existem serviços que podem ser acessados diretamente pelo Host.

Imagine:

Host
 │
 ├── :5000 → API
 │
 └── :5001 → Notifications

Agora pense em um ambiente de produção.

Você realmente deseja que todos os serviços sejam diretamente acessíveis?

O serviço de notificações precisa necessariamente ser exposto ao usuário?

O banco de dados deveria possuir uma porta publicada?

A resposta geralmente será não.

Investigue o conceito de:

> *Serviços internos e serviços expostos.*

Seu objetivo será modificar a arquitetura para que apenas o serviço responsável pela entrada externa seja publicado.

# Missão 07 — Reverse Proxy

Agora será introduzido um novo componente:

> *Nginx*

O Nginx funcionará como Reverse Proxy.

Ele será responsável por receber requisições externas e encaminhá-las para os serviços apropriados.

A arquitetura deverá se aproximar de:

              Cliente
                 │
                 ▼
              Nginx
                 │
          ┌──────┴──────┐
          │             │
          ▼             ▼
         API      outro serviço


Investigue:

- O que é um Reverse Proxy.
- Qual problema ele resolve.
- Diferença entre Proxy e Reverse Proxy.
- Por que o cliente não precisa conhecer o endereço interno dos serviços.
- Como o Nginx encontra a API.
- Como o Nginx se comunica com os containers.

# Missão 08 — Roteamento

Agora configure o Reverse Proxy para encaminhar diferentes caminhos.

Por exemplo:
/

deverá chegar à API.

Enquanto outro caminho poderá ser encaminhado para outro serviço.

O objetivo é compreender que o Reverse Proxy pode funcionar como uma camada de roteamento.

Investigue também o que acontece quando:

- o serviço de destino está parado;
- o serviço não existe;
- a porta está incorreta;
- o serviço está fora da rede.

Observe os erros produzidos pelo Nginx.

# Missão 09 — Redes e Reverse Proxy

Agora integre o conhecimento do Dia 03.

O Nginx não deverá acessar os serviços utilizando IPs fixos.

Ele deverá utilizar os mecanismos de descoberta fornecidos pela rede Docker.

Isso permitirá reforçar os conceitos estudados anteriormente:

- DNS interno;
- nomes de serviços;
- redes compartilhadas;
- isolamento;
- comunicação interna.

Observe como o conhecimento dos dias anteriores começa a se encaixar.

# Missão 10 — Observando a Arquitetura

Depois que tudo estiver funcionando, pare e observe a arquitetura.

Você agora possui:

                     Cliente
                        │
                        ▼
                 Reverse Proxy
                        │
                        ▼
                       API
                        │
                        ▼
                  Notifications


Além disso, existem:
- Docker Compose
- Docker Network
- Healthchecks
- Logs
- Volumes
- Images
- Containers

Documente como todos esses componentes se relacionam.

# Perguntas de Arquitetura

Ao concluir o desafio, responda:

## Healthcheck

- Qual a diferença entre running e healthy?
- Por que um processo pode estar funcionando enquanto a aplicação está quebrada?
- O que torna um Healthcheck útil?

## Logs

- Por que logs são importantes?
- Quais informações deveriam estar disponíveis nos logs?
- Como utilizar logs durante uma investigação?

## Troubleshooting

- Qual seria sua primeira ação diante de um serviço indisponível?
- Como você diferencia problema de aplicação de problema de infraestrutura?
- Como provar onde está o problema?

## Reverse Proxy

- Por que utilizar um Reverse Proxy?
- Por que não expor todos os serviços diretamente?
- Qual a vantagem de possuir um único ponto de entrada?

## Redes

- Como o Reverse Proxy encontra a API?
- Por que não utilizar IPs fixos?
- O que aconteceria se o container da API fosse recriado?

# Missão Bônus

Pesquise e documente:

- Nginx
- Reverse Proxy
- Healthcheck
- docker inspect
- docker logs
- docker stats
- stdout
- stderr
- Graceful Shutdown
- Restart Policies
- Load Balancing

Não é necessário dominar todos esses conceitos.

O objetivo é ampliar sua visão sobre como aplicações containerizadas são operadas.

# Documentação Obrigatória

Durante este dia você deverá registrar:

## Arquitetura

Desenhe a arquitetura antes e depois da implementação do Reverse Proxy.

## Healthchecks

Documente:

- configuração utilizada;
- comportamento normal;
- comportamento durante falha.

## Logs

Registre exemplos de problemas encontrados e como os logs ajudaram a identificá-los.

## Troubleshooting

Crie um pequeno guia próprio contendo os passos que você seguiria para investigar uma aplicação Docker indisponível.

## Reverse Proxy

Explique:

- por que foi utilizado;
- quais serviços ele acessa;
- quais serviços são públicos;
- quais serviços são internos.

# Critério de Sucesso

Ao concluir este desafio você deverá ser capaz de:

- criar Healthchecks;
- interpretar estados de saúde;
- acompanhar logs;
- investigar falhas;
- diferenciar problemas de aplicação e infraestrutura;
- configurar um Reverse Proxy;
- encaminhar requisições para serviços internos;
- utilizar redes Docker para comunicação interna;
- manter serviços internos sem exposição direta ao Host.

Mais importante do que fazer a infraestrutura funcionar será conseguir responder:

> *"Como eu descobriria o que está errado se ela parasse de funcionar?"*

Essa é a pergunta central do Dia 06.

# Reflexão

Ao finalizar o desafio, registre:

- Qual problema foi mais difícil de diagnosticar?
- Qual informação dos logs foi mais útil?
- Qual diferença você percebeu entre running e healthy?
- Por que o Reverse Proxy melhora a arquitetura?
- Quais serviços deveriam permanecer internos?
- Como seu processo de troubleshooting mudou desde o Dia 01?
- O que ainda falta para considerar essa arquitetura próxima de uma aplicação de produção?

# Preparação para o Dia 07

No Dia 07 todos os conceitos serão reunidos.

A aplicação deixará de ser apenas um laboratório de Docker e se tornará um projeto completo.

Você deverá utilizar:

- Containers;
- Imagens;
- Dockerfiles;
- Layers;
- Build Cache;
- Volumes;
- Redes;
- DNS;
- Docker Compose;
- Variáveis de ambiente;
- Healthchecks;
- Logs;
- Reverse Proxy;
- Persistência;
- Boas práticas de segurança.

O objetivo será construir uma arquitetura completa e, principalmente, *justificar cada decisão tomada*.