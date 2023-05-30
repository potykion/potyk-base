#py 

# Python либы


### Веб-фреймворки  
  
- [Django](https://www.djangoproject.com/) - самый популярный веб-фреймворк, куча функций из коробки (ака batteries included), куча интеграций; если хочется писать сервера на питоне, и не знаешь с чего начать - бери джангу - пусть генерится куча файлов на старте, но разобравшись в них, понимаешь, что фреймворки строятся на тех же концепциях  
- [Django REST framework](https://www.django-rest-framework.org/) - мастхев чтобы писать апишки  
- [Django Ninja](https://django-ninja.rest-framework.com/) - надстройка над DRF, которая позволяет писать апишки в стиле FastAPI - с помощью тайпингов и Pydantic  
- [drf-yasg](https://github.com/axnsan12/drf-yasg) - лучший генератор swagger-доки для джанги  
- [wagtail](https://github.com/wagtail/wagtail) - cms для джанги  
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - самый простой веб-фреймворк - начать можно с [1 файла с 5 строчками](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart); но по сравнению с Джангой, мало батареек в коробке - надо куча всего доустанавливать - в итоге получается та же джанга  
- [aiohttp](https://docs.aiohttp.org/en/stable/) - один из первых асинхронных фреймворков; по фичам - аналогичен фласку: в коробке роутинг, мидлваре, простенький сёрв статики; суть асинхронности в том, что повышается производительность серва; еще в коробке есть асинхронный веб-клиент  
- [FastAPI](https://fastapi.tiangolo.com/) - еще один асинхронный фреймворк (но можно писать и в синхронном стиле), суть в том, что схемы запросов и ответов можно описывать, используя тайпинги и Pydantic + есть интеграция со сваггером из коробки + неплохой диай на функциях  
  
---  
  
### Работа с бд  
  
- Django ORM - лучшная ормка, идет в комплекте с Django  
- [Sqlalchemy](https://www.sqlalchemy.org/) - лучшая либа для работы с бд, если не Django-проект; есть и орм, и возможность писать скл, используя sqlalchemy-конструкции, и писать сырой sql; есть куча дополнений, типа [миграций](https://alembic.sqlalchemy.org/en/latest/), [утилит по созданию бд](https://sqlalchemy-utils.readthedocs.io/en/latest/); альтернативы: [peewee](http://docs.peewee-orm.com/en/latest/) - лайтовая ормка  
- [aiopg](https://github.com/aio-libs/aiopg) - асинхронная работа с постгресом, есть интеграция с sqlalchemy-запросами; альтернативы: [asyncpg](https://github.com/MagicStack/asyncpg)  
- [repka](https://github.com/potykion/repka) - _собственная разработка_, асинхронная абстракция над бд на базе aiopg  
- [pymongo](https://pymongo.readthedocs.io/en/stable/) - официальный клиент для работы с монгой, есть [асинхронная версия](https://motor.readthedocs.io/en/stable/)  
  
---  
  
### Веб-клиенты  
  
- [requests](https://github.com/psf/requests) - самая популярная либа для http-запросов  
- [httpx](https://github.com/encode/httpx) - асинхронный хттп-клиент - альтернатива aiohttp; [respx](https://github.com/lundberg/respx) - моки для либы  
- [python-zeep](https://github.com/mvantellingen/python-zeep) - SOAP клиент  
- [requests-html](https://docs.python-requests.org/projects/requests-html/en/latest/) - лучший парсер html; альтернативы: [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
- [splinter](https://github.com/cobrateam/splinter) - более высокоуровневая обертка над [Selenium](https://github.com/SeleniumHQ/selenium/) - штукой для управлением браузера; альтернативы: [helium](https://github.com/mherrmann/selenium-python-helium)  
  
---  
  
### Работа с данными  
  
- [pydantic](https://github.com/samuelcolvin/pydantic) - комбо из питоновских дата-классов и парсилки джсона - очень приятно с данными работать становится; есть [плагин на pycharm](https://github.com/koxudaxi/pydantic-pycharm-plugin); альтернативы: [питоновские датаклассы](https://docs.python.org/3/library/dataclasses.html), [attrs](https://www.attrs.org/en/stable/), [marshmallow](https://marshmallow.readthedocs.io/en/stable/)  
- [humps](https://github.com/nficano/humps) - конвертит словари из одного нейминга в другой  
- [more-itertools](https://github.com/more-itertools/more-itertools) - различные утилитки для работы с коллекциями  
- [parse](https://pypi.org/project/parse/) - противоположность `format` - позволяет парсить строки по шаблону, не упарываясь регулярками  
  
---  
  
### Работа с документами  
  
- [jinja2](https://jinja.palletsprojects.com/en/2.11.x/) - лучший шаблонизатор  
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - лучшая либа для работы с xlsx  
- [jinja2xlsx](https://github.com/potykion/jinja2xlsx) - _собственная разработка_, конвертит html-таблицы в openpyxl-таблицы  
- [python-pdfkit](https://github.com/JazzCore/python-pdfkit) - лучший конвертер хтмл в пдф на базе [wkhtmltopdf](https://wkhtmltopdf.org/)  
- [python-docx-template](https://github.com/elapouya/python-docx-template) - jinja2 шаблоны в ворде  
- [docci](https://github.com/potykion/docci) - _собственная разработка_, абстракция работы с файлами: определение mime-type, конвертация в base64, сохранение/загрузка; а также работа с зип-архивами, эксельками, директориями  
- [xmltodict](https://github.com/martinblech/xmltodict) - нормальная работа с xml  
  
---  
  
### QA  
  
#### Качество кода  
  
- [black](https://github.com/psf/black) - форматтер кода  
- [mypy](https://github.com/python/mypy) - чекер типизации; альтернативы: [pyright](https://github.com/microsoft/pyright), [pytype](https://github.com/google/pytype)  
- [flake8](https://github.com/PyCQA/flake8) - линтер, есть [куча плагинов](https://github.com/DmytroLitvinov/awesome-flake8-extensions), быстрее [pylint](https://github.com/PyCQA/pylint)  
- [pydocstyle](https://github.com/pycqa/pydocstyle) - линтер, проверяющий наличие докстрингов  
- [pre-commit](https://github.com/pre-commit/pre-commit) - пре-коммит хуки - запуск штук, описанных выше, перед каждым коммитом; считай локальный сиай  
  
#### Тестирование  
  
- [pytest](https://github.com/pytest-dev/pytest/) - лучший фреймворк для тестирования; есть [куча плагинов](https://github.com/search?q=pytest)  
- [responses](https://github.com/getsentry/responses) - моки для [requests](https://github.com/psf/requests)  
- [aioresponses](https://github.com/pnuckowski/aioresponses) - моки асинхронных хттп-запросов через aiohttp; альтернативы: [aresponses](https://github.com/aresponses/aresponses)  
- [freezegun](https://github.com/spulec/freezegun) - моки для дейттайма  
- [PyHamcrest](https://github.com/hamcrest/PyHamcrest) - матчеры для тестов  
- [factory_boy](https://factoryboy.readthedocs.io/en/stable/) - тестовые фабрики - генерят объекты с фейковыми данными; альтернативы: [model-bakery](https://pypi.org/project/model-bakery/) - для джанги  
  
#### Логгирование, профилирование, отладка  
  
- [loguru](https://github.com/Delgan/loguru) - лучшая либа для логгирования  
- [stackprinter](https://github.com/cknd/stackprinter) - получше стектрейс; альтернативы: [PySnooper](https://github.com/cool-RR/PySnooper)  
- [scalene](https://github.com/plasma-umass/scalene) - профилировщик  
  
---  
  
### Девопс  
  
- [gunicorn](https://gunicorn.org/) - популярный WSGI-сервер - масштабирует однопроцессорный сервы, типа джанги; альтернативы: [uvicorn](https://www.uvicorn.org/) - асинхронный WSGI-сервер - ASGI  
- [Supervisor](http://supervisord.org/) - управление процессами - автоматически запускает/перезапускает процессы на линукс-машинке, напр. gunicorn, альтернативы: [Docker](https://www.docker.com/)  
- [Fabric](http://www.fabfile.org/) - выполнение команд на удаленной машине; альтернативы: [ansible](https://docs.ansible.com/)  
  
---  
  
### Прочее  
  
- [poetry](https://github.com/python-poetry/poetry) - лучший менеджер зависимостей; есть [плагин для пайчарма](https://github.com/koxudaxi/poetry-pycharm-plugin)  
- [pyjwt](https://pyjwt.readthedocs.io/en/stable/) - работа с jwt-токенами  
- [python-dotenv](https://pypi.org/project/python-dotenv/) - читает .env-файл - файл с переменными окружения - удобно для локальных настроек  
- [python-dependency-injector](https://github.com/ets-labs/python-dependency-injector) - норм ioc контейнер  
- [celery](https://github.com/celery/celery) - либа для работы с очередями задач; альтернативы: [dramatiq](https://github.com/Bogdanp/dramatiq), [rq](https://github.com/rq/rq)  
- [click](https://github.com/pallets/click) - либа для создания кли приложений; альтернативы: [typer](https://github.com/tiangolo/typer) - кли на тайпингах; [Gooey](https://github.com/chriskiehl/Gooey) - делает юай из кли  
- [babel](http://babel.pocoo.org/en/latest/) - либа для локализации  
- [pillow](https://pillow.readthedocs.io/en/stable/) - популярная либа для работы с картинками  
- [pypiserver](https://github.com/pypiserver/pypiserver) - pypi сервер - полезно когда надо есть корпоративные либы  
- [notifiers](https://github.com/liiight/notifiers) - либа для отправки уведомлений, напр. через Pushover; альтернативы: [apprise](https://github.com/caronc/apprise)  
- [Sourcetrail](https://github.com/CoatiSoftware/Sourcetrail) - строит граф зависимостей / иерархию классов; есть [плагин для пайчарма](https://github.com/CoatiSoftware/idea-sourcetrail)
- https://github.com/PrefectHQ/marvin - pydantic-ai модели - считай типизированный скрепинг
