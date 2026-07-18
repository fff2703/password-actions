#password strength checker
import string 

password = input("Enter your password: ")

#check if in password is upper and lower case letters 
upper_case = any([1 if i in string.ascii_uppercase else 0 for i in password])
lower_case = any([1 if i in string.ascii_lowercase else 0 for i in password])
digits = any([1 if i in string.digits else 0 for i in password])
special_characters = any([1 if i in string.punctuation else 0 for i in password])

#check the length of the password
character_count = len(password)
character_count_check = character_count >= 8

characters =[upper_case, lower_case, digits, special_characters, character_count_check]

score =0

for i in range(len(characters)):
    if characters[i]:
        score += 1


#give feedback to the user based on the score
print(f"Your password strength is: {score}/5")

# give advice on how to improve the password
print("\nSuggestions:")

if not upper_case:
    print("Add at least one uppercase letter.")

if not lower_case:
    print("Add at least one lowercase letter.")

if not digits:
    print("Add at least one number.")

if not special_characters:
    print("Add at least one special character.")

if not character_count_check:
    print("Use at least 8 characters.")

if score == 5:
    print("Your password is strong.")