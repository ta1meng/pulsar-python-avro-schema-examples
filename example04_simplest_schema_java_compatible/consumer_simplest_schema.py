import pulsar

from pulsar.schema import AvroSchema
from example04_simplest_schema_java_compatible.SimpleSchema import Example

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe(
    topic='persistent://climate/field-service/simplest-schema',
    subscription_name='my-subscription',
    schema=AvroSchema(Example))
while True:
    msg = consumer.receive()
    exampleEvent = msg.value()
    print("Example event is %s"%exampleEvent)
    consumer.acknowledge(msg)
client.close()

