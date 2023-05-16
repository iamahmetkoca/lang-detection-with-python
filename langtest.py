from langdetect import detect
from iso639 import to_name 

text = input("Write something: ")  
lang = detect(text) 
lang_name = to_name(lang)  
print(lang_name) 