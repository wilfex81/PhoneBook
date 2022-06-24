import json


'''This class is used to create a phone book'''
class PhoneBook():
    def __init__(self): 
        self.phoneBook = {}

    
    def add(self):
        '''This function adds a name and number to the phone book'''
        name = input("Enter name to be saved: ")
        number = input("Enter number for {}: " .format(name))
        self.phoneBook[name] = number
        return self.phoneBook
    
    def save(self, filename):
        '''This function saves the phone book to a file'''
        with open("contacts.json", "w") as f:
            json.dump(self.phoneBook, f, indent=4)
        
        return "Saved"

    
    def lookup(self, name):
        '''This function looks up a name in the phone book'''
        if name in self.phoneBook:
            return self.phoneBook[name]
        else:
            return "Not found"

    def remove(self, name):
        '''This function removes a name from the phone book'''
        if name in self.phoneBook:
            del self.phoneBook[name]
        else:
            return "Not found"
    
    def update(self, name, number):
        '''This function updates a name in the phone book'''
        if name in self.phoneBook:
            self.phoneBook[name]= number
        else:
            return "Not found"

    def print(self):
        '''This function prints the phone book as a dictionary'''
        for name in self.phoneBook:
            print(name, self.phoneBook[name])


if __name__ == "__main__":
    phoneBook = PhoneBook()
    while True:
        print("""
        1. Add
        2. Remove
        3. Update
        4. Lookup
        5. Print
        6. Exit
        """)
        choice = input("Enter choice: ")
        if choice == "1":
            phoneBook.add()
            phoneBook.save("phoneBook.json")
        elif choice == "2":
            name = input("Enter name: ")
            phoneBook.remove(name)
        elif choice == "3":
            name = input("Enter name: ")
            number = input("Enter number: ")
            phoneBook.update(name, number)
        elif choice == "4":
            name = input("Enter name: ")
            print(phoneBook.lookup(name))
        elif choice == "5":
            phoneBook.print()
        elif choice == "6":
            break
        else:
            print("Invalid choice")
    
    

