"""
python3 store.py
The Dugout
  1. Running
  2. Baseball
  3. Basketball
  4. Exit
Select the number of a department.

Attributes:
  - Name
  - Departments

Optional extra attributes:
  - Store hours
  - Store capacity
"""

from departments import Department

# Composition: a 'has-a' relationship


class Store:

    # self is the class itself (this)
    def __init__(self, name, departments):
      # __init__ initiate
        self.name = name
        self.departments = []

        for dep in departments:
            department = Department(dep)
            self.departments.append(department)

    def __str__(self):
      # __str__ string
        output = ''
        output += self.name + '\n'

        for index, department in enumerate(self.departments):
            output += str(index + 1) + '. ' + str(department) + '\n'

        # for department in self.departments:
        #     output += department + '\n'
        output += str(len(self.departments) + 1) + '. Exit'

        return output

        # return f'store name is {self.name}'

    def __repr__(self):
      # repr debugging
        return self


store = Store('the dugout', ['running', 'baseball', 'basketball'])

print(store)


selection = 0
while selection != len(store.departments) + 1:
    selection = input('select a number of a department: ')
    try:
        selection = int(selection)
        if selection >= 1 and selection < len(store.departments) + 1:
            print(f'the user selected: {selection}')
        else:
            print('choose from the given choices.')
    except ValueError:
        print('choose a number, not an empty string or a letter')

print('thank you for shopping with us today :)')
