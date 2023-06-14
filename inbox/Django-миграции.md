#может_пригодится

# Миграции

## Накатить

```shell
cd www
python manage.py migrate
```

## Как накатить миграции на logs-бд

```shell
python manage.py migrate --database=logs
```

## Смерджить

```sh
python manage.py makemigrations --merge
```

