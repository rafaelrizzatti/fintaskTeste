## Fintask Teste Técnico

Desafio técnico para Fintask. O Desafio se encontra em um pdf no Projeto. (Avaliacao_desenvolvedor.pdf)

Para execução do projeto que se encontra dentro de um docker, executar os comandos:

* docker-compose up --build

Após isso, em outro terminal, utilizar o comando "docker ps" para pegar o ID do container que está rodando o Projeto.
Para criar o banco de dados inicial, utilizar os comandos:

* docker exec -it (container_id) python manage.py makemigrations
* docker exec -it (container_id) python manage.py migrate

Para ter acesso ao django admin, criar um super usuario com o comando:

* docker exec -it (container_id) python manage.py cratesuperuser

Dentro do Django Admin, como usuario Administrador, você terá acesso a todos Usuarios (Anunciantes e Administradores) e a todas Demandas.

Um anunciante pode realizar o seu proprio cadastro através da API.
Após feito cadastro ele obterá um Token, que irá permitir a manipulação de suas Demandas.

Para execução dos Testes:

* docker exec -it (container_id) python manage.py test

### API Endpoints
* /admin/ (Acesso apenas por Usuarios Administradores)
* /api/users/ (Cadastro de Usuarios)
* /api/users/login (Obtenção do Token para acesso a suas demandas)
* /api/demandas/ (Listagem de Demandas e Criação de Demandas)
* /api/demandas/ID/ (Alteração e Exclusão de Demandas)
* /api/demandas/ID/finalizar/ (Finalização de uma Demanda)

Dentro do Projeto tem um arquivo que pode ser usado no Postman para importação e utilização dos Endpoints.

E também aqui uma documentação do Postman para utilização em variadas linguagens: https://documenter.getpostman.com/view/7986826/TW6xp8gy

Quaisquer dúvidas, entrar em contato: rafael.rizzatti@gmail.com
