class Staff:
    def __init__(self, name, age, qualification, contact, role):
        self.name = name
        self.age = age
        self.qualification = qualification
        self.contact = contact
        self.role = role
        self.training_history = []

def display_menu():
    print("\nStaff Management System")
    print("1. Add New Staff")
    print("2. Display Staff Information")
    print("3. Update Staff Information (Dean only)")
    print("4. Record Training History (Dean only)")
    print("5. Display Training History")
    print("6. Quit")

def add_staff(staff_list):
    print("\nEnter Staff Details:")
    name = input("Name: ")
    age = input("Age: ")
    qualification = input("Qualification: ")
    contact = input("Phone Number: ")
    role = input("Enter your role(Assistant Prof/Associate Prof/Dean): ")

    staff_member = Staff(name, age, qualification, contact, role)
    staff_list.append(staff_member)
    print("\nStaff added successfully!")

def display_staff(staff_list):
    print("\nStaff Information:")
    for staff_member in staff_list:
        print("\nName:", staff_member.name)
        print("Age:", staff_member.age)
        print("Qualification:", staff_member.qualification)
        print("Contact Information:", staff_member.contact)
        print("Role:", staff_member.role)
        print("-" * 30)

def update_staff(staff_list, role):
    if role != "Dean":
        print("\nOnly the Dean can update staff information.")
        return

    name_to_update = input("\nEnter the name of the staff member to update: ")

    for staff_member in staff_list:
        if staff_member.name == name_to_update:
            print("\nUpdate Staff Details:")
            staff_member.age = input("Age: ")
            staff_member.qualification = input("Qualification: ")
            staff_member.contact = input("Contact Information: ")
            print("\nStaff information updated successfully!")
            return

    print("\nStaff member not found.")

def record_training_history(staff_list, role):
    if role != "Dean":
        print("\nOnly the Dean can record training history.")
        return

    name_to_record = input("\nEnter the name of the staff member to record training history: ")

    for staff_member in staff_list:
        if staff_member.name == name_to_record:
            training_event = input("Enter training event: ")
            staff_member.training_history.append(training_event)
            print("\nTraining history recorded successfully!")
            return

    print("\nStaff member not found.")

def display_training_history(staff_list):
    name_to_display = input("\nEnter the name of the staff member to display training history: ")

    for staff_member in staff_list:
        if staff_member.name == name_to_display:
            print("\nTraining History for", staff_member.name)
            for event in staff_member.training_history:
                print("- ", event)
            return

    print("\nStaff member not found.")

def main():
    staff_list = []

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            add_staff(staff_list)
        elif choice == '2':
            display_staff(staff_list)
        elif choice == '3':
            update_staff(staff_list, "Dean")
        elif choice == '4':
            record_training_history(staff_list, "Dean")
        elif choice == '5':
            display_training_history(staff_list)
        elif choice == '6':
            print("\nExiting Staff Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option (1-6).")


main()
