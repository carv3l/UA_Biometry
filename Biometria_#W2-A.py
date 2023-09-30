dict_all = {}

list_words = []

char_text = input("Input Text:\n")
 
list_words = [*char_text]
    
for letter in list_words:
    
    if letter.isalpha():
        dict_all[letter] = list_words.count(letter)
        
print(dict_all)
    
