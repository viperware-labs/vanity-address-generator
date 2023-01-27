# Built in python libraries
import secrets
import csv
import os
# pip install eth_keys
import eth_keys

found = False
checks = 0

# How often the "1000 checks so far" message should be displayed.
# Set to a large number if you don't want to see those messages.
PRINT_EVERY = 1000

# NOTE: The more characters you want to match, the longer this
# script will take. It will take 16^X guesses for every X characters. 
# You do the math.

# The prefix that the public address should match (0x1234)
PREFIX = '0x123'

# The suffix that the public address should match. (abcd)
SUFFIX = ''

# When set to true, the program will not stop when a match is found.
# Instead it will keep generating more addresses.
LOOP = False

# When set to true, the program will save your keys to a file
# in the directory below if a match is found.
SAVE = False

# Directory to save your private key files to.
SAVE_TO = 'keys'

def generate_key_pair():
    # Generate a private key using the secrets module
    private_key = secrets.randbits(256)

    # Convert the private key to bytes
    private_key_bytes = private_key.to_bytes(32, byteorder='big')

    # Create an instance of the PrivateKey class from the private key bytes
    private_key_obj = eth_keys.keys.PrivateKey(private_key_bytes)

    # Derive the public key from the private key
    public_key = private_key_obj.public_key

    # Get the public key address
    address = public_key.to_address()

    return address, private_key_obj

while not found:
    address, private_key = generate_key_pair()

    if address.startswith(PREFIX) and address.endswith(SUFFIX):
        print("MATCH FOUND! Found in {} checks".format(checks))
        print("Address:", address)
        print("Private Key:", private_key)

        checks = 0
        if not LOOP:
            found = True
        if SAVE:
            try:
                if not os.path.exists(SAVE_TO):
                    os.mkdir(SAVE_TO)
                with open('{}/{}.csv'.format(SAVE_TO, address), 'w', newline='') as csvfile:
                    fieldnames = ['private_key']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow({'private_key': private_key})
            except:
                print("Invalid path!")
    else:
        checks += 1
        if checks % PRINT_EVERY == 0:
            print("{} checks so far".format(checks))