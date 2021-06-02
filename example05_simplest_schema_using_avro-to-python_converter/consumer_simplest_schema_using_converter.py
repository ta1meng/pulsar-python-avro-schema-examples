import pulsar

from pulsar.schema import AvroSchema
from experimental.example04_simplest_schema import Example

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe(
    topic='persistent://climate/field-service/simplest-schema',
    subscription_name='my-subscription',
    schema=AvroSchema(Example))
while True:
    msg = consumer.receive()
    exampleEvent = msg.value()
    print("Example event is %s"%exampleEvent)
    print(exampleEvent.get_name())
    consumer.acknowledge(msg)
client.close()

