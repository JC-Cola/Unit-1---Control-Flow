age = input("Enter your age: ")
rate = input("Enter the rating of the movie (G/PG/PG-13/R): ")

if not age:
    print("ERROR: Please enter your age")
    
if not rate:
    print("ERROR: Please enter the rating")
    
elif rate == "G": 
    print("APPROVED: You can watch this movie!")
    
elif rate == "PG":
    if age >= 6:
        print("APPROVED: You can watch this movie!")
    else: 
        print("Must be 6+ for PG-rated movies")
        
elif rate == "PG-13":
    if age >= 13:
        print("APPROVED: You can watch this movie!")
    else:
        print("Not recommended for your age")
    
elif rate == "R":
    if age >= 17:
        print("APPROVED: You can watch this movie!")
    else:
        print("Must be 17+ for R-rated movies")
