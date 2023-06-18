#tools  

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

- На выбор предоставляется 3 OCREngine - если какая-то плохо работает, то имеет смысл выставить другие, передавая опцию: `OCREngine=2`, `OCREngine=3`

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

	```python
	"""  
	https://huggingface.co/docs/transformers/quicktour  
	https://huggingface.co/tasks/image-to-text  
	https://huggingface.co/microsoft/trocr-base-printed  
	https://huggingface.co/docs/transformers/model_doc/trocr  
	"""  
	  
	from transformers import TrOCRProcessor, VisionEncoderDecoderModel  
	from PIL import Image  
	import requests  
	  
	  
	if __name__ == '__main__':  
	url = 'https://skovoroda-static.storage.yandexcloud.net/images/0772fbe1830cb29afbe7c29af8ce7ba725129e5658ed72fcc5e801873848f2a1.jpg'  
	image = Image.open(requests.get(url, stream=True).raw).convert("RGB")  
	  
	processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')  
	model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')  
	pixel_values = processor(images=image, return_tensors="pt").pixel_values  
	  
	generated_ids = model.generate(pixel_values)  
	generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]  
	  
	print(f'{generated_text=}')
	```

- https://huggingface.co/tasks/image-to-text - ну и весь ml-движ тут
- Еще есть Облачные OCR: 
	- [Google Cloud Vision](https://cloud.google.com/vision/docs/ocr) 
	- [Yandex Cloud Vision](https://cloud.yandex.ru/services/vision)
- Еще популярный OCR - [Tesseract](https://github.com/tesseract-ocr/tessdoc)
	- Для него есть куча оберток, напр. на [go](https://github.com/otiai10/gosseract)
- https://github.com/PaddlePaddle/PaddleOCR
- https://github.com/katanaml/sparrow