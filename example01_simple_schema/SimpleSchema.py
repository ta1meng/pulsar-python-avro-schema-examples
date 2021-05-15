from pulsar.schema import *

# Based on https://pulsar.apache.org/docs/fr/client-libraries-python/#simple-definition
class Example(Record):
    a = String()
    b = Integer()
