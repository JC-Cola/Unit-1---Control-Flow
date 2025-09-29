password = input("Enter your password: ")
length = len(password)
uppercase_count = 0
lowercase_count = 0
digit_count = 0
special_count = 0
specials = "~!@#$%^&*()_+|:<>?"

for char in password:
    if 'A' <= char <= 'Z':
        uppercase_count +=1
    if 'a' <= char <= 'z':
        lowercase_count +=1
    if '0' <= char <= '9':
        digit_count +=1
    if char in specials:
        special_count +=1
        
print("PASSWORD ANALYSIS:")
print("="*20)
print(f"Password {password}")
print("")
print("CHARACTER COUNTS:")
print(f"Length: {length} characters")
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_count}")
print("")
print("REQUIREMENTS CHECK:")
if length >= 8:
    print("Length (8+ characters): PASSED")
else:
    print("Length (8+ characters): FAILED")

if uppercase_count >= 1:
    print("Uppercase letters: PASSED")

else:
    print("Uppercase letters: FAILED")
    
if lowercase_count >= 1:
    print("Lowercase letters: PASSED")
else:
    print("Lowercase letters: FAILED")
    
if digit_count >= 1:
    print("Digits: PASSED")
else:
    print("Digits: FAILED")
    
if special_count >= 1:
    print("Special characters: PASSED")
else:
    print("Special characters: FAILED")

print("")
print("SECURITY ISSUES:")
for i in range(len(password)-2):
    if password[i] == password[i+1] == password[i+2]:
        print("Contains repeated characters (3+)")
        break
    else:
        print("No repeated characters (3+)")
        break
        
if "123" in password:
    print("Contains sequence 123")

if "abc" in password:
    print("Contains sequence abc")
    
print("")
rating = None
if length >= 8 and uppercase_count >= 1 and lowercase_count >= 1 and digit_count >= 1 and special_count >= 1 and not ("123" in password) and not ("abc" in password):
    rating = "STRONG"
elif length >= 8 and uppercase_count >= 1 and lowercase_count >= 1 and digit_count >= 1 and special_count >= 1:
    rating = "MEDIUM"
else:
    rating = "WEAK"
print(f"FINAL RATING: {rating}")