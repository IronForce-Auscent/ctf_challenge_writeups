import base64
import secrets 
import string 
import gzip 

REDACTED = "test_flag"
flag ="HNF23{REDACTED}"

def encode_ascii(to_ascii_encode):
    return to_ascii_encode.encode('ascii')
def compress_input(file_to_compress):
    return gzip.compress(file_to_compress)
def decode_ascii(to_ascii_decode):
    return to_ascii_decode.decode('ascii')
def encode_base64(to_base64_encode):
    return base64.b64encode(to_base64_encode)
def generate_random_ascii_characters():
    # evaluated_code ="ins + 2 - 2 + 32 + 64 + 128 + 256"
    random_ascii_characters = secrets.choice(string.ascii_letters)
    # eval (evaluated_code )
    # return evaluated_code, random_ascii_characters - ORIGINAL RETURN FUNC
    return random_ascii_characters
def encode_flag(asciiencode_input):
    asciiencoded_result = encode_ascii(asciiencode_input)
    base64encoded_result = encode_base64(asciiencoded_result)
    asciidecoded_result = decode_ascii(base64encoded_result)
    for num_1to32 in range(32):
        asciidecoded_result += generate_random_ascii_characters()
    asciidecoded_result = encode_ascii(asciidecoded_result)
    return compress_input(asciidecoded_result)
def main(writing_to_file):
    output_file_to_write_to = open('test_output.txt','wb')
    output_file_to_write_to.write(writing_to_file)
    output_file_to_write_to.close()
main(encode_flag(flag))
