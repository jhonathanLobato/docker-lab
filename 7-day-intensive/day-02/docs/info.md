# Docker Intensive — Dia 02

# Persistência e Sistema de Arquivos

> **Objetivo do dia:** compreender como o Docker gerencia o sistema de arquivos dos containers, entender o conceito de Writable Layer, descobrir por que os dados são perdidos ao remover um container e aprender quando utilizar Bind Mounts e Volumes.

# Contexto

Após a entrega da primeira versão da aplicação Flask, a equipe de desenvolvimento recebeu uma nova solicitação.

A aplicação agora deverá armazenar informações geradas pelos usuários.

Durante os testes, percebeu-se que todas as informações desapareciam sempre que o container era removido e criado novamente.

O gerente da equipe levantou a seguinte preocupação:

> "Não podemos perder os dados dos clientes toda vez que atualizarmos a aplicação."

Agora cabe a você investigar o motivo desse comportamento e propor uma solução adequada.

# Problema

A aplicação precisa persistir dados.

Esses dados devem permanecer disponíveis mesmo que:

- o container seja parado;
- o container seja removido;
- uma nova versão da aplicação seja criada;
- uma nova imagem seja construída.

# Objetivos de Aprendizado

Ao concluir este desafio você deverá compreender:

- Como funciona o sistema de arquivos de uma imagem Docker.
- O que é uma Layer.
- O que é a Writable Layer.
- Por que imagens são imutáveis.
- Por que containers perdem dados.
- Diferença entre imagem e container.
- Diferença entre Bind Mount e Volume.
- Quando utilizar cada estratégia.
- Como compartilhar dados entre Host e Container.
- Como persistir dados corretamente.

# Restrições

Durante este desafio você **não pode**:

- copiar Dockerfiles prontos;
- utilizar Docker Compose;
- utilizar bancos de dados externos;
- utilizar tutoriais que apenas entreguem comandos.

Toda decisão deve ser justificada.

# Desafio

Sua missão será evoluir a aplicação criada no Dia 01.

Ela deverá ser capaz de armazenar informações em arquivos.

Após isso você deverá provar experimentalmente o comportamento do Docker em diferentes cenários.

Você deverá realizar experimentos suficientes para responder todas as perguntas propostas neste desafio.

# Missão 01 — Descobrir onde os dados ficam

Investigue:

- Onde os arquivos criados pela aplicação são armazenados.
- O que acontece quando um arquivo é criado dentro do container.
- Em qual camada esses arquivos ficam.

Não procure apenas a resposta.

Faça experimentos.

# Missão 02 — Entender a Writable Layer

Descubra:

- O que é a Writable Layer.
- Quando ela é criada.
- Quando ela deixa de existir.
- Quem é responsável por criá-la.
- Ela faz parte da imagem?

# Missão 03 — Recriação do container

Faça experimentos.

Crie arquivos.

Remova containers.

Crie novos containers.

Observe cuidadosamente:

- quais arquivos permanecem;
- quais desaparecem;
- quais nunca deveriam desaparecer.

Documente tudo.

# Missão 04 — Bind Mount

Agora imagine que um desenvolvedor deseja editar os arquivos diretamente do computador enquanto a aplicação continua executando.

Investigue:

- Como compartilhar um diretório entre Host e Container.
- O que acontece quando um arquivo é alterado no Host.
- O que acontece quando um arquivo é alterado dentro do Container.
- Quais vantagens essa abordagem oferece para desenvolvimento.

# Missão 05 — Volumes

Agora considere um ambiente de produção.

Você não quer depender da estrutura de diretórios do Host.

Investigue:

- Como o Docker armazena Volumes.
- Quem gerencia esses dados.
- O que acontece quando um container é removido.
- O que acontece quando um Volume é removido.
- Como reutilizar um Volume em outro container.

# Missão 06 — Comparação

Monte uma comparação entre:

- Writable Layer
- Bind Mount
- Volume

Compare:

- Persistência
- Performance
- Segurança
- Portabilidade
- Casos de uso
- Facilidade de backup
- Compartilhamento

# Perguntas de Arquitetura

Ao final do desafio você deve conseguir responder:

## Sobre Layers

- O que é uma Layer?
- Por que elas são imutáveis?
- Como elas economizam espaço em disco?
- Como influenciam o Build Cache?

## Sobre Writable Layer

- Quem cria essa camada?
- Onde ela fica?
- Por que ela desaparece?
- Ela pode ser compartilhada?

## Sobre Volumes

- Qual problema eles resolvem?
- Por que existem?
- Por que não salvar tudo dentro do container?
- Como funcionam internamente?

## Sobre Bind Mounts

- Quando utilizar?
- Quando evitar?
- Quais riscos existem?
- Por que são excelentes para desenvolvimento?

## Sobre Arquitetura

Imagine que você precisa decidir entre:

- salvar arquivos na Writable Layer;
- utilizar Bind Mount;
- utilizar Volume.

Como você justificaria essa decisão para outro engenheiro?

# Missão Bônus

Pesquise e documente:

- OverlayFS
- Copy-on-Write
- Union File System
- docker diff
- docker commit
- docker volume inspect
- docker system df

Não é necessário dominar esses assuntos.

O objetivo é começar a compreender como o Docker funciona internamente.