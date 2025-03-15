import msgpack
import yaml

# Parse yaml
with open('proto.yml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Convert to messagepack
msgpack_data = msgpack.packb(yaml_data)

# Save binary
with open('proto.msgpack', 'wb') as file:
    file.write(msgpack_data)

# Decode binary
with open('proto.msgpack', 'rb') as file:
    loaded_msgpack = file.read()
    decoded_data = msgpack.unpackb(loaded_msgpack)
