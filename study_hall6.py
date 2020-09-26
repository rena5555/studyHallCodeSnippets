import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# dobs = pd.DataFrame({'name': ['Suzy', 'Wei','Yulia', 'Arvind'],
#                    'day': ['12', '19', '2', '23'],
#                    'month': ['Dec', 'Nov', 'May', 'Jul']})
# addresses = pd.DataFrame({'name': ['Marisol', 'Arvind','Stephan', 'Suzy'],
#                      'city': ['San Francisco', 'Denver', 'Austin', 'Seattle'],
#                      'state': ['CA', 'CO', 'TX', 'WA']})

# frames = [addresses, dobs]

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.intersection(set2))

# grocery = pd.DataFrame({'category':['produce', 'produce', 'meat',
#                                     'meat', 'meat', 'cheese', 'cheese'],
#                         'item':['celery', 'apple', 'ham', 'turkey',  'lamb',
#                                 'cheddar', 'brie'],
#                         'price':[.99, .49, 1.89, 4.34, 9.50, 6.25, 8.0]})

# grouped = grocery.groupby('category')

# one_mean = grouped.filter(lambda x: x.mean() >= 3)

# two_max = grouped.max()

# grocery['price'] = grouped.transform(lambda x: x * .9 if x.max() > 3 else x)

# three_round = grocery['price']

# customers = pd.DataFrame([
#     [100, 'Prometheus Barwis', 'prometheus.barwis@me.com', '(533) 072-2779'],
#     [101, 'Alain Hennesey', 'alain.hennesey@facebook.com', '(942) 208-8460'],
#     [102, 'Chao Peachy', 'chao.peachy@me.com', '(510) 121-0098'],
#     [103, 'Somtochukwu Mouritsen', 'somtochukwu.mouritsen@me.com','(669) 504-8080'],
#     [104, 'Elisabeth Berry', 'elisabeth.berry@facebook.com','(802) 973-8267']],
#     columns = ['customer_id', 'name', 'email', 'phone'])

# orders = pd.DataFrame([[1000, 100, 144.82], [1001, 100, 140.93],
#                        [1002, 102, 104.26], [1003, 100, 194.60],
#                        [1004, 100, 307.72], [1005, 101,  36.69],
#                        [1006, 104, 039.59], [1007, 104, 430.94],
#                        [1008, 103, 031.40], [1009, 104, 180.69],
#                        [1010, 102, 383.35], [1011, 101, 256.20],
#                        [1012, 103, 930.56], [1013, 100, 423.77],
#                        [1014, 101, 309.53], [1015, 102, 299.19]],
#                columns = ['order_id', 'customer_id', 'order_total'])

# total_spent = orders.groupby("customer_id").sum()['order_total']

# # for group, row in grouped_orders:
# #     print(group)
# #     print(row)

# # orders.drop(['order_id', 'order_total'], axis =1, inplace = True)

# # customers.drop(['email', 'phone'], axis =1, inplace = True)

# customer_spend = pd.merge(customers, total_spent, on="customer_id", how="inner")

# customer_spend['total_spend'] = customer_spend['order_total']

# variable = customer_spend[['customer_id', 'name', 'total_spend']]

# variable.hist()
# plt.savefig('~/Desktop/histogram_facey.png')

import numpy as np

#same params and behavior as range(), except returns np.array
# arr = np.arange(12)

# # print(arr[arr % 2 == 0])

# arr[arr % 2 == 0] += 1

# print(arr[arr < 5])

matrix = np.array([[42, np.nan, 89, 2],
                   [99, np.nan, 42, 2],
                   [55, 42, 17, 2]])

# print(np.isnan(matrix))

row_vector = np.arange(1, 7).reshape(1, -1)

print(matrix)
