from string import ascii_letters, punctuation, digits
from random import choice, randint

min = 1999
max = 2001

string_format = ascii_letters + punctuation + digits

generated_string = "".join(choice(string_format) for x in range(randint(min, max)))

print("Your String is: {0}".format(generated_string))
