import random
import string

def get_lenght():
	length = input('enter the password length: ')
	try:
		length = int(length)
	except:
		print('enter the number (e.g. 12)')
		get_lenght()
	return length

def get_spec_characters():
	print('specify the special characters that will be in your password')
	print(f'by default: {string.punctuation}  (press enter)')
	special_characters = input('').replace(" ", '') or string.punctuation
	return special_characters


length = get_lenght()

special_characters = get_spec_characters()

# ascii_letters = lowers + uppers
total = string.ascii_letters + string.digits + special_characters

password = ''.join(random.sample(total, length))

print(password)

