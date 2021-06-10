import pulsar

from pulsar.schema import AvroSchema
from example04_simplest_schema_java_compatible.SimpleSchema import Example

client = pulsar.Client('pulsar://localhost:6650')

topicSchema = AvroSchema(Example)
print("Schema info is: " + topicSchema.schema_info().schema())

# Replace with your topic name. However, the namespace for the topic should have these schema compatibility settings:
# "schema_auto_update_compatibility_strategy" : "Full",
# "schema_compatibility_strategy" : "ALWAYS_COMPATIBLE",
# "is_allow_auto_update_schema" : true,
# "schema_validation_enforced" : true
producer = client.create_producer(topic='persistent://climate/field-service/simplest-schema', schema=topicSchema)
producer.send(Example(name="Python producer"))

client.close()

print("Successfully sent message")