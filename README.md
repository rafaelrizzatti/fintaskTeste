## Fintask Teste Técnico

Desafio técnico para Fintask. O Desafio se encontra em um pdf no Projeto.
Para execução do projeto que se encontra dentro de um docker, executar os comandos:

* docker-compose up --build

Após isso, utilizar o comando "docker ps" para pegar o ID do container que está rodando o Projeto.
Para criar o banco de dados inicial, utilizar os comandos:

* docker exec -it (container_id) python manage.py makemigrations
* docker exec -it (container_id) python manage.py migrate

Para ter acesso ao django admin, criar um super usuario com o comando:

* docker exec -it (container_id) python manage.py cratesuperuser

Dentro do Django Admin, como usuario Administrador, você terá acesso a todos Usuarios (Anunciantes e Administradores) e a todas Demandas.

Um anunciante pode realizar o seu proprio cadastro através da API.
Após feito cadastro ele obterá um Token, que irá permitir a manipulação de suas Demandas.

### API Endpoints
* /admin/ (Acesso apenas por Usuarios Administradores)
* /api/users/ (Cadastro de Usuarios)
* /api/users/login (Obtenção do Token para acesso a suas demandas)
* /api/demandas/ (Listagem de Demandas e Criação de Demandas)
* /api/demandas/ID/ (Leitura, Alteração e Exclusão de Demandas)
* /api/demandas/ID/finalizar/ (Finalização de uma Demanda)

