import base64
import sys
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byte_data = bytes.fromhex(hex_string)
print(byte_data)
base64_encoded = base64.b64encode(byte_data)
print(base64_encoded.decode())
print(sys.maxsize)
X=12345687946545646495256261646415614564614649879845649846541
print(X)
print(sys.getsizeof(X))