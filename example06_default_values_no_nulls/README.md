This example tests out default value support in Avro schemas.
* V0 of schema is a minimal schame.
* V1 of schema adds some fields with various default values.
* V2 of schema adds nested schema with a default value inside it.

V1 of schema ws tested and then V2 was tested. The current producer code uses V2.

Consumer code is left at schema V1 because it crashes at runtime due to default values.

Observations:
* Python producers support default values. Verified using debugger.
* Java producers support default values through the builder pattern. Verified using debugger.
* Python consumers crash when attempting to decode payloads with schemas that contain default values. Fastavro tries to read fields that have default values, but these fields are not in the payload.
* Java consumers support default values.

The Java applications are not included in this repository because it is for Python applications.