import pandas as pd
from scipy.stats import norm
import numpy as np
from itertools import product

# ## Question 1



# # prices = pd.Series([1,1,2,3,5],
# #               index=['apple', 'pear', 'banana', 'mango', 'jackfruit'])

# # prices2 = pd.Series([1,1,2,3,5],
# #               index=['apple','pear', 'banana', 'mango', 'jackfruit'])


# # inventory = pd.Series([10, 50, 41, 22],
# #               index=['pear', 'banana', 'mango', 'apple'])

# # discount_prices = prices.apply(lambda x: .9*x if x>3 else x)


# # produce = pd.DataFrame({'price':prices,
# #                         'discount_price':discount_prices})

# # produce['clearance_price'] = produce['price'] *.5

# # print(produce)

# # two_clearance = produce.iloc[3, :]

# ## Question 3

# data = np.array([ 12.1085187 ,  12.10867427,  11.21137858,  10.01311363,
#                   10.79744224,  13.19280269,  12.44086123,  11.88810057,
#                   10.70064104,  11.50382741])

# def log_likelihood_normal_two_parameters(mu, sigma_sq, data_in):
#     """
#     Consume the parameters mu (mean) and sigma_sq (variance) of a normal
#     distribution, and compute the likelihood of a fixed dataset (data_in).
#     """
#     normal = norm(mu, np.sqrt(sigma_sq))
#     likelihoods = [normal.pdf(datum) for datum in data_in]
#     return np.sum(np.log(likelihoods))

# def minus_log_likelihood_normal_two_parameters(mu, sigma, data_in):
#     return - log_likelihood_normal_two_parameters(mu, sigma, data_in)

# for mu, sigma_sq in product([10, 11, 12], [1.0, 1.1, 1.2]):
#     print("Log-Lik of Two Parameter Normal Model With mu={0}, sigma_sq={1}: {2:3.2f}".format(
#         mu, sigma_sq, log_likelihood_normal_two_parameters(mu, sigma_sq, data))
#     )

# Suppose that a random sample of 50 bottles of a specific brand of bourbon are chosen and the alcohol content of each bottle is measured. Let μ
#  represent the population mean alcohol content for the population (all bottles of this bourbon). If the mean alcohol content was 39.9%, and
# the standard deviation for the sample is 2.75%, what is the lower bound of a 95% CI?

# Think its getting after a T-dist but this is what I coded but not getting the check mark:

# print(t.interval(alpha=0.95, df=49, loc=39.9, scale=(2.75/np.sqrt(50))))

# mat1 = np.array([[11, 12, 13, 24],
#                  [11, 21, 23, 55]])

# mat2 = np.array([[12, 34, 13, 24],
#                  [31, 23, 45, 54]])

# print(mat2.transpose())

## dot product
# [3, 5]   [2, 11] = [3*2 + 5*1 = 11     3*11 + 5*4 = 53]
# [1, 7]   [1, 4 ]   [1*2 + 7*1 =9          39          ]
mat1 = np.array([[3, 5],
                 [1, 7]])

mat2 = np.array([[2, 11],
                 [1, 4 ]])

# print(mat2[0][:])
# print(mat2[0, :])

def mat_multp(mat1, mat2):
    empty_mat = np.zeros(mat1.shape[0]*mat2.shape[1]).reshape(mat1.shape[0],mat2.shape[1])

    for row in range(mat1.shape[0]):
        for col in range(mat2.shape[1]):
            empty_mat[row][col] = sum(mat1[row] * mat2[:, col])

    return empty_mat

print(mat1.dot(mat2))



