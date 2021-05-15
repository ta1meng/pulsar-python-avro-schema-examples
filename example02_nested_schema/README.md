This example is broken out of the box.

The directory `schema_fixes` contains the changes needed to fix all the errors below.

The producer error trace against Python 2.7 is:

```
Traceback (most recent call last):
  File "/Users/tai.meng/dt/pulsar-python-avro-schema-examples/example02_nested_schema/producer_nested_schema.py", line 18, in <module>
    producer.send(Example(a="Sandbox", sub=MySubRecord(x=1,y=2,z="Does it work")))
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pulsar/__init__.py", line 852, in send
    deliver_at, deliver_after)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pulsar/__init__.py", line 935, in _build_msg
    data = self._schema.encode(content)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pulsar/schema/schema.py", line 112, in encode
    fastavro.schemaless_writer(buffer, self._schema, m)
  File "fastavro/_write.pyx", line 702, in fastavro._write.schemaless_writer
  File "fastavro/_write.pyx", line 376, in fastavro._write.write_data
  File "fastavro/_write.pyx", line 320, in fastavro._write.write_record
  File "fastavro/_write.pyx", line 374, in fastavro._write.write_data
  File "fastavro/_write.pyx", line 283, in fastavro._write.write_union
ValueError: <example02_nested_schema.NestedSchema.MySubRecord object at 0x118168350> (type <class 'example02_nested_schema.NestedSchema.MySubRecord'>) do not match ['null', {'fields': [{'type': ['null', 'int'], 'name': 'x'}, {'type': ['null', 'long'], 'name': 'y'}, {'type': ['null', 'string'], 'name': 'z'}], 'type': 'record', 'name': 'MySubRecord'}] on field sub
```

The producer error trace against Python 3.7 is:

```
Traceback (most recent call last):
File "/Users/tai.meng/dt/pulsar-python-avro-schema-examples/example02_nested_schema/producer_nested_schema.py", line 18, in <module>
producer.send(Example(a="Sandbox", sub=MySubRecord(x=1,y=2,z="Does it work")))
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pulsar/__init__.py", line 912, in send
deliver_at, deliver_after)
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pulsar/__init__.py", line 995, in _build_msg
data = self._schema.encode(content)
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pulsar/schema/schema.py", line 112, in encode
fastavro.schemaless_writer(buffer, self._schema, m)
File "fastavro/_write.pyx", line 660, in fastavro._write.schemaless_writer
File "fastavro/_write.pyx", line 341, in fastavro._write.write_data
File "fastavro/_write.pyx", line 288, in fastavro._write.write_record
File "fastavro/_write.pyx", line 339, in fastavro._write.write_data
File "fastavro/_write.pyx", line 251, in fastavro._write.write_union
ValueError: <example02_nested_schema.NestedSchema.MySubRecord object at 0x7ff970013e80> (type <class 'example02_nested_schema.NestedSchema.MySubRecord'>) do not match ['null', {'type': 'record', 'name': 'MySubRecord', 'fields': [{'name': 'x', 'type': ['null', 'int']}, {'name': 'y', 'type': ['null', 'long']}, {'name': 'z', 'type': ['null', 'string']}]}]
```

The consumer error trace aganst Python 2.7 is:

```
Traceback (most recent call last):
File "/Users/tai.meng/dt/pulsar-python-avro-schema-examples/example02_nested_schema/consumer_nested_schema.py", line 13, in <module>
exampleEvent = msg.value()
File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pulsar/__init__.py", line 177, in value
return self._schema.decode(self._message.data())
File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pulsar/schema/schema.py", line 118, in decode
return self._record_cls(**d)
File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pulsar/schema/definition.py", line 67, in __init__
self.__setattr__(k, kwargs[k])
File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pulsar/schema/definition.py", line 98, in __setattr__
value = field.validate_type(key, value)
File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pulsar/schema/definition.py", line 116, in validate_type
type(val), name, self.__class__))
TypeError: Invalid type '<type 'dict'>' for sub-record field 'sub'. Expected: <class 'example02_nested_schema.NestedSchema.MySubRecord'>
```

The consumer error trace against Python 3.7 is:

```
Traceback (most recent call last):
File "/Users/tai.meng/dt/pulsar-python-avro-schema-examples/example02_nested_schema/consumer_nested_schema.py", line 13, in <module>
exampleEvent = msg.value()
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pulsar/__init__.py", line 177, in value
return self._schema.decode(self._message.data())
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pulsar/schema/schema.py", line 141, in decode
return self._record_cls(**d)
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pulsar/schema/definition.py", line 67, in __init__
self.__setattr__(k, kwargs[k])
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pulsar/schema/definition.py", line 125, in __setattr__
value = field.validate_type(key, value)
File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pulsar/schema/definition.py", line 143, in validate_type
type(val), name, self.__class__))
TypeError: Invalid type '<class 'dict'>' for sub-record field 'sub'. Expected: <class 'example02_nested_schema.NestedSchema.MySubRecord'>
```