#ops #docker #psql

# Работа с бекапами в Docker

## Переименование бд

- Скорее всего, на локалке уже "накачен" бекап, так что надо переименовать бд
- Подключаемся:

```shell
psql -U postgres
```

- ^попросит пароль - его можно взять из `.env`
- Переименовываем:

```sql
alter database risx rename to risx_;
```

- **Важно:** нужно отключить все соединения к бд (в тч подключение из PyCharm через вкладку Database)

### Отключить активные соединения к бд

```sql 
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'risx'
  AND pid <> pg_backend_pid();
```

- [Источник](https://stackoverflow.com/a/5408501/5500609)

## Накатить бекап

- Если прислали архив, типа `tar.gz`, надо его разархивировать в `.sql`-файл
- Далее накатить в Docker:

```shell
cat {backup}.sql | docker exec -i postgresql psql -U postgres

cat backups/{backup}.sql | docker exec -i risx-deploy_db_1 psql -U postgres
```

- ^этот вариант для небольших бекапов
- [Вариант](https://stackoverflow.com/a/60043344/5500609) для больших бекапов:

```bash
docker cp {backup}.dump {postgresql}:/db.dump
docker exec -it postgresql bash
# Для .dump файлов
pg_restore -U postgres -d risx --no-owner -1 /db.dump
# Для .sql файлов
psql -U postgres -d risx -f db.dump
```

- Пример:

```sh
docker cp C:\Users\potyk\Downloads\backup\backup.sql postgresql:/db.dump
docker exec -it postgresql bash
# Для .dump файлов
pg_restore -U postgres -d risx --no-owner -1 /db.dump
# Для .sql файлов
psql -U postgres -d risx -f db.dump
```

## Сброс пароля

```shell
docker exec -i postgresql psql -h localhost -U postgres -c "ALTER USER postgres PASSWORD '12345';"
```
