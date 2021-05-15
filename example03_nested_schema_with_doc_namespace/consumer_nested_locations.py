import pulsar

from pulsar.schema import AvroSchema
from example03_nested_schema_with_doc_namespace.FieldLocationNested import FieldLocationNested

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe(
    topic='persistent://climate/field-service/nested-field-locations',
    subscription_name='my-subscription',
    schema=AvroSchema(FieldLocationNested))
while True:
    msg = consumer.receive()
    locationEvent = msg.value()
    print("Event is: ", locationEvent)
    print("Userdata is: ", locationEvent.Userdata)
    # print(locationEvent.latitude)
    # print(locationEvent.longitude)
    # print(locationEvent.Userdata.fieldId)
    # print(locationEvent.Userdata.action)
    consumer.acknowledge(msg)
client.close()

