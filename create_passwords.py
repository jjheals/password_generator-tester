import random as r
from sre_parse import SPECIAL_CHARS
import string as s


def check_validity(var, lst_choices):
    return var in lst_choices

#
# Function to generate a completely random password with the parameters given by the user
#
def generate_password():

    if alphanumeric == 'Y' and special_char == 'Y':
        # Had to use a raw string instead of s.printable because of the special characters " ' \ | ` many of which are not commonly available to be used in passwords
        #   and interfere with the output due to their values in python
        alphabet = f'{s.ascii_letters}{SPECIAL_CHARS}/0123456789'
    elif alphanumeric == 'N' and special_char == 'N':
        alphabet = s.ascii_letters
    elif alphanumeric == 'Y' and special_char == 'N':
        alphabet = f'{s.ascii_letters}0123456789'
    elif alphanumeric == 'N' and special_char == 'Y':
        alphabet = f'{s.ascii_letters}{SPECIAL_CHARS}/'

    new_password = ""

    i=0
    add_rand = int(r.randint(1,10))
    new_len = min_len + add_rand
    while i < new_len:
        new_password+=alphabet[r.randint(0,len(alphabet)-1)]
        i+=1

    if alphanumeric == 'Y':
        if not any(i.isdigit() for i in new_password):
            temp_list = []
            for char in new_password: temp_list.append(char)
            temp_list.insert(r.randint(0,len(temp_list)-1),str(r.randint(0,9)))
            new_password = ''.join(temp_list)
            
    if special_char == 'Y':
        c = 0
        for char in SPECIAL_CHARS:
            if char in new_password:
                return
            else: c += 1
        
        if c > 0:
            add_char = SPECIAL_CHARS[r.randint(0,len(SPECIAL_CHARS)-1)]
            temp_list = []
            temp_list.insert(r.randint(0,len(new_password)-1), add_char)
            new_password = ''.join(temp_list)

    return new_password


print("\n\nPassword creator:\n\nWhat would you like to do?\nA.) Create new password(s)\nB.) Test a current password\n")

mode = input()
mode = mode.upper()

while not check_validity(mode, ['A','B']):
    mode = input("Please choose A or B: ")
    mode = mode.upper()

#
# If user wants to create new password(s)
#
if mode == 'A':

    def get_parameters():

        # Get the minimum requried length
        min_len = input("\nWhat is the minimum required length? ")
        
        while True:
            try: 
                int(min_len)
                break
            except ValueError:
                min_len = input("Please enter an integer value: ")

        min_len = int(min_len)

        # Boolean are special characters allowed?
        special_char = input("Are special characters required? [Y/N]: ")
        special_char = special_char.upper()

        while not check_validity(special_char, ['Y','N']):
            special_char = input("Please choose Y or N: ")
            special_char = special_char.upper()

        # Boolean do you need numbers and letters?
        alphanumeric = input("Does the password(s) need to be alphanumeric? [Y/N]: ")
        alphanumeric = alphanumeric.upper()

        while not check_validity(alphanumeric, ['Y','N']):
            alphanumeric = input("Please choose Y or N: ")
            alphanumeric = alphanumeric.upper()

        return min_len, special_char, alphanumeric
    
    min_len, special_char, alphanumeric = get_parameters()

    sub_mode = input("\nDo you want to:\nA.) Create a new text file of possible passwords\nB.) Create a single password\n\n")
    sub_mode = sub_mode.upper()

    while not check_validity(sub_mode, ['A','B']):
        sub_mode = input("Please choose A or B: ")
        sub_mode = sub_mode.upper()

    # Create a text file of new passwords based on parameters
    if sub_mode == 'A':
        num_passwords = input("How many passwords do you want to generate? ")
        try:
            int(num_passwords)
        except ValueError:
            num_passwords = input("Please input an integer value: ")

        file_name = input("What do you want to name the file to save the passwords to [Omit extensions]? **THIS WILL OVERWRITE THE CURRENT CONTENTS OF THIS FILE IF IT EXISTS** : ")
        save_to = open(file_name + '.txt', 'w')

        i=1
        passwords=[]
        while i <= int(num_passwords):
            passwords.append(generate_password())
            i+=1
        for p in passwords:
            save_to.write(p + '\n')

        print(f"\nCreated {num_passwords} random passwords and saved to {file_name}.txt.\n\n")

    #Create a new single password based on parameters
    if sub_mode == 'B':
        print(f"\nYour new randomly generated password is: \n{generate_password()}\n\n")

#
# If user wants to test the strength of a current password 
#
if mode == 'B': 
    
    passwrd = input("\nInsert the password you want to test: ")
    rockyou = input("\nDo you want to test against the 'rockyou.txt' list of common passwords [Y/N]? (This will take much longer and will use many more resources!): ")
    rockyou = rockyou.upper()

    while not check_validity(rockyou, ['Y','N']):
        rockyou = input('Please enter Y or N: ')
        rockyou = rockyou.upper()


    # Keep track of the things that make the password more secure
    score = 0

    # Add to score based on length of password
    if len(passwrd) > 14: 
        score+=4
    elif len(passwrd) > 10:
        score+=3
    elif len(passwrd) > 7:
        score+=2
    elif len(passwrd) > 5:
        score+=1

    # Add to score based on if it has any numbers
    n=0
    for num in range(0,10):
        if str(num) in passwrd:
            n+=1
    if n != 0:
        score+=2
    
    # Add to score based on if it has any special characters
    s=0
    for c in (SPECIAL_CHARS + '/'):
        if c in passwrd:
            s+=1
    if s > 0:
        score+=2
    
    # Add to score based on if any capital AND lowercase letters
    cap = 0
    lwr = 0
    for char in passwrd:
        if char.isupper():
            cap+=1
        elif char.islower():
            lwr+=1
        else: continue
    if cap == 0:
        score-=1
    if lwr == 0:
        score-=1
    else: score+=2

    # Check against rockyou.txt (if applicable)
    if rockyou == 'Y':
        with open('rockyou.txt', errors='ignore') as file:
            rockyou_contents = file.read()
            if passwrd in rockyou_contents:
                score-=7
                print("\nThis password was found in 'rockyou.txt'!")
            else:
                score+=1
    
    if score >= 10:
        result = "'very strong'"
    elif score >= 7:
        result = "'decent'"
    elif score >= 5:
        result = "'poor'"
    else:
        result = "'extremely poor'"
    
    print(f'Score: {score}\n')
    print(f"Based on the length, appearance of numbers and special characters, and appearance of capital vs. lower letters, (and rockyou.txt comparison, if applicable) your password is {result}.")