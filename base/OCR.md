#тулзы 

# OCR

## OCR.Space

- https://ocr.space/ocrapi
- **Самый изевый вариант**: просто регаешься, получаешь api-ключ на почту, кидаешь запросики:

```http
POST https://api.ocr.space/parse/image  
ApiKey: K8454439234323432 
Content-Type: application/x-www-form-urlencoded  
  
language=rus&filetype=jpg&url=https://skovoroda-static.storage.yandexcloud.net/images/0772fbe1830cb29afbe7c29af8ce7ba725129e5658ed72fcc5e801873848f2a1.jpg
```

## EasyOCR

- https://github.com/JaidedAI/EasyOCR
- Python-либа
- Вроде просто `pip install easyocr`, но там еще хуйлиард мл-либ качается, типа торча (~~я не торч я просто дунул~~) и куда (~~куда? каво~~)
- Потом еще модель сама качается
- Потом в докере это не на изичах поднимается
- Так что **норм вар на локалке на винде запустить, но деплоить на сервак — чет гемор**
- А в коде пользоваться просто - ниже FastAPI ендпоинт, который на вход принимает url картинки, а на выходе выдает опознанный текст в виде строки:

	```python
	import easyocr  
  
	import httpx  
	from fastapi import FastAPI  
	  
	app = FastAPI()  
	  
	  
	@app.post("/")  
	def ocr(image_url: str):  
		image_data = httpx.get(image_url).content  
		  
		reader = easyocr.Reader(['ru'])  
		result = reader.readtext(image_data, output_format='dict')  
		text = '\n'.join([r['text'].title() for r in result])  
		  
		return {"text": text}
	```

## Еще варианты

- https://huggingface.co/microsoft/trocr-base-printed - OCR от Microsoft, аналогично EasyOCR — надо написать Python-скрипт и нести за собой ml-зоопарк либ
- https://huggingface.co/tasks/image-to-text - ну и весь ml-движ тут