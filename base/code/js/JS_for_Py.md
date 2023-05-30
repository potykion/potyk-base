#js #py 

# JS для Python разраба

## `itertools.groupby`

```js
const groupBy = (arr, key) => arr.reduce((acc, item) => ({...acc, [item[key]]: [...acc[item[key]] || [], item]}), {});
```

## `zip`

```js
const zip = (arr1, arr2) =>  arr1.map((item, i) => [item, arr2[i]]);
```
