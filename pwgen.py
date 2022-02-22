<<<<<<< HEAD
from random import random,choice
import string

exe = 1

def define():
    global length
    global chars
    length = int(input('\nHow big does your password need to be? \n\n'))
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    add_str_digits = input('\nDo you want to use string digits on it? "1" -> string digits / "2" -> ponctuation\n\n')
    if '1' in add_str_digits:
        chars += string.digits
    if '2' in add_str_digits:
        chars += string.punctuation
    add_str_digits = ''


def gen():
    pw = ''
    for i in range(length):
        pw += choice(chars)
    print ('\nYour new password is: '+ pw +'\n\n')

while exe != 0:
    define()
=======
from random import random,choice
import string

exe = 1

def define():
    global length
    global chars
    length = int(input('\nHow big does your password need to be? \n\n'))
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    add_str_digits = input('\nDo you want to use string digits on it? "1" -> string digits / "2" -> ponctuation\n\n')
    if '1' in add_str_digits:
        chars += string.digits
    if '2' in add_str_digits:
        chars += string.punctuation
    add_str_digits = ''


def gen():
    pw = ''
    for i in range(length):
        pw += choice(chars)
    print ('\nYour new password is: '+ pw +'\n\n')

while exe != 0:
    define()
>>>>>>> ee68593f729a66d2cd53079e588c54a5f395cdeb
    gen()