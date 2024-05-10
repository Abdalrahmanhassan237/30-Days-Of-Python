# strings can be stored in variables
first_name = input('what is your first name ? ')
last_name = input('what is your last name ? ')
# you can combine strings with +
print('Hello '+first_name.capitalize() +' '+last_name.capitalize())

# you can use functions (methods) to modify strings
sentence = input('enter any sentence : ')
print('upper case : ' , sentence.upper())
print('lower case: ',sentence.lower())
print(sentence.capitalize()) # this method make first character upper
print(sentence.title()) # this method make first character of each word separated by space upper
print(sentence.count('a')) # count how much character appear in sentence

# slicing string 

print(sentence[:9]) # Slice From the Start  
print(sentence[0:]) # Slice To the End
print(sentence[0:9:-1]) # slicing string from the end
print(sentence[4::2])
print(sentence[-6:-2]) # Negative Indexing


# check strings

txt = "The best things in life are free!"
if "free" in txt :
    print("Yes, 'free' is present.") 
elif "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
 
  

