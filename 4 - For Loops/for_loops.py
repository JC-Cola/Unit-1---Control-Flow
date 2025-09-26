# Three forms of range() function
#1 range(stop)
for i in range(5): #0,1,2,3,4
    print(i)
    
#2 range(stop, stop)
for i in range(3, 8): #3,4,5,6,7
    print(i)
    
#3 range(start, stop, step)
for i in range(2, 11, 2): #2,4,6,8,10
    print(i)
#counting backwards
for i in range(10, 1, -2):
    print(i)
    
# Countdown Timer
import time
for seconds in range (10, -1, -1):
    print(f"{seconds}-seconds")
    #time.sleep(1) #wait 1 seconds between numbers
print("BLAST OFF! 🚀")

# Multiplication Table
# Take user input for the number and print the table
num = int(input("Enter a number for the multiplication table: "))
for i in range(1, 11, 1):
    print(f"{num}x{i:2d}={num*i:3d}")