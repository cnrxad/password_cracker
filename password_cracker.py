import hashlib

found = 0
input_hash = input("Insert hashed password: ")
pass_doc = input("Insert dictionary: ")

try:
    pass_file = open(pass_doc, 'r')
except:
    print("Error:" + pass_doc + "was not found.")

for word in pass_file:
    encrypted_word = word.encode('utf-8')
    hashed_word = hashlib.md5(encrypted_word.strip())
    digest = hashed_word.hexdigest()

    if digest == input_hash:
        print("Password found! \n Password: " + word)
        found = 1
        break

if not found:
    print("Password not found in file: " + pass_doc)
