import re

names = []
numbers= []
emails = []

file_path = 'example.txt'

with open(file_path,'r') as file:
    data = file.read()


name_pattern = re.compile(r'\b[A-Za-z]+\s[A-Za-z]+\b')
number_pattern = re.compile(r'\b\d{11}\b')
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

potential_names = name_pattern.findall(data)
numbers = number_pattern.findall(data)
emails = email_pattern.findall(data)

valid_names = [name for name in potential_names if 'gmail' not in name.lower() and 'com' not in name.lower()]

names.extend(valid_names)

print("Names:",names)
print("Numbers:",numbers)
print("Emails:",emails)
