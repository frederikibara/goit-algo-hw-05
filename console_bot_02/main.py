from parser import parse_input
from handler import *

def main():
    """
Main contains the basic functionality of the bot assistant application.
It handles user interactions such as adding, modifying and displaying contacts.

Update 0.2 :
   - KeyError, ValueError, IndexError exeptions handling has been introduced
   - Updating the 'change' command to 'mod'
   - Added new del_contact function
   - Added new clear_all function 
   - Added new module 'emoji_bank.py'
   - Added documentation 

Commands:
    - hello : Just a greeting.
    - add <name> <phone> : Adds a new contact.
    - mod <name> <new_phone>: Updates an existing contact.
    - del <name> Deletes an existing contact.
    - phone <name>: Displays the contact's phone number.
    - all: Displays all contacts.
    - clear: Deletes all contacts. 
    - exit or close: Exits the program.
"""

    contacts = {}   
    print('Welcome to my assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        
        match command:
            case 'hello': 
                print('How can I help you?')
            case 'add': 
                print(add_contacts(args, contacts))
            case 'mod': 
                print(modify_contact(args, contacts))
            case 'del':
                print(del_contact(args, contacts))
            case 'phone':
                print(show_phone(args, contacts))            
            case 'all':
                print(show_all(contacts))           
            case 'clear':
                print(clear_all(contacts))
            case 'exit' | 'close': 
                print('Good bye!\n')
                break
            case _ :
                print('Invalid command')


if __name__ == '__main__':
    main()
