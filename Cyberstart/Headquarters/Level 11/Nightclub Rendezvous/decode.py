with open(r"C:\Users\user\OneDrive\Desktop\Github Repositories (Local)\ctf_challenge_writeups\Cyberstart\Headquarters\Level 11\Nightclub Rendezvous\encoded_input.txt", "r") as file:
    f_contents = file.read()
encoded_input = []
for word in f_contents.split("\n"):
    encoded_input.append(int(word))

possible_strings = ""
for i in range(10):
    current_string = ""
    for word in encoded_input:
        word += i
        current_string += chr(word)
    current_string += "\n"
    possible_strings += current_string
    current_string = ""
print(possible_strings)