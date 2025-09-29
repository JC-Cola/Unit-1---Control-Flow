text = 'Hello Word'
# vowels = 0
# for char in text:
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#         vowels +=1
#     elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
#         vowels +=1
        
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text: 
    if char in vowels:
        vowel_count += 1

print(vowel_count)

text1 = "ABC123xyz"
for i in range (len(text1)):
    if '0' <= text1[i] <= '9':
        print(f"Digit at position {i}: {text1[i]}")
        
word = "Hello"
for i in range(len(word)):
    print(f"{word[i]} at index {i} and {word[-1-i]} at index {-1-i}")