import base64


encryped_code = "/_],1'57)&]X>Y?9"
xor_key = "iliketoxor"
reversed_xor_code = "F34GTSZOFT44W2ZM"
print(reversed_xor_code[::-1])
reversed_reversed_xor_code = "MZ2W44TFOZSTG43F"

print(base64.b32decode(reversed_reversed_xor_code.encode())).decode()