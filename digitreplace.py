# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 
# and above with '1'. Return the resulting string.

# Note: input will never be an empty string    #366058562030849490134388085

def fake_bin(x):
    n = ''                     # It can be any thing here
    for i in x:
        if int(i) < 5:
            n = n + '0'        # n is an no value variable so it does not make change
        else:
            n = n + '1'
    return n

print(fake_bin('366058562030849490134388085'))
print('366058562030849490134388085')

# def repl(num_str):
#     binary = num_str
#     for i in range(9 + 1):
#         if i < 5:
#             binary = binary.replace(str(i), "0")
#         else:
#             binary = binary.replace(str(i), "1")
#     return binary