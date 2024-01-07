import serde_timedelta
from serde import serde
from serde.json import to_json, from_json
from datetime import timedelta

serde_timedelta.init()


@serde
class Foo:
    a: timedelta


f = Foo(timedelta(hours=10))
json = to_json(f)
print(json)
print(from_json(Foo, json))
