#mkdocs 

# mkdocstrings

- [mkdocstrings-python](https://mkdocstrings.github.io/python/) - позволяет вставлять в mkdocs-доку описания python-модулей и их содержимого, включая классы, методы и тд

## Установка

```
pip install mkdocstrings[python]
```

```yaml
# mkdocs.yml
plugins:
  - mkdocstrings:
      handlers:
        python:
	      # Путь к пакету с модулями - здесь используем пакет, который находится на 2 уровня выше в директории reborn_lol
          paths: [ ../../reborn_lol ]
          options:
            # При выводе классов по умолчанию выводятся родители класса - обычно это не нужно - лишний шум
			show_bases: false
			# Настройки хедеров (h1, h2) -  
			# в них пишется название члена модуля (напр. названия классов и методов в модуле)  
			# Отображать ли хедеры  
			# show_root_heading: true  
			# Как рендерить хедер h1, h2, h3 - в данном случае h3  
			# heading_level: 3  
			# Показывать полный путь к члену модуля или нет  
			# false: CardAcquiringType  
			# true: bank.core.acquiring_types.CardAcquiringType  
			# show_root_full_path: false  
			# Хз  
			# show_root_toc_entry: false
```

## Вывод содержимого класса в доку

- Указываем путь к классу

```yml
::: bank.core.acquiring_types.CardAcquiringType
	# По умолчанию выводится весь исходный код класса + его аттрибуты и методы - отрубаем их, нам достаточно исходного кода класса
    options:
      members: false
```
