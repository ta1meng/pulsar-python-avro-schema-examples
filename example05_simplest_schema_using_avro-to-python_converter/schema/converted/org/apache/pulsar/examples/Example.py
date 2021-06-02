# -*- coding: utf-8 -*-

""" avro python class for file: Example """

import json
from helpers import default_json_serialize, todict
from typing import Union


class Example(object):

    schema = """
    {
        "name": "Example",
        "type": "record",
        "namespace": "org.apache.pulsar.examples",
        "fields": [
            {
                "name": "name",
                "type": "string"
            }
        ]
    }
    """

    def __init__(self, obj: Union[str, dict, 'Example']) -> None:
        if isinstance(obj, str):
            obj = json.loads(obj)

        elif isinstance(obj, type(self)):
            obj = obj.__dict__

        elif not isinstance(obj, dict):
            raise TypeError(
                f"{type(obj)} is not in ('str', 'dict', 'Example')"
            )

        self.set_name(obj.get('name', None))

    def dict(self):
        return todict(self)

    def set_name(self, value: str) -> None:

        if isinstance(value, str):
            self.name = value
        else:
            raise TypeError("field 'name' should be type str")

    def get_name(self) -> str:

        return self.name

    def serialize(self) -> None:
        return json.dumps(self, default=default_json_serialize)
