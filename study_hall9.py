import numpy as np
import random
import scipy.stats as stats
import matplotlib.pyplot as plt
# import statistics as stats


## Stats

# # PMF
# P(X = k)

# # PDF
# Relative probability (not an explicit prob. . . . can't use for prob. calculations)

# # CDF
# P(X <= k)

# print(sum([random.choice(np.arange(1,7)) for _ in range(100000)]) / 100000)

# # binomial
# p = 0.005
# n = 1000
# k = 10

# # P(X >= 10) = ???

# # P(X >= 10) = 1 - P(X <= 9))

# # P(5 < x < 10) = P(X <= 9) - P(X <= 5)

# print(1 - stats.binom.cdf(k-1, n, p))

## Central Limit Theorem

# Create a normal distribution with mu = 5, sd = 2, n = 1000
# pop_norm1 = np.random.normal(5, 2, 1000)
# pop_norm2 = np.random.normal(20, 2, 1000)

# dist = np.array(list(pop_norm1) + list(pop_norm2))

# plt.hist(dist, bins=20)
# plt.show()

# # Plot frequency histogram
# plt.hist(pop_norm, bins=20)
# plt.show()

# def subset_mean(arr):
#     # take sample size 30
#     return np.mean([arr[random.randint(0,(len(arr)-1))] for _ in range(100)])

# plt.hist([subset_mean(dist) for _ in range(100000)], bins=20)
# plt.show()


# print(subset_mean(pop_norm))

# mean = 63
# sd = 12
# sd_mean = 12 / np.sqrt(36)

# # P(X_bar <= 59) = ??
# print(stats.norm.cdf(59, loc=mean, scale= sd_mean))

B = np.array([[ -5,  3, -1], [-3, 6,  -1], [-1, -7, 3]])

B_inv = np.linalg.inv(B)

print(B_inv.dot(np.array([[-10], [18], [-38]])))
