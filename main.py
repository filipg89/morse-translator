logo = r'''___  ___                      _____                   _       _             
|  \/  |                     |_   _|                 | |     | |            
| .  . | ___  _ __ ___  ___    | |_ __ __ _ _ __  ___| | __ _| |_ ___  _ __ 
| |\/| |/ _ \| '__/ __|/ _ \   | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
| |  | | (_) | |  \__ \  __/   | | | | (_| | | | \__ \ | (_| | || (_) | |   
\_|  |_/\___/|_|  |___/\___|   \_/_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|   

                                                                            '''

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', ':', ';', '?', "'",
            '-', '(', ')', '"', ' ', '!', '/', '&', '=', ';', '+', '_', '$', '@']
MORSE = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
         '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--',
         '....-', '.....', '-....', '--...', '---..', '----.', '-----', '.-.-.-', '--..--', '---...', '-.-.-.',
         '..--..', '.----.', '-....-', '-.--.', '-.--.-', '.-..-.', '.......', '-.-.--', '-..-.', '.-...', '-...-',
         '-.-.-.', '.-.-.', '..--.-', '...-..-', '.--.-.']

print(logo)
again = True
while again:
    language = input('Choose an option:\n1 - Translate to Morse Code\n2 - Translate from Morse Code\n')
    response = ""
    while language != "1" and language != "2":
        language = input("You have to enter either 1 or 2 in order to continue\n")
    if language == "1":
        user_input = input("Enter your phrase in Alphabet:\n").upper()
        for letter in user_input:
            if letter in ALPHABET:
                morse_letter = MORSE[ALPHABET.index(letter)]
                response += morse_letter + " "
            else:
                response += f'"Symbol {letter} doesnt have a Morse equivalent"'
        print(f"Your input converted to Morse code is:\n{response}")
    elif language == "2":
        user_input = input("Enter your phrase in Morse:\n").upper()
        for letter in user_input.split(' '):
            if letter in MORSE:
                alphabet_letter = ALPHABET[MORSE.index(letter)]
                response += alphabet_letter
            elif letter == "":
                pass
            else:
                response += f' "{letter}" not recognized as Morse symbol '
        print(f"Your input converted to Alphabet is:\n{response.lower()}")
    another = input("Do you want to try again? yes/no\n").lower()
    if another == "no":
        again = False
        print("-----------------------------------------------------------")
        print("Thank you for using Morse translator tool!")
        print("Have a good day!")
