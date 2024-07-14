![tests](https://github.com/dertilo/nested-dataclass-serialization/actions/workflows/tests.yml/badge.svg)
[![pypi](https://img.shields.io/pypi/v/nested-dataclass-serialization.svg)](https://pypi.python.org/project/nested-dataclass-serialization)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![bear-ified](https://raw.githubusercontent.com/beartype/beartype-assets/main/badge/bear-ified.svg)](https://beartype.readthedocs.io)
[![Ruff-ified](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/dertilo/python-linters/blob/master/python_linters/ruff.toml)

# nested dataclass serialization
- lets you (de)serialize nested dataclasses from and to json
- uses custom json-encoder for recursive serialization
- uses `importlib` for deserialization (instantiation of the dataclass-objects)
### minimal example
```python

@dataclass
class Bar:
    x: str


@dataclass
class Foo:
    bars: list[Bar]

bar = Bar(x="test")
foo = Foo(bars=[bar, bar])

json_str = serialize_dataclass(foo)

# this json_str looks like this:
{
    "_target_": "test_dataclass_serialization.Foo",
    "_id_": "a22ddd36-<some-long-id-here>d2290929",
    "bars": [
        {
            "_target_": "test_dataclass_serialization.Bar",
            "_id_": "a22ddd36-<some-long-id-here>ebb0ab925b1bd977208e4",
            "x": "test",
        },
        {
            "_target_": "test_dataclass_serialization.Bar",
            "_id_": "a22ddd36-<some-long-id-here>ebb0ab925b1bd977208e4",
            "x": "test",
        },
    ],
}
# somewhere in a different python-process/container/server
des_foo = deserialize_dataclass(json_str) # getting back the dataclass-object
assert id(des_foo.bars[0]) == id(des_foo.bars[1]) # just to show that deserialization works
```

### similar libs
- [madman-bob](https://github.com/madman-bob/python-dataclasses-serialization): looks like you need to explicitly provide the python-class for deserialization: `JSONSerializer.deserialize(InventoryItem, {'name': 'Apple', 'unit_ ...`