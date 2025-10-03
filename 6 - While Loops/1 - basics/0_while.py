#syntax:
'''
initialize variable
while condition:
    code block
    increment/decrement
'''
num = 5
while num >= 1:
    print(num)
    num -=1

num = 1
total = 0
# while num <= 10:
#     total += num
#     num +=1
# print(total)

while num <= 10:
    total += num
    if num < 10:
        print(num, end="+")
    else:
        print(num, end="=")
    num +=1
print(total)

#Sum of digits
#Take user input as int, and sum the digits of it
# number = input("Enter numbers to be added: ")
sum = 0
# for char in number:
#     sum += int(char)
# print(sum)

# i = 0
# while i<len(number):
#     sum += int(number[i])
#     i += 1
# print(f"Total: {sum}")

# Algorithim - sum of 
n = int(input("Enter a number: "))
number = n
sum = 0
while number > 0:
    digit = number % 10 #Get the last digit
    sum += digit #Add to sum
    number = number // 10 #Remove the last digit

print(f"The sum of digits {n}: {sum}")


# Algorithm - count digits (as ints)
number = 54321
n = number
count = 0
while number > 0:
    count +=1
    number = number // 10
print(f"The count of {n} is {count}")