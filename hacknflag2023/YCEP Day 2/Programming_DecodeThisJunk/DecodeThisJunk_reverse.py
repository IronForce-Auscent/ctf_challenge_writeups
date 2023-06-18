import base64
import secrets
import string
import gzip

def decode_ascii(to_ascii_decode):
    return to_ascii_decode.decode('ascii')

def decode_base64(to_base64_decode):
    return base64.b64decode(to_base64_decode)

def decompress_input(compressed_data):
    return gzip.decompress(compressed_data)

def generate_random_ascii_characters():
    random_ascii_characters = secrets.choice(string.ascii_letters)
    return random_ascii_characters

def encode_ascii (to_ascii_encode ):
    return to_ascii_encode.encode('ascii')

def decode_flag(compressed_input):
    asciidecoded_result = decompress_input(compressed_input)
    asciidecoded_result = decode_ascii(asciidecoded_result)

    for num_1to32 in range(31, -1, -1):
        asciidecoded_result = asciidecoded_result[:num_1to32] # Remove the last character

    base64encoded_result = encode_ascii(asciidecoded_result)
    asciiencoded_result = decode_base64(base64encoded_result)
    original_input = decode_ascii(asciiencoded_result)
    
    return original_input

def main():
    with open('output.txt', 'rb') as file:
        compressed_input = file.read()

    original_input = decode_flag(compressed_input)
    print(f"Original input: {original_input}")

if __name__ == "__main__":
    main()
