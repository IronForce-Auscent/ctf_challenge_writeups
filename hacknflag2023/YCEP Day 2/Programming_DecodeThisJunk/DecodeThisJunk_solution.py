import base64
import secrets 
import string 
import gzip 
flag ="HNF23{REDACTED}"

def gen_random_char():
    return secrets.choice(string.ascii_letters)

def main(s6):
    s7 = s6.encode('ascii')
    s8 = base64.b64encode(s7)
    s9 = s8.decode('ascii')
    for i in range(32):
        s9 += gen_random_char()
    s9 = s9.encode('ascii')
    return gzip.compress(s9)

def save(ss):
    file = open('new_output.txt','wb')
    file.write(ss)
    file.close()

save(main(flag))