class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        if len(phone_number) == 10:
            if phone_number.isdigit():
                return True
            else:
                return False
        else:
            return False

class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):

        if Contact.validate_phone_number(phone_number):

            new_contact = Contact(name, phone_number)

            cls.all_contacts.append(new_contact)

        else:
            raise ValueError("Error: phone number must contain exactly 10 digits")


print(ContactList.all_contacts)  # []

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone)




