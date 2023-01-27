# Ethereum Key Generator

This script is used to generate a random Ethereum private and public key pair, and then checks if the address of the public key matches a specified prefix and suffix. It can also be configured to save the private key to a file and to continue generating key pairs after a match is found.

## Required Libraries
- secrets
- csv
- os
- eth_keys (can be installed using pip)

## Configuration
You can configure the script by editing the following variables:
- PRINT_EVERY: How often the script will display a message with the number of checks that have been made so far. Set to a high number if you don't want to see those messages.
- PREFIX: The prefix that the public address should match (e.g. "0x1234").
- SUFFIX: The suffix that the public address should match (e.g. "abcd").
- LOOP: When set to true, the program will not stop when a match is found. Instead it will keep generating more addresses.
- SAVE: When set to true, the program will save your keys to a file in the directory specified in the "SAVE_TO" variable.
- SAVE_TO: The directory to save your private key files to.

## How to Use
1. Make sure you have the required libraries installed.
2. Configure the script to your liking by editing the variables as described above.
3. Run the script using Python.
4. Wait for the script to find a match or reach the maximum number of checks you specified.
5. If "SAVE" is set to true, the private key will be saved to the specified directory.

## Note
The script uses the "secrets" library to generate a private key, which is cryptographically secure. However, please keep in mind that this script is provided as-is and its integrity cannot be guaranteed. Use at your own risk.

Also, The more characters you want to match, the longer this script will take. It will take 16^X guesses for every X characters. You can do the math by yourself.
