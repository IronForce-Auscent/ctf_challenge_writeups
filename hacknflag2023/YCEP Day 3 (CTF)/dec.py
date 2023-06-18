import base64
import gzip

data = open("output.txt", "rb").read()
s = gzip.decompress(data)
s = s.decode("ascii")
s = s[:-32]
s = s.encode("ascii")
s = base64.b64decode(s)
s = s.decode("ascii")
print(s)

# oneline
print(__import__("base64").b64decode(__import__("gzip").decompress(open("output.txt", "rb").read()).decode("ascii")[:-32].encode("ascii")).decode("ascii"))