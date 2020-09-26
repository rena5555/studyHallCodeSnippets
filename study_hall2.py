import numpy as np
import pandas as pd

def my_func(lst):
    """Adds a 5 to the list

    Args:
        lst ([any]): random list

    Returns:
        [any]: a copy
    """
    lst_copy = lst.copy()

    lst_copy.append(5)

    return lst_copy

my_random_list = my_func([1])

print(round(np.log(10) - np.log(2), 2))

## Question 2

class Person:
    def __init__(self, name, coworker=None, age=None):
        self.name = name
        self._age = age
        self.coworker = coworker

        if self._age >= 13 and self._age <= 19:
            self.is_teen = True
        else:
            self.is_teen = False

    def __str__(self):
        return f'Name: {self.name} \nAge: {self._age}'

    def __add__(self, other_person):
        if isinstance(other_person, int):
            self._age += other_person
            return self

        else:
            return Person(self.name + ' and ' + other_person.name, None, self._age + other_person._age)

    def __eq__(self, other):
        return self.name == other.name and self._age == other._age and self.coworker == other.coworker

    def is_teen(self):
        if self._age >= 13 and self._age <= 19:
            return True
        else:
            return False

    def for_display(self):
        if self.is_teen():
            print(f'{self.name} is a teen.')
        else:
            print(f'{self.name} is not a teen')

    def happy_birthday(self):
        self._age += 1

        if self._age >= 13 and self._age <= 19:
            self.is_teen = True
        else:
            self.is_teen = False

lance = Person('Lance', None, 37)
lance_evil_twin = Person('Lance', None, 36)
tovio = Person('Tovio', None, 35)
lance.happy_birthday()
print(lance._age)
print(lance)
str_lance = str(lance)
print(str_lance)
print(lance == lance_evil_twin)

## Question 3

def __init__(self, name, location, size=0):
        self.name = name
        self.location = location
        self.size = size
        self.questions_asked = []

## Pandas

prices = pd.Series([1,1,2,3,5],
                   index=['apple',
                          'pear',
                          'banana',
                          'mango',
                          'jackfruit'])

inventory = pd.Series([10, 50, 41, 22],
                      index=['pear', 'banana', 'mango', 'apple'])

discount_prices = prices * .75

produce = pd.DataFrame({'price': prices,
                        'discount_price': discount_prices,
                        'inventory': inventory})

produce.loc[:,'discount_price'] = produce.loc[:,'discount_price'] * .5

produce.loc[produce.price>=3, 'price'] = 2.50

print(produce)
# print(produce.head())


def elements_twice_min(arr):
    """
    Return all elements of array arr that are greater than or equal to 2 times
    the minimum element of arr.
    Parameters
    ----------
    arr: numpy array (n, m)
    Returns
    -------
    numpy Array, a vector of size between: 0 and (n * m) - 1
    """
    return arr[arr >= (np.min(arr) * 2)]

arr = np.array([[1, 1, 1, 1, 3],
                [3, 4, 2, 2, 2]])

print(elements_twice_min(arr))
