'''File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .}
Using this example, the letter A would be assigned the symbol %, the letter a would be assigned
the number 9, the letter B would be assigned the symbol @, and so forth.
12
The program should open a specified text file, read its contents, and then use the dictionary to
write an encrypted version of the file’s contents to a second file. Each character in the second file
should contain the code for the corresponding character in the first file. Write a second program
that opens an encrypted file and displays its decrypted contents on the screen.'''

codes = {
    'A': '!', 'a': '1',
    'B': '@', 'b': '2',
    'C': '#', 'c': '3',
    'D': '$', 'd': '4',
    'E': '%', 'e': '5',
    'F': '^', 'f': '6',
    'G': '&', 'g': '7',
    'H': '*', 'h': '8',
    'I': '(', 'i': '9',
    'J': ')', 'j': '0',
    'K': '_', 'k': '-',
    'L': '+', 'l': '=',
    'M': '{', 'm': '}',
    'N': '[', 'n': ']',
    'O': ':', 'o': ';',
    'P': '"', 'p': "'",
    'Q': '<', 'q': '>',
    'R': ',', 'r': '.',
    'S': '?', 's': '/',
    'T': '~', 't': '`',
    'U': '|', 'u': '\\',
    'V': '&^', 'v': '^&$',
    'W': '!', 'w': '1',
    'X': '@', 'x': '2',
    'Y': '#', 'y': '3',
    'Z': '$', 'z': '4'
}

def encrypt_file(input_file, output_file):

    with open(input_file, 'r') as infile,open(output_file,'w') as outfile:
        for line in infile:
            encrptdata = ''.join(codes.get(char,char) for char in line)
            outfile.write(encrptdata)

    print(f"Encryption completed. Encrypted content written to '{output_file}'.")

def decrypt_file(input_file, output_file):

    reverse_codes = {value:key for key,value in codes.items()}

    with open(input_file,'r') as infile, open(output_file,'w') as outfile:
        for line in infile:
            decryptdata = ''.join(reverse_codes.get(char,char) for char in line)
            outfile.write(decryptdata)    

    print(f"Decryption completed. Decrypted content written to '{output_file}'.")

input_filename = "inputfile.txt"      
encrypted_file = "encrypt.txt"
decrypted_file = "decrypt.txt"

encrypt_file(input_filename, encrypted_file)
decrypt_file(encrypted_file, decrypted_file)