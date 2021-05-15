import pulsar

from pulsar.schema import AvroSchema

from example03_nested_schema_with_doc_namespace.FieldLocationNested import FieldLocationNested, UserdataSchema

client = pulsar.Client('pulsar://localhost:6650')

topicSchema = AvroSchema(FieldLocationNested)
print("Schema info is: " + topicSchema.schema_info().schema())

# Replace with your topic name. However, the namespace for the topic should have these schema compatibility settings:
# "schema_auto_update_compatibility_strategy" : "AutoUpdateDisabled",
# "schema_compatibility_strategy" : "FORWARD_TRANSITIVE",
# "is_allow_auto_update_schema" : false,
# "schema_validation_enforced" : true
producer = client.create_producer(topic='persistent://climate/field-service/nested-field-locations', schema=topicSchema)
userdata=UserdataSchema(fieldId="Python", action="action")
fieldLocationNested = FieldLocationNested(latitude=1.0, longitude=2.0, Userdata=userdata)

producer.send(fieldLocationNested)

client.close()

print("\nSuccessfully sent message\n")
