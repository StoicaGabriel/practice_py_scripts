class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)


if __name__ == "__main__":
    # Class variables can be modified from object-level calls.
    contact = Contact("John", "john@example.com")
    contact.all_contacts.append(64)
    print(contact.all_contacts)

    # Class properties for getters and setters.
    color = Color('#ffffff', 'black')
    print(color.name)
    color.name = 'white'
