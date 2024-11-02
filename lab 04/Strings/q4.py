'''9.4 Password Validation
Assume that you are writing a program for a local software house. It is a password checker program.
Two Python built-in functions you’ll need are ord(character) and chr(asciiNumber). ord(character)
takes a character and returns its ascii value. In opposite fashion, chr(asciiValue) takes an ascii
value and returns a character mapped on that ascii value. Following is ascii chart.
Fig:5 ASCII Code Table
7
That particular software house sets the criteria of password as: A password is valid if and only
if it has: * At least one lower case letter * At least one upper case letter * At least one special
characters from the above given image. * At least one digit
All other passwords are invalid. Use the functions described above to create this program.Summing
up the program requirements:
1. takes input as password from user
2. Apply the described tests
3. And prints whether the password is valid or invalid.'''

def pass_checker(password):
    upp_case_checker = any(char.isupper() for char in password)
    low_case_checker = any(char.islower() for char in password)
    digit_checker = any(char.isdigit() for char in password)

    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
    spec_char_checker = False
    for char in special_characters:
        if password.__contains__(char):
            spec_char_checker = True
            break

    if upp_case_checker and low_case_checker and digit_checker and spec_char_checker:
        print("Password in valid")
    else:
        print("!Invalid Password")
        
pass_checker("sajidL3$")