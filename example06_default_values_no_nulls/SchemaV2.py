from pulsar.schema import *

class DefaultValuesNoNullsUserdataSchema(Record):
    fieldId = String(required=True, default='defaultFieldId')
    acreage = Integer(required=True, default=-1)
    def from_dict(self, dictionary):
        return DefaultValuesNoNullsUserdataSchema(dictionary)

class DefaultValuesNoNulls(Record):
    name = String(required=True)
    description = String(required=True, default='Defaultdescription.')
    floatValue = Float(required=True, default=3.14159)
    intValue = Integer(required=True, default=9876)
    boolValue1 = Boolean(required=True, default=False)
    boolValue2 = Boolean(required=True, default=True)
    DefaultValuesNoNullsUserdata = DefaultValuesNoNullsUserdataSchema(required=True)
    _namespace = 'org.apache.pulsar.examples'

