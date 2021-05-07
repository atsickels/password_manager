'''
Austin Sickels
5/7/2021
'''

import os.path
from datetime import date
import random

char_begin = 33 # The beginning of the range of ascii characters we want to allow
char_end = 123 # The end of the range of ascii characters we want to allow

class Password:

    def __init__ (self):
        self.website = None
        self.length = 0
        self.password = ""
        self.last_changed = date.today()

    def save_password(self, filename):
        filename.write(
            f"{self.website}: {self.password}\n{self.last_changed}\n")

    def generate_password(self):
        for i in range(0, self.length):
            char = random.randint(char_begin, char_end)
            self.password = self.password + chr(char)

    def set_params(self):
        self.website = input("Enter website name: ")
        self.length = int(input("Enter length of password: "))


def find_and_reset(password_to_find):
    with open('password_list.txt') as f:
        datafile = f.readlines()
    for line in datafile:
        if password_to_find in line:
            return True # The string is found
    print("Password does not exist")



if __name__ == '__main__':
    if not os.path.exists("password_list.txt"):
        file_to_create = open("password_list.txt", "w")
        file_to_create.close()
    file = open("password_list.txt", "a+")

    currPass = Password()
    currPass.set_params()
    currPass.generate_password()
    currPass.save_password(file)
    find_and_reset('Tes')
