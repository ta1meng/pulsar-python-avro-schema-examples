from pulsar.schema import *

class NoNestingNoDefaultValues(Record):
    name = String(required=True)
    _namespace = 'org.apache.pulsar.examples'

