I used a whitespace remover tool to remove all whitespaces from the *.avsc file.

Then I used a JSON escaper tool to escape the Avro schema, and created the *.schema file.

Finally, I uploaded the schema file to the topic:

```
bin/pulsar-admin schemas upload --filename FieldLocationNestedV0.python.schema "climate/field-service/nested-field-locations"
```

These are the changes made in `schema_fixes`:
* `doc` attribute in Avro schema is now supported
* `namespace` attribute in Avro schema is now supported
* `default` values are supported, though this example does not have default values specified
* `required` subrecord support added
* Fixed ordering bug that re-ordered fields in the generated schema definition, which makes the schema definition incompatible with existing schema on topic
