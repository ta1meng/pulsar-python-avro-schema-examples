import pulsar

from pulsar.schema import AvroSchema
from example06_default_values_no_nulls.SchemaV1 import DefaultValuesNoNulls

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe(
    topic='persistent://climate/field-service/default-values-nested-no-nulls',
    subscription_name='my-subscription',
    schema=AvroSchema(DefaultValuesNoNulls))
while True:
    msg = consumer.receive()
    exampleEvent = msg.value()
    print("Example event is %s"%exampleEvent)
    consumer.acknowledge(msg)
client.close()

