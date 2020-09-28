# Any variable associated to a parameter in a function call will be passed as
# a reference (its value can be modified by the function and it will have real-
# time effect.
def func(list_of_values: list, value_to_add) -> None:
    list_of_values.append(value_to_add)


if __name__ == "__main__":
    lst = [2, 3, 4, 12, 1]
    print(lst)
    func(lst, 5)
    print(lst)
    func(lst, 22)
    print(lst)
