import pulsar

from pulsar.schema import AvroSchema
from example02_nested_schema.NestedSchema import Example

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe(
    topic='persistent://climate/sandbox/nested-schema',
    subscription_name='my-subscription',
    schema=AvroSchema(Example))
while True:
    msg = consumer.receive()
    exampleEvent = msg.value()
    print("Event is: %s"%exampleEvent)
    print("Subrecord is: %s"%exampleEvent.sub)
    consumer.acknowledge(msg)
client.close()

