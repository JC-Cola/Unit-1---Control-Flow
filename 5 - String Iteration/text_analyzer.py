text = input("Enter a text: ")
# initalize counters
total_chars = len(text)
letter_count = 0
digit_count = 0
uppercase_count = 0
lowercase_count = 0

# track first and last char
first_letter = None
last_letter = None

print(f"Analyzing: '{text}'")
print("=" * 40)

# process each char
for char in text:
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        letter_count +=1
        if first_letter is None:
            first_letter = char
        last_letter = char # keep udating (last one wins)
    # count uppercase
    if 'A' <= char <= 'Z':
        uppercase_count +=1
    # count lowercase
    if 'a' <= char <= 'z':
        lowercase_count +=1
    # count digit
    if '0' <= char <= '9':
        digit_count +=1
        
print(f"Total Characters: {total_chars}")
print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"First character: {first_letter}")
print(f"Last character: {last_letter}")
