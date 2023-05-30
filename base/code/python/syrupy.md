#py

# Syrupy

## Как сделать снепшоты в pdf?

1. Делаем класс:

	```python
	from syrupy.extensions.single_file import SingleFileSnapshotExtension  
	  
	class PdfSyrupyExtension(SingleFileSnapshotExtension):  
		_file_extension = "pdf"
	```

2. Юзаем класс:

	```python
	def test_render_pdf(snapshot):  
		pdf: bytes = ...
	  
		assert pdf == snapshot(extension_class=PdfSyrupyExtension)
	```