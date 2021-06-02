from pulsar.schema import *

class Example(Record):
    name = String(required=True)
    _namespace = 'org.apache.pulsar.examples'

