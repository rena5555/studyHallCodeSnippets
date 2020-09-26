import math
import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# customers = pd.DataFrame([
#         [100, 'Prometheus Barwis', 'prometheus.barwis@me.com', \
#              '(533) 072-2779'],
#         [101, 'Alain Hennesey', 'alain.hennesey@facebook.com', \
#              '(942) 208-8460'],
#         [102, 'Chao Peachy', 'chao.peachy@me.com', '(510) 121-0098'],
#         [103, 'Somtochukwu Mouritsen', 'somtochukwu.mouritsen@me.com', \
#             '(669) 504-8080'],
#         [104, 'Elisabeth Berry', 'elisabeth.berry@facebook.com', \
#             '(802) 973-8267']
#         ],
#     columns = ['customer_id', 'name', 'email', 'phone'])

# # print(customers)

# orders = pd.DataFrame([[1000, 100, 144.82], [1001, 100, 140.93],
#                        [1002, 102, 104.26], [1003, 100, 194.6 ],
#                        [1004, 100, 307.72], [1005, 101,  36.69],
#                        [1006, 104,  39.59], [1007, 104, 430.94],
#                        [1008, 103,  31.4 ], [1009, 104, 180.69],
#                        [1010, 102, 383.35], [1011, 101, 256.2 ],
#                        [1012, 103, 930.56], [1013, 100, 423.77],
#                        [1014, 101, 309.53], [1015, 102, 299.19]],
#                columns = ['order_id', 'customer_id', 'order_total'])

# # # Combine and aggregate the above DataFrames according to the instructions.
# # # Feel free to use multiple steps.

# temps = pd.DataFrame({
#     'time': ['morning', 'noon', 'night',
#              'morning', 'noon', 'night',
#              'morning', 'noon', 'night',
#              'morning', 'noon', 'night'],
#     'city': ['Denver', 'Denver', 'Denver',
#              'Austin', 'Austin', 'Austin',
#              'NYC', 'NYC', 'NYC',
#              'SFO', 'SFO', 'SFO'],
#     'temp': [46, 57, 52,
#              51, 68, 53,
#              32, 32, 33,
#              53, 71, 61]})

# cities = pd.DataFrame({
#     'city' : ['NYC', 'Austin', 'SFO', 'Denver'],
#     'latitude' : ['40.7N', '30.27N', ' 37.78', '39.7N'],
#     'longitude' : ['74.002W', '97.7W', '122.42W', '104.99W'],
#     'State' : ['NY', 'TX', 'CA', 'CO']})

# print(temps)

# city_avg = temps.groupby('city')['temp'].mean()

# cities_with_mean = pd.merge(cities, city_avg, on='city')

# cities_with_mean['avg_temp'] = cities_with_mean['temp']
# cities_with_mean.drop('temp', inplace=True, axis=1)

# cities_with_mean.rename(columns={'temp' : 'avg_temp',
#                                  'latitude' : 'lat',
#                                  'longitude': 'long'},
#                                  inplace=True)

# print(cities_with_mean)

# cities_with_mean = cities_with_mean[['city', 'State', 'avg_temp']]

# # print(cities_with_mean)

# cit_avg = temps.groupby('city').transform(lambda x: 1 if x.mean() > 55 else 0)

# # print(cit_avg)

# cit_avg.to_csv('test.csv')

cars = pd.read_csv('csv.csv', sep='|')


# cars['mpg'].hist(bins=20)
# cars.hist('mpg', bins=20)
cars.plot(y='mpg', kind='hist', bins=20)
plt.show()

# unif_data =  np.array([ 12.74150234,   7.48813381,  11.7510409 ,   5.93809414,
#                          4.68964288,   3.70627976,   3.46101127,   6.41408594,
#                         10.21747766,   8.71674398,   3.60720254,   9.65162582,
#                          6.58295132,   7.31954815,   7.49708025,   5.66849976,
#                          6.35144344,  12.08445868,   7.80220492,   9.83051264,
#                         12.19963228,   3.59743489,  11.4528373 ,   5.77606004,
#                         10.68932553,  10.41001181,  12.31509935,  12.31377402,
#                          9.99084698,   5.64170829,   4.8600061 ,   3.83064209,
#                          5.80984023,  11.87182268,   8.62335338,   5.27884731,
#                         12.12025134,   4.35138826,   4.26284551,   6.70120651,
#                         12.91554048,  10.58164179,  10.33635382,   9.18362962,
#                          7.06904495,  10.03298992,   5.95876344,   6.05199525,
#                         10.08473599,   9.1744051 ])

# mean = np.mean(unif_data)
# var = np.var(unif_data)

# lower_bound = mean -  np.sqrt(3 * var)
# upper_bound = mean + np.sqrt(3 * var)

