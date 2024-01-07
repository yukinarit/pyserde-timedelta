[pyserde](https://github.com/yukinarit/pyserde) extension for `datetime.timedelta`.

```python
import serde_timedelta
from serde import serde
from serde.json import to_json, from_json
from datetime import timedelta

# Initialize serde_timedelta extension.
serde_timedelta.init()


@serde
class Foo:
    a: timedelta


f = Foo(timedelta(hours=10))
json = to_json(f)
print(json)                  # Prints {"a":"PT10H"}
print(from_json(Foo, json))  # Prints Foo(a=datetime.timedelta(seconds=36000))
```
