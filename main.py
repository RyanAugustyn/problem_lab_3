
#Task 1 Happy Numbers
#19 is a happy number; 1^2 + 9+2 = 82; 8^2 + 2^2 = 68; 6^2 + 8^2 = 100; 1 ^2 + 0^2 + 0^2 = 1

#do a check if in infinite loop, if the initial number ever equals one of the results
#take in a number
#separate the digits 
#do a loop that squares the separated digits 
#if the squared numbers sum ever reaches one, return True; else return false

#first few happy numbers are 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100


def is_happy_number(num_input):
    str_num = str(num_input)
    temp = 0
    while(True):
        for x in str_num:
            temp += int(x) * int(x)
            str_num = str(temp)
        #realized from an infinite running loop that number 4 kept coming up, seems to be a viable check  
        if temp == 4:
            return str(num_input) + ' is sad'
        elif temp == 1:
            return str(num_input) + ' is happy'
        temp = 0

# test = is_happy_number(23)
# print(test)


#Task 2: Prime Numbers
#A prime number is a number that is only divisible by one and itself. 
# Write a method that prints out all prime numbers between 1 and 100

#enter a number 
#loop through all numbers 1-100
#take a number and loop through up to half of itself; 50 will not be divisible by something beyond 25
#use modulo, check for remainder to see if divisible
#if not, add to list of prime numbers 
#look up converting float to int: math.ceil()
#1 is not a prime number having only one factor 

from math import ceil

def find_primes(num_input):
    results = []
    for x in range(2, num_input):
        for y in range(2, ceil(x/2) + 1): #was adding in 4, but printing all else correct, so added 1
            if x % y == 0:
                break   
        else:
            results.append(x)
    return results

# test = find_primes(1000)
# print(test)

#The prime numbers from 1 to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
#    output                          [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]




#Task 3: Fibonacci
#A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
# Write a method that does the Fibonacci sequence starting at 1
# HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs

#take in user input
#write first a version that takes a max number as an argument
#take two numbers, set equal to 0 and 1
#do a while loop that has a variable to keep track of current number addition, and add the two others together
#works, now try with starting number
#loop a set number of times, maybe 10, so no infinite loop

def fibonacci_nums(num_input):
    x1 = 0
    x2 = 1
    result =[1]
    fib_num = 1
    while fib_num < num_input:
        fib_num = x1 + x2
        result.append(fib_num)
        x1 = x2
        x2 = fib_num
    return result

test = fibonacci_nums(9)
print(test)

