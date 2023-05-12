# Write a function that takes an unknown number of arguments and returns their sum.
def sum_numbers(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print(sum_numbers(1,2,3,4,5))  

# Write a function that takes two arguments, the first being a string and 
# the second being an unknown number of integers. The function should return 
# a new string where the integers have been added to the original string.
def adding_nums(sent,*integers):
    result =sent
    for integer in integers:
        result+=str(integer)
        return result
print(adding_nums("The sum of the intergers: ",2,3,4,5,7))

# Write a function that takes an unknown number of keyword arguments and 
# returns a dictionary where the keys are the argument names and the values are the argument values.
def unknown_name(**names):
    # for key,value in names:
    #     print(f"{key}""{value}")
    return names
print(unknown_name(name="Jemima",age=19))

# Write a function that takes a function and an unknown number of arguments, and returns
# the result of calling the function with the arguments.

def function_nums(unknown_num,*nums):
    return unknown_num(*args)
def multiply_numbers(*nums):
    total=1
    for num in nums:
        total*=num
    return total
print(function_nums (multiply_numbers,5,6,7,8))



    










