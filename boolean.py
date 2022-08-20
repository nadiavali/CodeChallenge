# Complete the method that takes a boolean value and return a 
# "Yes" string for true, or a "No" string for false.

# def bool_to_word(boolean):
#     if boolean == True:
#         return 'Yes'
#     else:
#         return 'No'

def bool_to_word(bool):
    return ['No', 'Yes'][bool] # bool is 0 and 1 or bool is False or True # you can replace bool with 0 or 1

print(bool_to_word(False))