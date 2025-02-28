'''# 1.Debugging'''
# >>>2.2
# >>>c:/Users/leon2/python_decal/yuang_decal/homework4.py
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# 0
# >>>I got incorrect answer for question 2
# >>>change the return to outside of the loop and it gives me complete answers

# >>>2.3
# >>>File "c:\Users\leon2\python_decal\yuang_decal\homework4.py", line 48, in first_15_elements
#     return squarelist[:15]
# TypeError: 'function' object is not subscriptable
# >>> replacing the called object from a function to refered list makes it work

# >>>3.2
# >>>Traceback (most recent call last):
#   File "c:\Users\leon2\python_decal\yuang_decal\homework4\homework4.py", line 123, in <module>
#     print(modified_2d_list(matrix))
# NameError: name 'matrix' is not defined
# >>> define matrix = create_2d_list()

'''2.1 Making a List Variable'''
# Create a variable (name it anything you want, but make it descriptive!) that
# is assigned to a list with numbers 0 through 20. You should not write each
# number manually.
# >>> whateverNameYouWant = # Your code here
# >>> print(whateverNameYouWant)
# [0, 1, 2, ..., 20] # It should print all numbers 1-20 in a list

num_list = list(range(21))
print(num_list)

'''2.2 Working with List Elements'''
# Write a function that will take in your list from Part 2.1 and square each element
# in the list. Assign the result to a new variable.
# 1
# >>> whateverNameYouWant = # Your code from Part 2.1
# >>>
# >>> def squareList():
# >>> # Your code here
# >>>
# >>> anotherNameYouWant = squareList(list)
# >>> print(anotherNameYouWant)
# [0, 1, 4, ..., 400]

def squarelist(num_list):
    sq_nums = []
    for int in num_list:
       sq_nums.append(int ** 2)
    return sq_nums
print(squarelist(num_list))

'''# 2.3 Slicing'''
# Write a function that takes in your new list from Part 2.2 and returns the first
# 15 elements of the list using slicing.
# >>> anotherNameYouWant = squareList(list)
# >>> first_fifteen_elements(anotherNameYouWant)
# [0, 1, 4, ..., 196]

def first_15_elements(squarelist):
    return squarelist[:15]
squared_nums = squarelist(num_list)
print(first_15_elements(squared_nums))

'''# 2.4 Striding'''
# Write a function that takes in your list from Part 2.2 and returns every 5th
# element from the list using striding.
# >>> anotherNameYouWant = squareList(list)
# >>> every_fifth_element(anotherNameYouWant)
# [16, 81, 196, 361]

def skip_5_num(squarelist):
    return squarelist[4::5]
print(skip_5_num(squared_nums))

'''# 2.5 Slicing & Striding'''
# Write a function that takes your list from Part 2.2, slices the last 3 elements of
# the list, and then returns every 3rd element from that list in reverse order.
# >>> anotherNameYouWant = squareList(list)
# >>> fancy_function(anotherNameYouWant)
# [400, 289, 196, 121, 64, 25, 4]

def slicing_striding(squarelist):
    return squarelist[-1::-3]
print(slicing_striding(squared_nums))

'''3.1 Creating a 5x5 2D List'''
# Write a function that uses nested for loops to create a 5x5 2D list where the
# numbers 1 through 25 are stored sequentially. Assign the result to a new vari-
# able.
# >>> matrix = create_2d_list()
# >>> print(matrix)
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
# [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

def create_2d_list():
    matrix = []
    count = 1

    for i in range(0,5):
        row = []
        for j in range(0,5):
            row.append(count)
            count +=1
        matrix.append(row)
    return matrix 

print(create_2d_list()) 




'''3.2 Replacing 2D List with Multiples of 3'''
# With the 2D list you created in Part 3.1, write a function that will replace all
# multiples of 3 with the character “?”.
# >>> matrix = create_2d_list()
# >>> modified_2d_list(matrix)
# [[1, 2, ‘?’, 4, 5],
# [‘?’, 7, 8, ‘?’, 10],
# [11, ‘?’, 13, 14, ‘?’],
# [16, 17, ‘?’, 19, 20],
# [‘?’, 22, 23, ‘?’, 25]]

matrix = create_2d_list()
def modified_2d_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix
print(modified_2d_list(matrix))

'''3.3 Summing None-’ ?’ Elements'''
# Assign the result of your function from Part 3.2 to a variable. Write a function
# that will iterate through the new 2D list variable and return the sum of all the
# elements that are not “?”. Hint: Try using “!=”.
# >>> matrix = create_2d_list()
# >>> new_matrix = modified_2d_list(matrix)
# >>> sum_non_question_elements(new_matrix)
# 217

def sum_non_question_elements(matrix):
    sum = 0
    for i in matrix:
        for j in i:
            if j != "?":
                sum +=j
    return sum

print(sum_non_question_elements(matrix))








                        






