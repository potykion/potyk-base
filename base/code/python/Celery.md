#py #celery 

# Celery

## Что есть что и как запускать?

### celeryd

`celeryd`  - celery-worker - выполняет таски, прибывающие на celery

Запуск:

```
python manage.py celeryd -Q celery,backup,hl7,duplicates --loglevel=INFO --purge
```

### celerybeat

`celerybeat` - celery-планировщик - добавляет в очередь (брокер сообщений) задачи по расписанию (напр. через крон)

Запуск:

```
python manage.py celerybeat --loglevel=INFO
```

## Как отменять таски?

```python
# lock.core.LockService.unlock
from www.celery_conf import app

app.control.revoke(task_id, terminate=True)
```

[Источник](https://stackoverflow.com/questions/8920643/cancel-an-already-executing-task-with-celery)

### Внутри таски

```python
# hl7_server.tasks.client_query

@shared_task(bind=True)
def client_query(self, service_hl7_id, message_er7, task_id=None):
    self.app.control.revoke(task_id, terminate=True)
```

- **Важно:** нужно указывать `bind=True`, чтобы в таске был `self`

### Как посмотреть отмененные таски?

```python
app.control.inspect().revoked()
```

## Как запускать cron по таймзоне?

Сделать partial-функцию, у которой `nowfun` будет генерить дату с таймзоной:

```python
import datetime as dt
from functools import partial
import pytz
from celery.schedules import crontab
from django.conf import settings

tz_crontab = partial(
    crontab,
    nowfun=lambda: dt.datetime.now(pytz.timezone(settings.TIME_ZONE)),
)

CELERYBEAT_SCHEDULE = {
    'load_daily_stats': {
        'task': 'statistics.tasks.load_daily_stats',
        'schedule': tz_crontab(hour=0, minute=0),
    },
}
```

[Источник](https://stackoverflow.com/questions/21827290/celery-beat-different-time-zone-per-task)

## Ссылочки

- [First steps with Django — Celery 5.3.0b1 documentation](https://docs.celeryq.dev/en/latest/django/first-steps-with-django.html)
- [celery.app.control — Celery 5.2.7 documentation](https://docs.celeryq.dev/en/stable/reference/celery.app.control.html)
- [python - Right way to use celery.app.control in celery - Stack Overflow](https://stackoverflow.com/questions/63993789/right-way-to-use-celery-app-control-in-celery)
