import pulsar

from pulsar.schema import AvroSchema
from example07_two_schema_versions_no_default_values.SchemaV1 import NoNestingNoDefaultValues

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe(
    topic='persistent://climate/field-service/two-schemas-no-defaults',
    subscription_name='my-subscription',
    schema=AvroSchema(NoNestingNoDefaultValues))
while True:
    msg = consumer.receive()
    exampleEvent = msg.value()
    print("Example event is %s"%exampleEvent)
    consumer.acknowledge(msg)
client.close()

