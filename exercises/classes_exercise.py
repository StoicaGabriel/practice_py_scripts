class Dog:
    species = 'Canis Familiaris'

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


class Terrier(Dog):
    # Method override in case text changes in parent class.
    def speak(self, sound='Arf'):
        # super() can act weird in bigger hierarchy.
        return super().speak(sound)


# Same thing applies to those two following classes.
class Bulldog(Dog):
    def speak(self, sound='Bow Wow'):
        return super().speak(sound)


class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return super().speak(sound)


jordas = Terrier(name='Jordas', age=8)
miles = GoldenRetriever(name='Miles', age=6)
jayjay = Bulldog(name='JayJay', age=3)

print(jordas.name, jordas.age)
print(miles.name, miles.age)

print(jordas.species)

print(jordas, '\n', miles)

print(miles.speak(), '\n', jordas.speak(), '\n', jayjay.speak())


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        # Using ':,' after a numeric variable does a separation such as 1000 -> 1,000
        return f"The {self.color} car has {self.mileage:,} miles."


r_car = Car(color='blue', mileage=20_000)
b_car = Car(color='red', mileage=30_000)

print(r_car, '\n', b_car)


# Dunder methods experiments
class Sequence:
    def __len__(self):
        pass

    def __getitem__(self, item):
        return item


sequence = Sequence()
print(len(sequence))
