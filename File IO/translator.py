from translate import Translator

input_file = open("C:/Users/14058/OneDrive/Desktop/Programming/Python Stuff/File IO/Test folder/translate2.txt", mode = 'r', encoding = 'utf-8')
output_file = open("C:/Users/14058/OneDrive/Desktop/Programming/Python Stuff/File IO/Test folder/translated2.txt", mode = 'w', encoding = 'utf-8')

for line in input_file.readlines():
    translator = Translator(to_lang = 'ko')
    translation = translator.translate(line)
    output_file.write(translation + '\n')

# translator = Translator(to_lang = 'ko')
# translation = translator.translate("Hello. I'm Shreyas. How are you?")
# print(translation)