from pulsar.schema import *

class DefaultValuesNoNullss(Record):
    name = String(required=True)
    _namespace = 'org.apache.pulsar.examples'

