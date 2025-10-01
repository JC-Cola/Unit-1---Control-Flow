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
number = input("Enter numbers to be added: ")
sum = 0
# for char in number:
#     sum += int(char)
# print(sum)

i = 0
while i<len(number):
    sum += int(number[i])
    i += 1
print(f"Total: {sum}")

