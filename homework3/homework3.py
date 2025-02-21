#1.
def power_loop(x,y):
    result = 1
    for _ in range(y):
        result *=x
    return result
print(power_loop(2,3))

#2.
readings = [15, 14, 17, 20, 23, 28, 20]

def find_min_max(readings):
    min_temp = min(readings)
    max_temp = max(readings)
    return(min_temp, max_temp)
print(find_min_max(readings))

#3.
def is_weekend(true):
    return true in (6, 7)
print(is_weekend(4))

#4.
def efficiency(dist, fuel):
    return dist // fuel
print(efficiency(514, 114))

#5.
def decode(n):
    if n < 10:
        return n
    
    last_dig = n % 10 #5
    remains = n // 10 #1234

    num = 1
    temp = remains
    while temp > 0:
        temp //= 10
        num *= 10

    return last_dig * num + remains
print(decode(12345))

#6.1
nums = [2024, 98, 131, 2, 3, 72]

def min_number(nums):
    min_val = nums[0]
    for i in nums:
         if i < min_val:
              min_val = i
    return min_val
   
print(min_number(nums))

def max_number(nums):
    max_val = nums[0]
    for i in nums:
         if i > max_val:
              max_val = i
    return max_val

print(max_number(nums))

#6.2
nums = [2024, 98, 131, 2, 3, 72]

def find_min_with_while_loop(nums):
    min_val = nums[0]
    i = 0

    while i < len(nums):
        if nums[i] < min_val:
            min_val = nums[i]
        i += 1
    return min_val
print(find_min_with_while_loop(nums))

def find_max_with_while_loop(nums):
    max_val = nums[0]
    i = 0

    while i < len(nums):
        if nums[i] > max_val:
            max_val = nums[i]
        i += 1
    return max_val
print(find_max_with_while_loop(nums)) 

#7
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"
    i = 0
    vowel_no = 0
    consonant_no = 0

    while i < len(text):
        if text[i].isalpha():
            if text[i] in vowels:
                vowel_no +=1
            else:
                consonant_no +=1
        i +=1
    return(vowel_no, consonant_no)
text = "To bugs and errors: What is love? Baby don't hurt me, don't hurt me, no more"
print(vowel_and_consonant_count(text))

#8
num = 2468
def digital_root(num):
    i = 0
    while num > 0:
        i += num % 10
        num //= 10
    return i
print(digital_root(num))



    
                

    




    




