# # 1. You have been plopped into this directory system. What command will tell you what your working directory is?
# pwd

# # 2. The command tells you ∼/python decal/judy decal. What command with list all the files in your current working directory?
# ls

# # 3. Brianna just sent out an announcement that there was a typo on homework.py. So you need to pull the updates. What commands will let you move to the correct repository and pull the latest changes?
# git pull origin master/main 

# # 4. How would you move this new homework.py to your personal repository homework directory?
# mv homework.py my_repo/

# # 5. You want to see the contents of the homework.py in your terminal from your personal repository. What command(s) will let you do this?
# cat homework.py 

# # 6. You want to edit the contents of the homework.py in your terminal from your personal repository. What command will let you do this?
# nano homework.py

# # 7. You have finished the homework. What commands will allow you to save the changes and push from your local repository to your remote repository?
# git add homework.py
# git commit -m "add homework.py"
# git push original main

# # 9. What absolute path will allow you to move to Recents/?
# cd ~/recents/

# 2.1 Data Types
# Write a function that takes any input and returns a string indicating its data
# type.
# >>> checkDataType(3.14)
# ‘float’
# >>> checkDataType(True)
# ‘bool’

def checkDataType(i):
    return type(i)
print(type(3.14))
print(type(True))

# 2.2 Conditionals
# Write a function that takes an integer as input and returns ’Even’ if the integer
# is even, and ’Odd’ otherwise.
# >>> evenOrOdd(7)
# ’Odd’
# >>> evenOrOdd(10)
# ’Even’

def checkIntType(i):
    if i % 2 == 0:
        return 'even' 
    else:
        return 'odd'
print(checkIntType(7))

# 3 Loops
# Write a function that takes a list of integers and returns their sum using a loop
# (do NOT use the built-in sum() function).
# >>> numbers = [1, 2, 3, 4, 5]
# >>> sumWithLoop(numbers)
# 15

numbers = [1, 2, 3, 4, 5]

def SumofNums(i):
    total = 0
    for num in i:
        total += num
    return total

print(SumofNums(numbers))

# 4.1 Lists
# Write a function that takes a list and returns a new list with each element
# duplicated.
# >>> duplicateList([‘a’, ‘b’, ‘c’])
# [‘a’, ‘a’, ‘b’, ‘b’, ‘c’, ‘c’]

def duplicatelist(i):
    new_list = []
    for j in i:
        new_list.append(j)
        new_list.append(j)
    return new_list
print(duplicatelist(['a', 'b', 'c']))

# 4.2 Debugging
# There’s an error in the following function that’s supposed to return the square
# of a number. Find and correct it:
# def square(num)
# return num * num

def square(num):
    return num * num
print(square(3))










    



    



