#mongo #go

# Go Mongo Фильтры

## `null` или пустой массив

```go
// tags == nil || len(tags) == 0
filter = bson.M{  
	"$or": bson.A{  
		bson.M{"tags": nil},  
		bson.M{"tags": bson.M{"$size": 0}},  
		// Опционально фильтр по отсутствию ключа
		// bson.M{"tags": bson.M{"$exists": false}}
	},  
}
```