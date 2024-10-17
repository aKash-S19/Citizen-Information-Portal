import random
import string
import hashlib

def generate_initial_passwords():
    users = {}
    default_passwords = {}
    for roll_no in range(1, 63):
        default_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        default_passwords[roll_no] = default_password
        users[roll_no] = hash_password(default_password)
    return users, default_passwords

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def set_user_password(users, roll_no, new_password):
    users[roll_no] = hash_password(new_password)

def validate_login(users, roll_no, password):
    hashed_password = hash_password(password)
    return users.get(roll_no) == hashed_password

def add_land_regulation(land_regulations, regulation_name, details):
    land_regulations[regulation_name] = details

def add_government_scheme(government_schemes, scheme_name, details):
    government_schemes[scheme_name] = details

def add_admin_procedure(admin_procedures, procedure_name, details):
    admin_procedures[procedure_name] = details

def get_land_regulation(land_regulations, regulation_name):
    return land_regulations.get(regulation_name, "Regulation not found")

def get_government_scheme(government_schemes, scheme_name):
    return government_schemes.get(scheme_name, "Scheme not found")

def get_admin_procedure(admin_procedures, procedure_name):
    return admin_procedures.get(procedure_name, "Procedure not found")

def upload_document(documents, document_name, document_content):
    documents[document_name] = document_content

def get_document(documents, document_name):
    return documents.get(document_name, "Document not found")

def add_feedback(feedback_list, feedback):
    feedback_list.append(feedback)

def view_feedback(feedback_list):
    return feedback_list

def add_contact(contacts, department, official_name, contact_info):
    if department not in contacts:
        contacts[department] = {}
    contacts[department][official_name] = contact_info

def view_contacts(contacts):
    for dept in contacts:
        print(f"Department: {dept}")
        for name, info in contacts[dept].items():
            print(f" - {name}: {info}")

# Initializing data structures
users, default_passwords = generate_initial_passwords()
land_regulations = {}
government_schemes = {}
admin_procedures = {}
documents = {}
feedback_list = []
contacts = {}

# User sets their own password
roll_no = int(input("Welcome to the Citizen Information Portal! Please enter your roll number (1-62): "))
if roll_no in default_passwords:
    print(f"Your default password is: {default_passwords[roll_no]}")
    new_password = input("Please set your new password (minimum 8 characters): ")
    set_user_password(users, roll_no, new_password)
    print("Password changed successfully! You can now log in.")
else:
    print("Oops! That roll number is not valid. Please try again.")

# User login
roll_no = int(input("Please enter your roll number to log in: "))
password = input("Enter your password: ")
if validate_login(users, roll_no, password):
    print("Login successful! Welcome to the portal.")

    # Menu-driven interface for Citizen Information Portal
    while True:
        print("\nCitizen Information Portal Menu:")
        print("1. Access Information")
        print("2. Document Repository")
        print("3. Feedback Module")
        print("4. Resource Directory")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nInformation Module Menu:")
            print("1. Add Land Regulation")
            print("2. Add Government Scheme")
            print("3. Add Administrative Procedure")
            print("4. View Land Regulation")
            print("5. View Government Scheme")
            print("6. View Administrative Procedure")
            info_choice = input("What would you like to do? ")

            if info_choice == '1':
                regulation_name = input("Enter regulation name: ")
                details = input("Enter regulation details: ")
                add_land_regulation(land_regulations, regulation_name, details)
                print(f"Regulation '{regulation_name}' added successfully!")
            elif info_choice == '2':
                scheme_name = input("Enter scheme name: ")
                details = input("Enter scheme details: ")
                add_government_scheme(government_schemes, scheme_name, details)
                print(f"Scheme '{scheme_name}' added successfully!")
            elif info_choice == '3':
                procedure_name = input("Enter procedure name: ")
                details = input("Enter procedure details: ")
                add_admin_procedure(admin_procedures, procedure_name, details)
                print(f"Procedure '{procedure_name}' added successfully!")
            elif info_choice == '4':
                regulation_name = input("Enter regulation name to view: ")
                print(get_land_regulation(land_regulations, regulation_name))
            elif info_choice == '5':
                scheme_name = input("Enter scheme name to view: ")
                print(get_government_scheme(government_schemes, scheme_name))
            elif info_choice == '6':
                procedure_name = input("Enter procedure name to view: ")
                print(get_admin_procedure(admin_procedures, procedure_name))
            else:
                print("Invalid choice. Please try again.")

        elif choice == '2':
            print("\nDocument Repository Menu:")
            print("1. Add Document")
            print("2. View Documents")
            document_choice = input("What would you like to do? ")

            if document_choice == '1':
                document_name = input("Enter document name: ")
                content = input("Enter document content: ")
                upload_document(documents, document_name, content)
                print(f"Document '{document_name}' added successfully.")
            elif document_choice == '2':
                print("Documents in the repository:")
                for doc_name, doc_content in documents.items():
                    print(f"- {doc_name}: {doc_content}")
            else:
                print("Invalid choice. Please try again.")

        elif choice == '3':
            print("\nFeedback Module Menu:")
            print("1. Add Feedback")
            print("2. View Feedback")
            feedback_choice = input("What would you like to do? ")

            if feedback_choice == '1':
                feedback = input("Please enter your feedback: ")
                add_feedback(feedback_list, feedback)
                print("Thank you! Your feedback has been added.")
            elif feedback_choice == '2':
                print("Feedback received:")
                for fb in view_feedback(feedback_list):
                    print(f"- {fb}")
            else:
                print("Invalid choice. Please try again.")

        elif choice == '4':
            print("\nResource Directory Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            resource_choice = input("What would you like to do? ")

            if resource_choice == '1':
                department = input("Enter department name: ")
                official_name = input("Enter official name: ")
                contact_info = input("Enter contact information: ")
                add_contact(contacts, department, official_name, contact_info)
                print(f"Contact for {department} added successfully.")
            elif resource_choice == '2':
                print("Contact Information:")
                view_contacts(contacts)
            else:
                print("Invalid choice. Please try again.")

        elif choice == '5':
            print("Thank you for using the Citizen Information Portal! Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")
else:
    print("Oops! Invalid roll number or password. Please try again.")
