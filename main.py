import os
import time
import csv

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

    #check if the file exists
    file_exist = os.path.isfile('contacts.csv')

    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        if not file_exist:
            writer.writerow(['Name', 'Contact', 'Email'])

        writer.writerow([name, number, email])

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

    file_exist = os.path.isfile('contacts.csv')

    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)

        if not file_exist:
            print('No contacts found.')

        for row in reader:
            print(row)
    
    input('Press Enter to return to the main menu.')
        
def search_contact():
    clear_screen()
    print('Search Contact List\n')
    contact_name = input('Enter name to search: ')
    found = False

    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)    #skips the first line containing headings

        for row in reader:
            if row[0].lower() == contact_name.lower():
                print('Contact Found.')
                print('Name: ' +row[0])
                print('Number: ' +row[1])
                print('Email: ' +row[2])
                found = True
                break

    if not found:
        print('No contact found')

    input('Press Enter to return to the main menu.')


#this needs to be corrected
def update_contact():
    clear_screen()
    print('Update Contact List\n')
    contact_name = input('Enter the name of contact you want to update: ')
    found = False

    with open('contacts.csv','r') as file:
        reader = csv.reader(file)
        next(reader)    #skips the first line of headings

        for row in reader:
            if row[0].lower() == contact_name.lower():
                print('\nContact found.\n')
                print('Update the details.\n')
                new_name = input('Name: ')
                new_number = input('Number: ')
                new_email = input('Email: ')

                with open('contacts.csv','a', newline='') as file:
                    writer = csv.writer(file)
                    row[0] = new_name
                    row[1] = new_number
                    row[2] = new_email
                
                found = True
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