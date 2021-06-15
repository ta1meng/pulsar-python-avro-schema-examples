import pulsar

from pulsar.schema import AvroSchema
from example07_two_schema_versions_no_default_values.SchemaV0 import NoNestingNoDefaultValues

client = pulsar.Client('pulsar://localhost:6650')

topicSchema = AvroSchema(NoNestingNoDefaultValues)
print("Schema info is: " + topicSchema.schema_info().schema())

# Replace with your topic name. However, the namespace for the topic should have these schema compatibility settings:
# "schema_auto_update_compatibility_strategy" : "Full",
# "schema_compatibility_strategy" : "ALWAYS_COMPATIBLE",
# "is_allow_auto_update_schema" : true,
# "schema_validation_enforced" : true
producer = client.create_producer(topic='persistent://climate/field-service/two-schemas-no-defaults', schema=topicSchema)
producer.send(NoNestingNoDefaultValues(name="Python producer"))

client.close()

print("Successfully sent message")