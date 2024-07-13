from functools import wraps
from emoji_bank import get_emoji

def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return '*** Give me name and phone please ***'
        except KeyError:
            return '*** Invalid typing ***'
        except IndexError:
             return '*** Enter contact\'s name after command ***'
    return wrapper


@input_error
def add_contacts(args, contact):
    """ Adding name & phone number to contact base"""
    
    name, phone = args
    if name not in contact:
        contact[name] = phone
        return f'{get_emoji(0)}  contact added' 
    else:
        return 'Сontact already exists'
    
    
@input_error
def modify_contact(args, contact):
    """ Update contact information """
    
    name, new_phone = args
    if name in contact:
        contact[name] = new_phone
        return f'{get_emoji(1)} contact updated'
    else:
        return 'Contact not found'


@input_error
def del_contact(args, contact):
    """ Delete contact by name """
        
    name = args[0] 
    if name in contact:
        del contact[name]
        return f'{get_emoji(2)} contact was deleted'
    else:
        return 'Contact not found'


@input_error   
def show_phone(args, contact):
    """ Displays phone by contact name """
    
    name = args[0] 
    if name in contact:
        return f'{get_emoji(4)}  {contact[name]}'
    else:
        return 'Contact not found'
    

def show_all(contact): 
    """ Shows all added contacts """
    
    if not contact:
        return 'Contacts not found'
    else:
        contacts_info = ''
        for name, phone in contact.items(): 
             contacts_info += f'{name} {get_emoji(4)}  {phone}\n'
    return contacts_info


def clear_all(contact): 
    """ Delete all contacts """
    
    if not contact:
        return 'Contacts not found'
    else:
        contact.clear()
    return f'ALL contacts are DELETED {get_emoji(3)}'