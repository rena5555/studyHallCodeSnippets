import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# class LinearPolynomial():
#     def __init__(self, m, b):
#         self.m = m
#         self.b = b

#     def __str__(self):
#         """
#         Returns a string representation of the LinearPolynomial instance
#         referenced by self.

#         Returns
#         -------
#         A string formatted like:

#         mx + b

#         Where m is self.m and b is self.b
#         """
#         pass

#     def __add__(self, other):
#         """
#         This function adds the other instance of LinearPolynomial
#         to the instance referenced by self.

#         Returns
#         -------
#         The sum of this instance of LinearPolynomial with another
#         instance of LinearPolynomial. This sum will not change either
#         of the instances reference by self or other. It returns the
#         sum as a new instance of LinearPolynomial, instantiated with
#         the newly calculated sums.
#         """

# # If m = 3, b = 5; then the __str__ method should return '3x + 5'

# fun1 = LinearPolynomial(4 + 3, 6 + 5)
# fun2 = LinearPolynomial(4, 6)

# print(fun1 + 5)

# # print(fun1.m, fun1.b)

# # fun1 + fun2 = new LinearPoly obj w/ m = 7; b = 11

# def elements_greater_than_mean(arr):
#     '''
#     Return a new array with the elements of the array
#     arr that are greater than its mean.

#     Parameters:
#     -----------
#     arr: np.array([])
#         A numerical array of an unknown dimension

#     Returns:
#     --------
#     np.array([])
#         An array which is a subset of the original array; use boolean indexing
#         to select only the values which are greater than the mean of all values
#         in the array.
#     '''
#     result = np.array([arr])
#     return result[result > result.mean()]

# Pandas

# grocery = pd.DataFrame({'category':['produce', 'produce', 'meat',
#                                             'meat', 'meat', 'cheese', 'cheese'],
#                         'item': ['celery', 'apple', 'ham', 'turkey',
#                                         'lamb', 'cheddar', 'brie'],
#                         'price':[.99, .49, 1.89, 4.34, 9.50, 6.25, 8.0],
#                         'inventory': [1, 2, 3, 4, 5, 6, 7]})

# grocery_grpd = grocery.groupby('category')

# for group, item in grocery_grpd:
#     print(group)
#     print(item)

temps = pd.DataFrame({
    'time': ['morning', 'noon', 'night',
             'morning', 'noon', 'night',
             'morning', 'noon', 'night',
             'morning', 'noon', 'night'],
    'city': ['Denver', 'Denver', 'Denver',
             'Austin', 'Austin', 'Austin',
             'NYC', 'NYC', 'NYC',
             'SFO', 'SFO', 'SFO'],
    'temp': [46, 57, 52,
             51, 68, 53,
             32, 32, 33,
             53, 71, 61]})

tmp_grpd_time = temps.groupby('time')

# for group, name in tmp_grpd_time:
#     print(group)
#     print(name)

tmp_grpd_city = temps.groupby('city')

# for group, name in tmp_grpd_city:
#     print(group)
#     print(name)

# print(tmp_grpd_city.filter(lambda x: x['temp'].mean() > 53))
# print(tmp_grpd_city.filter(lambda x: x['temp'].std() <= 6))
# print(tmp_grpd_time.filter(lambda x: x['temp'].std() <= 10))

# print(tmp_grpd_city.transform(lambda x: round((x - 32)*(5 / 9), 2)))
# temps['temp_C'] = tmp_grpd_city['temp'].transform(lambda x: round((x - 32)*(5 / 9), 2))

# temps.plot(kind='box')
# plt.show()




# left = pd.DataFrame({'name': ['dog', 'cat', 'fish', 'bird', 'dinosaur'],
#                              'A': ['A0', 'A1', 'A2', 'A3', 'A4'],
#                              'B': ['B0', 'B1', 'B2', 'B3', 'B3']})


# right = pd.DataFrame({'name': ['bird', 'fish', 'cat', 'dog', 'hog'],
#                               'C': ['C0', 'C1', 'C2', 'C3', 'C4'],
#                               'D': ['D0', 'D1', 'D2', 'D3', 'D4']})

# print(pd.merge(left, right, on='name', how='inner'))

# dobs = pd.DataFrame({'name': ['Suzy', 'Wei','Yulia', 'Arvind'],
#                    'day': ['12', '19', '2', '23'],
#                    'month': ['Dec', 'Nov', 'May', 'Jul']})

# addresses = pd.DataFrame({'name': ['Marisol', 'Arvind','Stephan', 'Suzy'],
#                      'city': ['San Francisco', 'Denver', 'Austin', 'Seattle'],
#                      'state': ['CA', 'CO', 'TX', 'WA']})

# print(pd.merge(dobs, addresses, on='name', how='outer'))

# left = pd.DataFrame({'city': ['Springfield', 'Springfield',
#                                   'Dover', 'Chicago'],
#                          'state': ['IL', 'OH', 'DE', 'IL'],
#                          'A': ['A0', 'A1', 'A2', 'A3'],
#                          'B': ['B0', 'B1', 'B2', 'B3']})


# right = pd.DataFrame({'city': ['Cleveland', 'Dover',
#                                        'Springfield', 'Chicago'],
#                               'state': ['OH', 'NH', 'IL', 'IL'],
#                                         'C': ['C0', 'C1', 'C2', 'C3'],
#                                         'D': ['D0', 'D1', 'D2', 'D3']})


# result = pd.merge(left, right, on=['city', 'state'], how='outer')
# print(result)

row_vec = np.array([1, 2, 3]).reshape(3,-1)
print(row_vec)

