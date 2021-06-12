import pulsar

from pulsar.schema import AvroSchema
from example06_default_values_no_nulls.SchemaV2 import DefaultValuesNoNulls, DefaultValuesNoNullsUserdataSchema

client = pulsar.Client('pulsar://localhost:6650')

topicSchema = AvroSchema(DefaultValuesNoNulls)
print("Schema info is: " + topicSchema.schema_info().schema())

# Replace with your topic name. However, the namespace for the topic should have these schema compatibility settings:
# "schema_auto_update_compatibility_strategy" : "Full",
# "schema_compatibility_strategy" : "ALWAYS_COMPATIBLE",
# "is_allow_auto_update_schema" : true,
# "schema_validation_enforced" : true
producer = client.create_producer(topic='persistent://climate/field-service/default-values-nested-no-nulls', schema=topicSchema)
event = DefaultValuesNoNulls(
    name="Python producer",
    floatValue=1.23,
    DefaultValuesNoNullsUserdata=DefaultValuesNoNullsUserdataSchema())
producer.send(event)

client.close()

print("Successfully sent message")