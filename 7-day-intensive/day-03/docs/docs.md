# Docker Intensive — Dia 03

# Redes e Comunicação entre Containers

> **Objetivo do dia:** compreender como os containers se comunicam entre si, como o Docker implementa redes virtuais, como funciona a resolução de nomes (DNS interno) e por que a arquitetura de aplicações modernas depende desse mecanismo.

# Contexto

Após a conclusão do Dia 02, a aplicação já é capaz de armazenar dados de forma persistente.

Entretanto, um novo requisito surgiu.

A empresa decidiu evoluir a arquitetura da aplicação.

Em vez de concentrar todas as responsabilidades em um único processo, será adotada uma arquitetura baseada em serviços independentes.

A API continuará sendo responsável por atender as requisições HTTP.

Entretanto, agora ela precisará conversar com outros serviços.

A primeira dificuldade encontrada pela equipe foi inesperada.

Mesmo estando na mesma máquina, um container não consegue simplesmente acessar outro utilizando `localhost`.

Essa descoberta levantou diversas perguntas.

Como um container encontra outro?

Quem fornece os endereços IP?

Como ocorre a comunicação?

O que acontece quando um container é recriado?

Como evitar depender de endereços IP que mudam constantemente?

Seu papel será investigar essas questões e compreender como o Docker resolve esse problema.

# Problema

Sua aplicação deixará de existir isoladamente.

Agora ela fará parte de um ambiente composto por múltiplos containers.

Esses containers precisarão trocar informações continuamente.

Você deverá construir essa comunicação utilizando os mecanismos oferecidos pelo Docker, compreendendo não apenas como utilizá-los, mas principalmente por que eles existem.

# Objetivos de Aprendizado

Ao concluir este desafio você deverá compreender:

- Como funciona a rede padrão do Docker.
- O que é uma Docker Network.
- Como containers se comunicam.
- O conceito de isolamento de rede.
- Diferença entre comunicação interna e externa.
- Como funciona o DNS interno do Docker.
- Por que não devemos utilizar endereços IP diretamente.
- Como criar redes personalizadas.
- Como conectar containers a uma mesma rede.
- Como inspecionar redes Docker.
- Como diagnosticar problemas de comunicação entre containers.

Mais importante do que decorar comandos será compreender como o Docker cria uma infraestrutura de rede virtual sobre o sistema operacional.

# Restrições

Durante este desafio você **não pode**:

- utilizar Docker Compose;
- utilizar Kubernetes;
- utilizar IPs fixos para comunicação entre containers;
- modificar arquivos do sistema operacional do Host para resolver nomes.

Toda comunicação deverá utilizar apenas recursos fornecidos pelo Docker.

# Desafio

Sua missão será transformar a aplicação construída até aqui em um ambiente composto por múltiplos containers.

Esses containers deverão conseguir trocar informações entre si utilizando os mecanismos de rede disponibilizados pelo Docker.

Durante todo o processo você deverá investigar como essa comunicação acontece internamente.

---

# Missão 01 — Entendendo a Rede Padrão

Antes de criar qualquer rede personalizada, investigue:

- Em qual rede um container é conectado automaticamente.
- Qual o objetivo dessa rede.
- Quais limitações ela possui.
- Como descobrir em qual rede um container está conectado.
- Como visualizar todos os containers participantes dessa rede.

Realize experimentos suficientes para compreender o comportamento da rede padrão.

# Missão 02 — Explorando a Arquitetura de Rede

Investigue como o Docker cria a infraestrutura de comunicação entre containers.

Descubra:

- Quem fornece o endereço IP de um container.
- Como esses IPs são atribuídos.
- O que acontece quando um container é removido.
- O endereço IP permanece o mesmo após uma recriação?
- É seguro depender desses endereços?

Documente todas as conclusões.

# Missão 03 — Criando uma Rede Personalizada

Agora a empresa decidiu organizar melhor sua infraestrutura.

Você deverá criar uma rede exclusiva para sua aplicação.

Investigue:

- Como criar uma Docker Network.
- Como conectar containers a essa rede.
- Como verificar quais containers estão conectados.
- O que muda em relação à rede padrão.

Compare cuidadosamente os dois cenários.

# Missão 04 — Descobrindo o DNS Interno

Uma das maiores vantagens das redes Docker é permitir que containers encontrem uns aos outros sem utilizar endereços IP.

Descubra:

- Como um container encontra outro utilizando apenas seu nome.
- Quem realiza essa resolução de nomes.
- Por que isso torna a arquitetura mais estável.
- O que acontece quando um container é recriado.

Ao final desta missão você deverá compreender por que praticamente nenhuma aplicação moderna utiliza IPs fixos para comunicação entre containers.

# Missão 05 — Comunicação entre Serviços

Agora você deverá construir um pequeno ambiente distribuído.

Sua API deverá conseguir consumir informações de outro container.

Não importa qual seja o serviço.

O foco deste desafio não é a aplicação.

O foco é a comunicação entre processos isolados.

Investigue:

- Como enviar requisições entre containers.
- Como validar que essa comunicação realmente ocorreu.
- Como diagnosticar falhas de conectividade.

# Missão 06 — Inspeção e Troubleshooting

Nenhuma infraestrutura está livre de problemas.

Você deverá investigar ferramentas capazes de responder perguntas como:

- Quais redes existem?
- Quais containers estão conectados?
- Qual IP foi atribuído?
- Qual Gateway está sendo utilizado?
- O container realmente está conectado à rede esperada?

Utilize os recursos do Docker para responder cada uma dessas perguntas.

# Perguntas de Arquitetura

Ao concluir este desafio você deverá responder:

## Sobre Redes

- O que é uma Docker Network?
- Por que ela existe?
- Como o Docker implementa esse isolamento?

---

## Sobre Endereços IP

- Quem atribui o IP de um container?
- Esse IP é permanente?
- Por que não devemos depender dele?

---

## Sobre DNS

- O que é o DNS interno do Docker?
- Como ele funciona?
- Qual problema ele resolve?

---

## Sobre Comunicação

- Por que um container não deve utilizar localhost para acessar outro?
- Como ocorre a comunicação entre dois containers?
- O que muda quando ambos pertencem à mesma rede?

---

## Sobre Arquitetura

Imagine que sua empresa possui:

- API
- Banco de Dados
- Redis
- Worker

Como você organizaria a comunicação entre esses serviços?

Justifique todas as decisões.

# Missão Bônus

Pesquise e documente:

- Bridge Network
- Host Network
- None Network
- DNS interno do Docker
- docker network inspect
- docker network ls
- docker network connect
- docker network disconnect
- Namespace de Rede (Network Namespace)

Não é necessário dominar todos esses conceitos.

O objetivo é começar a compreender como o Docker cria uma infraestrutura de rede isolada utilizando recursos do kernel Linux.

---

# Critério de Sucesso

Ao concluir este desafio você deverá ser capaz de explicar:

- Por que localhost não funciona entre containers.
- Como um container encontra outro.
- Como o Docker implementa redes virtuais.
- Como funciona o DNS interno.
- Por que utilizar nomes é melhor do que utilizar IPs.
- Como diagnosticar problemas de comunicação.

Mais importante do que executar comandos é compreender como a infraestrutura de rede do Docker funciona.
