#py 

# Профилирование памяти в Python

```python
import psutil  

def get_memory_usage_mb():  
	return psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
```

Просто вызываешь код выше, замеряя память и все: смотришь какие участки кода много жрут