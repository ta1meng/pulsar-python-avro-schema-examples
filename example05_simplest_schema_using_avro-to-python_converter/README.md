This example demonstrates how to get avro-to-python converter working with Pulsar.

First install avro-to-python, according to https://pypi.org/project/avro-to-python/

Then convert:

/Library/Frameworks/Python.framework/Versions/3.7/bin/avro-to-python SimplestSchemaV1.avsc converted

Then copy Example.py into the root of this directory, and merge in the content of helpers.py.

Finally, hack schema.py in the Pulsar client library so this line:
```
return self._record_cls(**d)
```

becomes:

```
return self._record_cls(d)
```

After this, both consumer and producer worked. However...

As this would be a backwards compatibility breaking change, I see no chance that the Python community will accept this hack. Therefore, I see no possibility that avro-to-python converter will become compatible with Pulsar Python client library, even though avro-to-python outputs Python classes with the namespace "org.apache.pulsar.examples". How misleading!