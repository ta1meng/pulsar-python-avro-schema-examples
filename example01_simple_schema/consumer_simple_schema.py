import pulsar

from pulsar.schema import AvroSchema
from example01_simple_schema.SimpleSchema import Example

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe(
    topic='persistent://climate/sandbox/simple-schema',
    subscription_name='my-subscription',
    schema=AvroSchema(Example))
while True:
    msg = consumer.receive()
    exampleEvent = msg.value()
    print("Example event is %s"%exampleEvent)
    consumer.acknowledge(msg)
client.close()

