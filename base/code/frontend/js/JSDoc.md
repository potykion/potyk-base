#js 

# JSDoc

- [JSDoc](https://jsdoc.app/index.html) - спека js-док-комментов

## Чем хороша

- Можно [типизировать без TypeScript](js-typing.md)
- Можно описывать док-тесты:

```js
/**
* @example
* // returns [0, 1, 2, 3]
* range(4)
*/
const range = (len) => [...Array(len).keys()];
```


