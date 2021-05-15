# Broken out of the box. Needed the fixes in schema_fixes to make this example work.
# See README in this directory, as well as the top level README for details.
from pulsar.schema import *

# Copied from https://pulsar.apache.org/docs/fr/client-libraries-python/#complex-types
class MySubRecord(Record):
    x = Integer()
    y = Long()
    z = String()

class Example(Record):
    a = String()
    sub = MySubRecord()

