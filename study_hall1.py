# Question 1
class Person:
    def __init__(self, name, coworker=None, age=None):
        self.name = name
        self.age = age
        self.coworker = coworker

    def is_teen(self):
        if self.age >= 13 and self.age <= 19:
            return True
        else:
            return False

    def for_display(self):
        if self.is_teen():
            print(f'{self.name} is a teen.')
        else:
            print(f'{self.name} is not a teen')

tovio = Person('Tovio')
lance = Person('Lance', tovio, 37)

print("Lance's age: ", lance.age)
print(lance.coworker.is_teen())
print(tovio.coworker)
print(lance.for_display())

## Question 2

import pandas as pd
prices = pd.Series([1,1,2,3,5],
              index=['apple', 'pear', 'banana', 'mango', 'jackfruit'])

inventory = pd.Series([10, 50, 41, 22],
              index=['pear', 'banana', 'mango', 'apple'])


one_ind = inventory.iloc[1::2]
two_less = prices[prices < prices.mean()]
three_onhand = (prices * inventory).loc['mango']

## Question 3

import numpy as np

def elements_greater_than_mean(arr):
    arr_ = np.array(arr)
    '''
    Return a new array with the elements of the array
    arr that are greater than its mean.
    Parameters:
    -----------
    arr: np.array([])
        A numerical array of an unknown dimension
    Returns:
    --------
    np.array([])
        A boolean array in the same dimensions of the original array, with
        values of True where the value is greater than the mean of all values
        in the array, and False where the value is equal to or less than the mean
    '''
    m = np.mean(arr)
    # print(m)
    # print(arr_ <= m)
    return arr[arr_ <= m]

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 5])
print(elements_greater_than_mean(arr))
