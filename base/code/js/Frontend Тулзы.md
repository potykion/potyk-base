#тулзы #frontend #js #dev-тулзы

# Frontend Тулзы

- [Storybook](https://storybook.js.org/) 
	- штука для документации компонентов / дизайн-системы
	- можно вывести все компоненты, которые есть в системе + из свойства
	- фреймворк-агностик
- https://github.com/typicode/json-server - топ-тул, когда нужна простая мок-круд-апишка: типа бека еще нет, а круд хочется
- https://github.com/fengyuanchen/compressorjs - топ либа 
- https://fengyuanchen.github.io/compressorjs/ - Одной строчкой я сжал картинку в 10 раз и это происходит на клиенте!
	```ts
	import Compressor from "compressorjs";
	
	const compressed = (
		await new Promise<File | Blob>(
			(success, error) =>
				new Compressor(file, {
					quality: 0.6,
					mimeType: "image/jpeg",
					success,
					error,
				})
		)
	) as File;
	```
	- *Альтернатива:* https://github.com/lovell/sharp  (+ svelte-обертка https://github.com/matyunya/svelte-image)
- https://nuxt.studio/ - ide для nuxt
- https://github.com/colinhacks/zod - поп-валидатор данных, типа pydantic для ts
- https://github.com/pyscript/pyscript - python в браузере (вместо js)
- https://github.com/marko-js/marko - html вместо фреймворков
- https://github.com/posva/mande - упрощение fetch
- https://github.com/vuejs/petite-vue - маленькая вьюшка