weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
num = (weight/(height*height)) * 703

bmi = ("Underweight" if num < 18.5 else
       "Normal" if 18.5 <= num < 25 else
       "Overweight" if 25 <= num < 30 else
       "Obese"
       )
print(f"Your BMI is {num}")
print(f"You category is {bmi}")