#py #dev-тулзы 

# helium

## Что это?

- [helium](https://github.com/mherrmann/selenium-python-helium) - обертка над [Selenium](https://www.selenium.dev/) - либой для автоматизации бразузера 
- Как работать с ней написано в [читшите](https://github.com/mherrmann/selenium-python-helium/blob/master/docs/cheatsheet.md)
- [Дока](https://selenium-python-helium.readthedocs.io/en/latest/index.html))

### Зачем автоматизировать браузер?

- Чтобы тестить сайты
- Чтобы скрепить сайты: стягивать инфу с сайтов без апи ~~и регистрации~~
    - Пример - [скачиватель залайканных картинок из ВК](https://github.com/potykion/my-vk-likes)

### Чем helium лучше selenium?

- Не надо дополнительно ставиться драйверы - `helium.start_firefox` и погнали
    - Хотя с хромом [чето беда](https://github.com/mherrmann/selenium-python-helium/issues/89)
- Основное преимущество - упрощенное апи
    - Хочешь нажать на кнопку с текстом - так и пиши: `helium.click('button text')`
- Полная совместимость с Selenium - знания о Selenium (напр. `WebElement`) тут будут на руку

## Пример кода

```python
# Смело импортим все
from helium import *

# Стартуем браузер
# Присваивать переменной - опционально
driver = start_firefox()

# click - начатие на что либо
# Дока подразумевает, что кликать можно так - просто указав текст кнопки
# Но для русского языка это не робит
# click("Распределение активов")
# Так что кликаем используя css-селектор
share_details = S(".col-xl-9 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
click(share_details)

# doubleclick - иногда click срабатывает со второго раза - так что юзаем двойной клик
doubleclick(S(".btn-primary"))

# write - заполнить инпут
# Здесь пишем "20" в инпут, который находится справа от надписи "TMOS.MCX"
write("20", into=TextField(to_right_of="TMOS.MCX"))

# Получение текста
S("span.text-success:nth-child(3)").web_element.text
```

## Нюансы

- `helium.scroll_down` чет не оч робит - лучше юзать `helium.press(ARROW_DOWN)`
- На 2023-06-08 при установке свежей версии helium будем получать [странную ошибку про таймаут](https://github.com/mherrmann/selenium-python-helium/issues/107)
	- [Дело в `urllib3>=2`](https://stackoverflow.com/questions/76180798/jenkins-job-failing-for-urllib3-valueerror-timeout-value-connect-was-object-o) - решение откат на `urllib3==1.26.16`

## Рецепты

### Получение аттрибута, типа `href`

```python
S.web_element.get_attribute('href')
```

- `S` - то, что получаем при вызове `find_all` 
