from pulsar.schema import *

class DefaultValuesNoNulls(Record):
    name = String(required=True)
    description = String(required=True, default='defaultDescription')
    floatValue = Float(required=True, default=3.14159)
    intValue = Integer(required=True, default=9876)
    boolValue1 = Boolean(required=True, default=False)
    boolValue2 = Boolean(required=True, default=True)
    _namespace = 'org.apache.pulsar.examples'

