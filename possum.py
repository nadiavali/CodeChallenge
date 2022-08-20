# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    sum = 0
    for n in arr:
        if n >= 0:
            sum = sum + n
    return sum

print(positive_sum([1,-7,9,0,-6]))
