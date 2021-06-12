This example tests out Pulsar behavior when producer sends events using older schema, and when consumer receives events using a newer schema. No default values are set.

Specifically it seeks to find out if Pulsar assigns default values to required fields, when required fields are missing in the payload.

Both the Java and Python clients produce runtime exceptions, which is reasonable behavior, because when required fields are missing in the payload, the consumer should not be able to receive any messages with schema validation enforced. 