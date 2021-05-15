#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#


from abc import abstractmethod
import json
import fastavro
import _pulsar
import io
import enum


class Schema(object):
    def __init__(self, record_cls, schema_type, schema_definition, schema_name):
        self._record_cls = record_cls
        self._schema_info = _pulsar.SchemaInfo(schema_type, schema_name,
                                               json.dumps(schema_definition, indent=True))

    @abstractmethod
    def encode(self, obj):
        pass

    @abstractmethod
    def decode(self, data):
        pass

    def schema_info(self):
        return self._schema_info

    def _validate_object_type(self, obj):
        if not isinstance(obj, self._record_cls):
            raise TypeError('Invalid record obj of type ' + str(type(obj))
                            + ' - expected type is ' + str(self._record_cls))


class BytesSchema(Schema):
    def __init__(self):
        super(BytesSchema, self).__init__(bytes, _pulsar.SchemaType.BYTES, None, 'BYTES')

    def encode(self, data):
        self._validate_object_type(data)
        return data

    def decode(self, data):
        return data


class StringSchema(Schema):
    def __init__(self):
        super(StringSchema, self).__init__(str, _pulsar.SchemaType.STRING, None, 'STRING')

    def encode(self, obj):
        self._validate_object_type(obj)
        return obj.encode('utf-8')

    def decode(self, data):
        return data.decode('utf-8')


class JsonSchema(Schema):

    def __init__(self, record_cls):
        super(JsonSchema, self).__init__(record_cls, _pulsar.SchemaType.JSON,
                                         record_cls.schema(), 'JSON')

    def _get_serialized_value(self, o):
        if isinstance(o, enum.Enum):
            return o.value
        else:
            return o.__dict__

    def encode(self, obj):
        self._validate_object_type(obj)
        return json.dumps(obj.__dict__, default=self._get_serialized_value, indent=True).encode('utf-8')

    def decode(self, data):
        return self._record_cls(**json.loads(data))


# From: https://stackoverflow.com/questions/1036409/recursively-convert-python-object-graph-to-dictionary
def todict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey))
                     for key, value in obj.__dict__.items()
                     if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj


class AvroSchema(Schema):
    def __init__(self, record_cls):
        super(AvroSchema, self).__init__(record_cls, _pulsar.SchemaType.AVRO,
                                         record_cls.schema(), 'AVRO')
        self._schema = record_cls.schema()

    def _get_serialized_value(self, x):
        if isinstance(x, enum.Enum):
            return x.name
        else:
            return x

    def encode(self, obj):
        self._validate_object_type(obj)
        buffer = io.BytesIO()
        m = todict(obj)
        #m = {k: self._get_serialized_value(v) for k, v in obj.__dict__.items()}
        fastavro.schemaless_writer(buffer, self._schema, m)
        return buffer.getvalue()

    def decode(self, data):
        buffer = io.BytesIO(data)
        d = fastavro.schemaless_reader(buffer, self._schema)
        return self._record_cls(**d)
