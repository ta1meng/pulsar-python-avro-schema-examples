from pulsar.schema import *

class NoNestingNoDefaultValues(Record):
    name = String(required=True)
    description = String(required=True)
    floatValue = Float(required=True)
    intValue = Integer(required=True)
    boolValue1 = Boolean(required=True)
    boolValue2 = Boolean(required=True)
    _namespace = 'org.apache.pulsar.examples'

