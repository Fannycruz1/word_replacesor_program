# creating a function 

def replace_word():
    str = input("Enter the text you'd like to edit: ")
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace,word_replacement))

replace_word()

