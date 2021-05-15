from pulsar.schema import *

class UserdataSchema(Record):
    fieldId = String(required=True, doc='IDofafieldasknowntosomefieldservice')
    action = String(required=False)
    def from_dict(self, dictionary):
        return UserdataSchema(dictionary)

class FieldLocationNested(Record):
    latitude = Float(required=True, doc='Latitude')
    longitude = Float(required=True, doc='Longitude')
    Userdata = UserdataSchema(required=True)
    _namespace = 'org.apache.pulsar.examples'
    _doc = 'Schemaforafieldlocation'