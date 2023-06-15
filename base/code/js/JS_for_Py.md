#js #py 

# JS для Python разраба

## `itertools.groupby`

```js
/**
* @example
* // returns {"Завтрак": [{title: "Бутер", type: "Завтрак"}], "Ужин": [{title: "Мясо", type: "Ужин"}]}
* groupBy([{title: "Бутер", type: "Завтрак"}, {title: "Мясо", type: "Ужин"}], "type")
*/
const groupBy = (arr, key) => arr.reduce((acc, item) => ({...acc, [item[key]]: [...acc[item[key]] || [], item]}), {});
```

## `zip`

```js
/**
* @example
* // returns [[1,3], [2, 4]]
* zip([1, 2], [3, 4])
*/
const zip = (arr1, arr2) =>  arr1.map((item, i) => [item, arr2[i]]);
```

## `range`

```js
/**
* https://stackoverflow.com/a/10050831/5500609
*
* @example
* // returns [0, 1, 2, 3]
* range(4)
*/
const range = (len) => [...Array(len).keys()];
```