#ops #docker

# Обновление БД в Docker

## Как обновить psql в docker?

- **https://betterprogramming.pub/how-to-upgrade-your-postgresql-version-using-docker-d1e81dbbbdf9**
- https://postgrespro.ru/docs/postgresql/11/upgrading
- https://docs.tibco.com/pub/mash-local/4.3.0/doc/html/docker/GUID-BD850566-5B79-4915-987E-430FC38DAAE4.html
- https://stackoverflow.com/questions/26331651/how-can-i-backup-a-docker-container-with-its-data-volumes#:~:text=To%20backup%20a%20data%20volume,data%20for%20a%20MySQL%20server
  .

### Бекапимся

```shell
docker-compose exec db pg_dumpall -U postgres > dump-2022-07-05.sql
```

### Удаляем volumes

- https://docs.docker.com/engine/reference/commandline/volume_rm/
- https://stackoverflow.com/questions/34658836/docker-is-in-volume-in-use-but-there-arent-any-docker-containers

```shell
docker-compose down --volume  
```

### Обновляем версию

Для тестов db-сервис собираем из `postgres_ru/Dockerfile`, а не из registry-image:

```yaml
# docker-compose.yml

services:
  db:
    # image: docker.ris-x.com:5000/risx-db:1.1
    # container_name: postgresql
    build: ./postgres_ru/

```

И меняем версию в `postgres_ru/Dockerfile`:

````dockerfile
# FROM postgres:9.6
FROM postgres:14.4

RUN localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias ru_RU.UTF-8
ENV LANG ru_RU.utf8
````

### Накатываем бекап

```shell
docker cp C:\Users\potyk\Downloads\backup\backup.sql risx-deploy_db_1:/db.dump  
docker-compose exec db bash
psql -U postgres
> create database risx; 
> \q
psql -U postgres -d risx < db.dump
psql -U postgres -c "ALTER USER postgres PASSWORD '12345';"
```

### Сбрасываем пароль юзеру

```python
from risx.models import User

u = User.objects.get(username='dav')
u.set_password('1')
u.save()
```


## Как обновить redis в docker? 

Просто стянуть свежий образ - все должно робить

