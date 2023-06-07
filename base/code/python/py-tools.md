#py #тулзы #dev-тулзы 

# Python Libs

Что я использую для ежедневной разработки

## Тестирование

- [pytest](https://docs.pytest.org/en/7.3.x/) - базовый фреймворк для тестирования
- [syrupy](https://github.com/tophat/syrupy) - снепшот-тестирование 
	- полезно когда в тесте генеришь большой джсон/док, и сравниваешь его с эталонным
- [factoryboy](https://factoryboy.readthedocs.io/en/stable/) - генератор тестовых сущностей
- [freezegun](https://github.com/spulec/freezegun)  - мок дат
- [pyhamcrest](https://github.com/hamcrest/PyHamcrest) - красивые ассерты
	- [dirty-equals](https://github.com/samuelcolvin/dirty-equals) - еще вариант, посвежее, от автора pydantic

## QA / Lint

- [Ruff](https://github.com/charliermarsh/ruff) - оч быстрый линтер
	- быстрее flake8 и уж тем более pylint
- [mypy](https://mypy-lang.org/) - чекер тайпингов
	- ничего лучше него нет (pyright робит хуже)
	- хотя и mypy не идеален, часто надо бороться с ним 
	- так что внедрять его надо либо со старта, либо очень урезанно, либо вообще не внедрять
- [black](https://github.com/psf/black) - хороший форматтер кода
	- есть [плагины для IDE](https://black.readthedocs.io/en/stable/integrations/editors.html)

