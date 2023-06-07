#mkdocs

# Как расширить MkDocs

>Как изменить содержимое md-страницы перед сборкой mkdocs?

## Задача

- В MkDocs теги указываются с помощью front-matter (`tags: - tag`), а в Obsidian с помощью `#хештега`
- Хочется при сборке mkdocs-доки заменять хештеги на front-matter, или чтобы `tags`-plugin понимал не только front-matter, а еще и хештеги

## Решение

- `tags`-plugin берет теги из front-matter страницы: т.е. из meta страницы - значит, нам нужно спарсить строку с хештегами и вставить их в meta страницы
- Использовать [hooks](https://www.mkdocs.org/user-guide/configuration/#hooks):

Пишем хук:

```python
# .mkdocs/hooks/transform_obs_tags.py

import logging
import re
import string

import mkdocs.plugins

log = logging.getLogger("mkdocs")

# 2. Опциональный приоритет хука
# Здесь 100 означает, что хук будет запущен перед плагинами
@mkdocs.plugins.event_priority(100)
# 1. Хук - это просто функция, которая является event-handler-ом в плагинах
# https://www.mkdocs.org/dev-guide/plugins/#events
# Здесь on_page_markdown - это функция, которая будет запускаться для каждой md-страницы
# В рамках нашей задачи мы хотим спарсить строки, которые содержат хештеги и вставить их в meta страницы
def on_page_markdown(markdown, page, **kwargs):
    """
    Парсит obsidian-теги (#тег) и выставляет их в meta страницы
    + Чекает что теги на английском
    """
    def _lines():
        lines = markdown.split('\n')

        for line in lines:
	        # 3. Реализацию пишешь сам
	        # Я сделал итерацию по всем строкам, и если строка начинается с хештега, 
			#   то строку не включаем в страницу, а теги вставляем в meta
            if re.match('#([\w|-]+)', line):
                tags = re.findall(r'#([\w|-]+)', line)
                page.meta['tags'] = tags
            else:
                yield line

    markdown = '\n'.join(_lines())

    return markdown

```

Подключаем хук:

```yaml
hooks:  
  - .mkdocs/hooks/transform_obs_tags.py
```

Все, должно заработать