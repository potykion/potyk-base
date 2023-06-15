#py #django

# Миграции в Django

- Миграция - код, который запускает команды обновления бд
- Например, захотели сделать новую колонку - добавляем в модель, затем создаем *миграцию*

## Основные команды

```shell
# Создание миграции
python manage.py makemigrations
# Создание пустой миграции
python manage.py makemigrations {app} --empty
# Применение миграции
python manage.py migrate
# Применение миграции на другую базу (кейс нескольких бд)
python manage.py migrate --database=logs
# Мердж миграций
```

## Как запускать код в миграции?

```python
from __future__ import unicode_literals

from django.db import migrations


# 3. Сигнатура = apps, schema_editor:
#   - apps - django-appы на момент миграции; из них мы получаем модели, актуальные на момент миграции; 
#       то есть если в следующей миграции мы добавили в модель новое поле, то в рамках этой миграции нового поля еще нет
#   - schema_editor - обычно не пригождается
def do(apps, schema_editor):
    # 4. Модели получаем, используя apps.get_model + указываем апп и модель - 
    #   получаем django.db.models.Model-class
    User = apps.get_model('app', 'User')


class Migration(migrations.Migration):
    dependencies = [
        ...
    ]

    operations = [
        # 1. RunPython - для запуска кода
        migrations.RunPython(
            # 2. Определяем метод с запускаемым кодом
            do,
            # 5. Миграции по своей сути откатываемы, но обычно код не нужно откатывать, поэтому используем noop
            reverse_code=migrations.RunPython.noop,
        )
    ]
```

### Зач это нужно?

- Для переноса данных из одной сущности в другую
- Для заполнения данных пресетами
- Создать новые сущности из других

## Как переименовать поле?

```python
migrations.RenameField(
    model_name='study',
    old_name='many_msp',
    new_name='msp',
)
```