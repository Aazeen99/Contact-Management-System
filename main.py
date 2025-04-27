import os
import time

#defining the contact list
contacts = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#defining all the functions
def add_contact():
    clear_screen()
    print('Add Contact: \n')
    name = input('Enter the name: ')
    number = input('Enter the number: ')
    email = input('Enter the email: ')

    contact = {
        'name' : name,
        'number' : number,
        'email' : email
    }

    contacts.append(contact)
    clear_screen()
    print(f'Contact \'{name}\' added successfully.')
    clear_screen()
    another_contact = input('Do you want to add another contact: (y/n) ').lower()

    if another_contact == 'y':
        add_contact()
    else:
        clear_screen()
        return

def view_contact():
    clear_screen()
    print('Contact List: \n')

    if not contacts:
        print('No contacts available.')
        time.sleep(2)
        clear_screen()
    else:
        for contact in contacts:
            print('Name: ' +contact['name'])
            print('Number: ' +contact['number'])
            print('email: ' +contact['email'])
            print('-' * 20)
    
    input('Press Enter to return to the main menu.')
        
def search_contact():
    clear_screen()
    print('Search Contact List\n')
    contact_name = input('Enter name to search: ')
    found = False

    for contact in contacts:
        if(contact['name'] == contact_name):
            print('\nName: ' +contact['name'])
            print('Number: ' +contact['number'])
            print('email: ' +contact['email'])
            found = True
            break

    if not found:
        print('No contact found')

    input('Press Enter to return to the main menu.')

def update_contact():
    clear_screen()
    print('Update Contact List\n')
    contact_name = input('Enter the name of contact you want to update: ')
    found = False

    for contact in contacts:
        if(contact['name'] == contact_name):
            found = True
            print(f'\nContact \'{contact_name}\' available.\n')

            #take input you need to update
            name = input('Enter updated name: ')
            number = input('Enter updated number: ')
            email = input('Enter updated email: ')

            contact['name'] = name
            contact['number'] = number
            contact['email'] = email

            break

    if not found:
        print('Contact not found.')

    input('Press Enter to return to the main menu.')

def delete_contact():
    clear_screen()
    print('Delete Contact\n')
    contact_name = input('Enter the name of contact you want to delete: ')    
    found = False

    for contact in contacts:
        if(contact['name'] == contact_name):
            contacts.remove(contact)
            found = True

            print('\nContact deleted successfully.\n')
            break

    if not found:
        print('Contact not found')
    
    input('Press Enter to return to the main menu.')

#Main body of the program
while True:
    clear_screen()
    print('Welcome to Contact Management System')
    print('\nSelect any of the following options:\n')
    print('''
        1 - Add Contact
        2 - View All Contacts
        3 - Search Contact
        4 - Update Contact
        5 - Delete Contact
        6 - Exit
        ''')

    selected_option = input('Enter option number: ')
    if(selected_option == '1'):
        add_contact()
    elif(selected_option == '2'):
        view_contact()
    elif(selected_option == '3'):
        search_contact()
    elif(selected_option == '4'):
        update_contact()
    elif(selected_option == '5'):
        delete_contact()
    elif(selected_option == '6'):
        print('Thank you for using Contact Management System. Goodbye!')
        break
    else:
        print('Enter a valid option (1-6).')