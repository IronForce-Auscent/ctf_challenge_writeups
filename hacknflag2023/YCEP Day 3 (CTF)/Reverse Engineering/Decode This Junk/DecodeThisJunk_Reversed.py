import base64
import gzip

data = open(r"C:\Users\user\OneDrive\Desktop\Github Repositories (Local)\ctf_challenge_writeups\hacknflag2023\YCEP Day 3 (CTF)\Reverse Engineering\Decode This Junk\output.txt", "rb").read()

# Step 1: Decode the data as gzip compressed
decompressed_data = gzip.decompress(data)

# Step 2: Decode the decompressed data as ASCII
decoded_data = decompressed_data.decode("ascii")

# Step 3: Remove the last 32 characters
trimmed_data = decoded_data[:-32]

# Step 4: Encode the trimmed data back to ASCII
encoded_data = trimmed_data.encode("ascii")

# Step 5: Decode the Base64 encoded data
decoded_base64_data = base64.b64decode(encoded_data)

# Step 6: Decode the decoded Base64 data as ASCII
final_data = decoded_base64_data.decode("ascii")

print(final_data)
