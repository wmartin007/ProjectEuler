# ProjectEuler.net
# Problem6
# William Martin
# 2/22/2018

# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.

nums = range(1,101)

sum_of_squares = sum(x**2 for x in nums)

square_of_sums = (sum(nums)**2)

diff = square_of_sums - sum_of_squares

print(diff)
