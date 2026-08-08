# Docker Intensive — Dia 07

# Projeto Final — Plataforma Containerizada

> *Objetivo:* projetar, construir, executar e documentar uma aplicação composta por múltiplos serviços utilizando Docker, aplicando os conceitos estudados durante os seis dias anteriores.

---

# O desafio

Durante os últimos seis dias você estudou Docker isoladamente.

Agora chegou o momento de juntar tudo.

Você recebeu a responsabilidade de criar a infraestrutura de uma pequena plataforma web.

A aplicação deverá possuir múltiplos componentes, cada um com uma responsabilidade específica.

O objetivo não é simplesmente fazer a aplicação funcionar.

Você deverá construir uma arquitetura que seja:

- reproduzível;
- organizada;
- persistente;
- observável;
- segura;
- escalável dentro das limitações de um ambiente local;
- documentada.

Mais importante:

> *Você deverá conseguir justificar cada decisão arquitetural.*

Não existe uma única solução correta para todos os problemas deste projeto.

Duas arquiteturas podem funcionar.

A melhor será aquela que você conseguir justificar tecnicamente.

---

# Cenário

Imagine que uma empresa esteja desenvolvendo uma plataforma chamada:

*Docker Intensive Platform*

A plataforma permitirá que usuários criem mensagens.

A aplicação possui diferentes responsabilidades:

text
Frontend
    │
    ▼
Backend API
    │
    ├──────────► PostgreSQL
    │
    ├──────────► Redis
    │
    └──────────► Message Queue
                      │
                      ▼
                    Worker


Toda a aplicação deverá ser executada através do Docker Compose.

Um Reverse Proxy será responsável pela entrada externa da aplicação.

---

# Requisitos funcionais

A plataforma deverá possuir pelo menos:

## Usuários

A aplicação deverá possuir usuários armazenados no banco de dados.

Você não precisa desenvolver um sistema completo de autenticação.

O objetivo é possuir dados reais para trabalhar com persistência.

---

## Mensagens

O usuário deverá conseguir criar mensagens.

Exemplo:

text
POST /messages


A mensagem deverá ser armazenada no banco.

---

## Processamento assíncrono

Quando uma mensagem for criada, a aplicação deverá gerar um evento para processamento posterior.

O processamento não deverá bloquear a requisição principal.

A arquitetura deverá possuir um Worker responsável por processar esses eventos.

---

## Cache

A aplicação deverá possuir uma camada de cache.

Você deverá identificar pelo menos uma operação que faça sentido utilizar cache.

Não coloque Redis apenas porque o projeto exige Redis.

Você deverá explicar:

> Qual problema o cache resolve neste sistema?

---

## Interface

A aplicação deverá possuir uma interface simples.

O Frontend não precisa ser complexo.

O objetivo é criar um consumidor real para a API.

---

# Arquitetura mínima obrigatória

O projeto deverá possuir os seguintes componentes:

text
┌──────────────────────────────────────────┐
│              Reverse Proxy               │
│                   Nginx                  │
└───────────────────┬──────────────────────┘
                    │
                    ▼
             ┌─────────────┐
             │  Frontend   │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │     API     │
             └──┬─────┬────┘
                │     │
       ┌────────┘     └────────┐
       ▼                       ▼
┌──────────────┐         ┌──────────────┐
│  PostgreSQL  │         │    Redis     │
└──────────────┘         └──────────────┘
                │
                ▼
         ┌──────────────┐
         │ Message Queue│
         └───────┬──────┘
                 │
                 ▼
           ┌──────────┐
           │  Worker  │
           └──────────┘


A arquitetura acima representa apenas os componentes necessários.

*Não representa necessariamente a solução final.*

Você deverá decidir como esses componentes serão conectados.

---

# Componentes

## 1. Reverse Proxy

Utilize um Reverse Proxy para criar o ponto de entrada da aplicação.

Responsabilidades:

- receber requisições externas;
- encaminhar requisições;
- esconder serviços internos;
- controlar quais serviços serão expostos.

### Você deverá decidir

- Qual porta será publicada?
- Quais serviços devem ser acessíveis externamente?
- Quais devem permanecer exclusivamente na rede interna?
- O Frontend será servido pelo Nginx ou por outro container?
- Como as rotas serão encaminhadas?

---

# 2. Frontend

Crie uma interface mínima capaz de:

- visualizar mensagens;
- criar uma mensagem;
- apresentar informações básicas sobre o sistema.

O Frontend não precisa ser sofisticado.

O foco é infraestrutura.

### Você deverá decidir

- O Frontend precisa de um container próprio?
- Qual imagem base utilizar?
- O build precisa de múltiplos estágios?
- O Frontend precisa acessar diretamente o Backend?
- O usuário deverá conhecer o endereço interno da API?

---

# 3. Backend

O Backend será responsável pela lógica principal.

Ele deverá:

- disponibilizar a API;
- acessar PostgreSQL;
- acessar Redis;
- publicar eventos;
- disponibilizar Healthcheck;
- gerar logs.

### Você deverá decidir

- Qual porta interna utilizar?
- Essa porta precisa ser publicada no Host?
- Quais variáveis de ambiente serão necessárias?
- Como o Backend encontrará o banco?
- Como o Backend encontrará o Redis?
- Como lidar com falhas de dependências?

---

# 4. PostgreSQL

O banco será responsável pela persistência principal.

Ele deverá armazenar:

- usuários;
- mensagens;
- informações necessárias para o funcionamento da aplicação.

### Você deverá decidir

- Como persistir os dados?
- Bind Mount ou Volume?
- O banco deve possuir porta publicada?
- Como o Backend acessará o banco?
- Como verificar se o banco está saudável?
- Quais informações devem ficar em variáveis de ambiente?

---

# 5. Redis

Redis será utilizado como camada de cache.

Você deverá escolher uma operação adequada para cache.

Por exemplo:

text
GET /messages


poderia utilizar cache.

Mas isso é apenas uma possibilidade.

### Você deverá investigar

- Quando cache faz sentido?
- O que acontece quando o cache é perdido?
- O sistema continua funcionando?
- O Redis precisa de persistência neste projeto?
- Volume seria necessário?

---

# 6. Message Queue

A plataforma precisa processar algumas tarefas de maneira assíncrona.

Você deverá utilizar um sistema de mensageria.

Exemplos de possibilidades:

- RabbitMQ;
- Redis Streams;
- outro mecanismo adequado.

A escolha é sua.

### Você deverá justificar

- Por que escolheu essa tecnologia?
- Qual problema a fila resolve?
- O que acontece quando o Worker está indisponível?
- As mensagens permanecem disponíveis?
- Existe risco de perder mensagens?

---

# 7. Worker

O Worker será responsável por consumir mensagens da fila e realizar processamento em segundo plano.

Por exemplo:

text
Usuário
   │
   ▼
API
   │
   ▼
Queue
   │
   ▼
Worker
   │
   ▼
Processamento


A API não deverá precisar esperar o Worker terminar.

### Você deverá decidir

- O Worker precisa de uma porta?
- Ele precisa ser acessível externamente?
- Como ele encontra a fila?
- Como ele encontra o banco?
- O que acontece se a fila estiver indisponível?

---

# Missão 01 — Planejamento

Antes de escrever qualquer Dockerfile, desenhe sua arquitetura.

Você deverá produzir:

text
docs/arquitetura-final.md


O documento deverá conter:

- componentes;
- responsabilidades;
- redes;
- volumes;
- dependências;
- fluxo das requisições.

---

# Missão 02 — Definição das redes

Você deverá pensar na rede como uma camada de segurança e organização.

Não coloque todos os serviços automaticamente na mesma rede sem pensar.

Investigue:

> Quais serviços realmente precisam conversar?

Por exemplo:

text
Nginx ──► Frontend
Nginx ──► API

API ──► PostgreSQL
API ──► Redis
API ──► Queue

Worker ──► Queue
Worker ──► PostgreSQL


A partir disso, determine quais redes devem existir.

### Perguntas

- O banco precisa conversar com o Nginx?
- O Redis precisa ser acessível pelo Frontend?
- O Worker precisa estar na mesma rede do Nginx?
- Quais serviços devem permanecer isolados?

---

# Missão 03 — Persistência

Identifique quais dados precisam sobreviver à recriação dos containers.

Crie uma estratégia de persistência.

Você deverá decidir entre:

- Volume;
- Bind Mount;
- nenhum armazenamento persistente.

### Regra

Não utilize um volume simplesmente porque "Docker recomenda".

Para cada armazenamento responda:

> O dado precisa sobreviver?

> Quem deve gerenciar esse dado?

> O Host precisa enxergar esse arquivo?

> O serviço consegue funcionar sem ele?

---

# Missão 04 — Variáveis de ambiente

Identifique todas as configurações que não deveriam estar diretamente no código.

Por exemplo:

text
DATABASE_HOST
DATABASE_PORT
DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
REDIS_HOST
REDIS_PORT
QUEUE_HOST
QUEUE_PORT


Não copie essa lista cegamente.

Analise quais configurações sua aplicação realmente necessita.

### Investigue

- .env
- environment
- env_file
- valores padrão;
- informações sensíveis.

---

# Missão 05 — Dockerfiles

Cada aplicação deverá possuir um Dockerfile adequado.

Você deverá aplicar os conhecimentos do Dia 5:

- imagem base adequada;
- ordem das Layers;
- Build Cache;
- .dockerignore;
- Multi-stage quando fizer sentido;
- usuário não-root quando possível;
- imagem final contendo somente o necessário.

### Pergunta importante

Você precisa obrigatoriamente utilizar Multi-stage em todos os containers?

Se a resposta for não:

> Em quais casos ele realmente faz sentido?

---

# Missão 06 — Compose

Agora transforme toda a arquitetura em infraestrutura declarativa.

O projeto deverá possuir um:

text
compose.yaml


Ele deverá definir:

- serviços;
- redes;
- volumes;
- variáveis de ambiente;
- healthchecks;
- dependências.

Você deverá conseguir inicializar toda a aplicação através do Compose.

---

# Missão 07 — Healthchecks

Cada serviço deverá possuir um mecanismo apropriado de verificação de saúde quando fizer sentido.

Não utilize o mesmo Healthcheck para todos os serviços.

Pense:

text
API
↓
/health

PostgreSQL
↓
teste específico do banco

Redis
↓
teste específico do Redis


O objetivo é entender que Healthcheck precisa testar a coisa certa.

### Pergunta

Um container Up significa que a aplicação está pronta?

Explique sua resposta.

---

# Missão 08 — Dependências

Agora utilize o conhecimento do Dia 4.

Você deverá definir as dependências entre serviços.

Mas existe uma regra:

> Não confunda ordem de inicialização com disponibilidade.

Investigue como utilizar:

text
depends_on


em conjunto com:

text
healthcheck


e explique as limitações dessa abordagem.

---

# Missão 09 — Logs

Todos os serviços importantes deverão produzir logs úteis.

Você deverá conseguir responder:

- O que aconteceu?
- Quando aconteceu?
- Em qual serviço aconteceu?
- Qual requisição estava sendo processada?

Faça testes deliberadamente quebrando componentes.

Por exemplo:

- parar o banco;
- parar o Redis;
- remover a conexão com a fila;
- utilizar uma porta incorreta.

Depois tente diagnosticar o problema apenas observando a infraestrutura.

---

# Missão 10 — Falhas

Esta será uma das partes mais importantes do projeto.

Você deverá provocar falhas deliberadamente.

## Cenário 1

PostgreSQL indisponível.

Pergunta:

> O que acontece com a API?

---

## Cenário 2

Redis indisponível.

Pergunta:

> A aplicação inteira precisa parar?

---

## Cenário 3

Worker indisponível.

Pergunta:

> A API continua funcionando?

---

## Cenário 4

Queue indisponível.

Pergunta:

> O que acontece quando o usuário cria uma mensagem?

---

## Cenário 5

Container da API removido.

Pergunta:

> O que acontece com o restante da arquitetura?

---

## Cenário 6

Banco de dados removido.

Pergunta:

> Os dados continuam existindo?

---

# Missão 11 — Segurança

Faça uma revisão da arquitetura.

Investigue:

- quais portas estão publicadas;
- quais serviços estão acessíveis externamente;
- quais containers executam como root;
- quais informações estão no .env;
- quais informações estão dentro da imagem;
- quais serviços realmente precisam de acesso à rede.

O objetivo não é criar uma arquitetura perfeitamente segura.

O objetivo é identificar e documentar os riscos.

---

# Missão 12 — Teste de reconstrução

Agora vem o teste final.

Destrua toda a infraestrutura.

Remova os containers.

Reconstrua as imagens.

Suba novamente toda a aplicação.

Depois responda:

> O ambiente consegue ser recriado apenas a partir do código e das configurações versionadas?

Se a resposta for não, descubra o motivo.

---

# Matriz de decisões

Uma parte obrigatória do projeto será criar uma matriz explicando suas escolhas.

Exemplo:

| Problema | Tecnologia escolhida | Por quê? | Alternativas |
|---|---|---|---|
| Persistência do banco | ? | ? | Bind Mount |
| Cache | ? | ? | ? |
| Mensageria | ? | ? | ? |
| Entrada externa | ? | ? | ? |
| Comunicação interna | ? | ? | ? |
| Configuração | ? | ? | ? |
| Build | ? | ? | ? |
| Healthcheck | ? | ? | ? |

Não copie as respostas.

O objetivo é preencher a tabela depois de investigar cada caso.

---

# Guia de decisão

Durante o projeto você poderá utilizar estas perguntas para decidir qual tecnologia utilizar.

## Volume ou Bind Mount?

Pergunte:

> O Host precisa manipular diretamente esses arquivos?

Se sim, investigue Bind Mount.

Se o armazenamento pertence à aplicação e deve ser gerenciado pelo Docker, investigue Volumes.

---

## Porta publicada ou apenas porta interna?

Pergunte:

> Um usuário externo precisa acessar esse serviço?

Se não, provavelmente não existe motivo para publicar a porta no Host.

---

## Uma rede ou várias?

Pergunte:

> Quais serviços precisam realmente conversar?

Crie a arquitetura a partir das necessidades de comunicação, e não simplesmente colocando tudo na mesma rede.

---

## Cache ou banco?

Pergunte:

> O dado precisa ser a fonte definitiva da verdade?

Se sim, provavelmente o banco é o lugar adequado.

Se o dado pode ser reconstruído e o objetivo é reduzir custo de consultas, investigue cache.

---

## Processamento síncrono ou assíncrono?

Pergunte:

> O usuário precisa esperar o processamento terminar?

Se não, investigue uma fila e um Worker.

---

## Multi-stage ou Dockerfile simples?

Pergunte:

> Existe uma etapa de compilação/build que não precisa existir no ambiente final?

Se sim, Multi-stage provavelmente faz sentido.

---

## Healthcheck

Pergunte:

> Qual evidência realmente demonstra que esse serviço está pronto?

O Healthcheck deverá testar essa condição.

---

## Reverse Proxy

Pergunte:

> Preciso expor todos os serviços diretamente?

Se não, investigue uma camada única de entrada.

---

# Estrutura sugerida do projeto

Você poderá organizar o projeto desta maneira:

text
projeto-final/

├── README.md
│
├── compose.yaml
├── .env.example
├── .gitignore
├── .dockerignore
│
├── docs/
│   ├── arquitetura.md
│   ├── decisoes.md
│   ├── troubleshooting.md
│   ├── seguranca.md
│   └── testes.md
│
├── frontend/
│   ├── Dockerfile
│   └── ...
│
├── api/
│   ├── Dockerfile
│   └── ...
│
├── worker/
│   ├── Dockerfile
│   └── ...
│
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
│
└── ...


A estrutura não é obrigatória.

Você poderá modificá-la conforme suas decisões arquiteturais.

---

# Entregáveis

Ao finalizar o projeto, seu repositório deverá conter:

## Infraestrutura

- compose.yaml
- Dockerfiles
- .dockerignore
- .env.example

## Aplicação

- Frontend
- Backend
- Worker

## Infraestrutura de dados

- PostgreSQL
- Redis
- Message Queue

## Operação

- Healthchecks
- Logs
- Reverse Proxy
- Redes
- Volumes

## Documentação

- Arquitetura
- Decisões
- Troubleshooting
- Segurança
- Testes

---

# Documentação das decisões

Para cada decisão importante, utilize este formato:

## Decisão

*Problema:*

Qual problema precisava ser resolvido?

*Alternativas consideradas:*

Quais soluções poderiam ser utilizadas?

*Solução escolhida:*

Qual solução foi utilizada?

*Motivo:*

Por que ela foi escolhida?

*Trade-offs:*

O que foi ganho?

O que foi perdido?

*Consequências:*

Como essa decisão influencia o restante da arquitetura?

---

# Critérios de sucesso

O projeto será considerado concluído quando:

- toda a infraestrutura puder ser inicializada pelo Compose;
- os serviços conseguirem se comunicar;
- os dados importantes forem persistentes;
- serviços internos não sejam desnecessariamente expostos;
- existam Healthchecks adequados;
- existam logs úteis;
- exista Reverse Proxy;
- exista processamento assíncrono;
- exista cache;
- os Dockerfiles estejam otimizados;
- a aplicação consiga ser reconstruída;
- a arquitetura esteja documentada.

Mas existe um critério ainda mais importante:

> *Você precisa conseguir explicar a arquitetura sem abrir o código.*

---

# Desafio Extra — Quebre sua própria arquitetura

Depois de terminar, tente quebrar o projeto.

Faça testes como:

text
Parar o PostgreSQL
Parar o Redis
Parar o Worker
Parar a Queue
Remover a API
Remover um container
Recriar um serviço
Apagar os containers
Reconstruir as imagens


Depois responda:

> O que sobreviveu?

> O que foi perdido?

> O que se recuperou automaticamente?

> O que precisou de intervenção?

> Onde estavam os pontos únicos de falha?

---

# Desafio Final — Explique sua arquitetura

Imagine que você esteja em uma entrevista técnica.

O entrevistador pergunta:

> "Explique a arquitetura Docker que você construiu."

Você deverá conseguir explicar:

text
Como uma requisição chega
        ↓
Como ela é roteada
        ↓
Como chega à API
        ↓
Como a API acessa o banco
        ↓
Como utiliza o cache
        ↓
Como publica eventos
        ↓
Como o Worker processa os eventos
        ↓
Como os dados são persistidos
        ↓
Como você monitora a saúde dos serviços
        ↓
Como você diagnostica uma falha


Se você conseguir explicar esse fluxo e justificar as decisões, o projeto cumpriu seu objetivo.

---

# Reflexão Final

Ao terminar o projeto, responda:

- Qual foi a decisão arquitetural mais difícil?
- Qual tecnologia você utilizou que não conhecia antes do intensivão?
- Qual problema você demorou mais para diagnosticar?
- Qual componente poderia ser removido?
- Qual componente seria mais difícil de substituir?
- Onde estão os pontos únicos de falha?
- O que você faria diferente em uma segunda versão?
- O que ainda faltaria para levar essa arquitetura para produção real?

---

# Conclusão do Intensivão

O objetivo destes sete dias nunca foi decorar Docker.

Durante o intensivão, você começou com um único container e gradualmente construiu uma arquitetura composta por múltiplos serviços.

Você passou por:

text
Container
   ↓
Persistência
   ↓
Redes
   ↓
Comunicação
   ↓
Compose
   ↓
Build profissional
   ↓
Observabilidade
   ↓
Produção


O projeto final representa a integração de todos esses conhecimentos.

O resultado mais importante, entretanto, não é o compose.yaml.

É a capacidade de olhar para um problema de infraestrutura e perguntar:

> *"Qual problema estou tentando resolver e qual é a solução mais adequada para esse contexto?"*

Essa é a habilidade que este intensivão pretende desenvolver.