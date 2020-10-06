class Contact:
    """Example of a class which has a variable editable by its instances."""
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Color:
    """Use the property() call to create a class property."""
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


class Person:
    """Try using the @property decorator instead."""
    def __init__(self, age: int, name: str):
        self.age = age
        self._name = name

    # The getter is always first, thus is used to declare the property. Name of
    # the getter is the same as the name of the property.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


if __name__ == "__main__":
    # Class variables can be modified from object-level calls.
    contact = Contact("John", "john@example.com")
    contact.all_contacts.append(64)
    print(contact.all_contacts)

    # Class properties for getters and setters.
    color = Color('#ffffff', 'black')
    print(color.name)
    color.name = 'white'

    # Class which uses the property decorator
    person = Person(age=25, name='John')
    print(person.name)
