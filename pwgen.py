from random import random,choice
import string


exe = 0


def define():
    global length
    global chars
    global pw
    length = int(input('\nHow big does your password need to be? \n\n'))
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    add_str_digits = input('\nDo you want to use string digits and/or ponctuation on it? "1" -> string digits / "2" -> ponctuation\n\n')
    if '1' in add_str_digits:
        chars += string.digits
    if '2' in add_str_digits:
        chars += string.punctuation
    add_str_digits = ''
    

def gen():
    pw = ''
    for i in range(length):
        pw += choice(chars)
    return pw
    

define()
while exe != 1:
    password = gen()
    print ('\nGenerated password: '+ password +'\n\n')
    exe = int(input('Did you like this one? 1 -> yes /// something else -> no \n\n'))


print ('\nYour new password is: '+ password +'\nGood one!\n\n')