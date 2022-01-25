# Random Password Generator using Python

#import the necessary modules!
import random
import string

print('hello, Welcome to Password generator!')

#input the length of password
length = int(input('\nEnter the length of password: '))                      

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = "*%$#@!&"
#string.ascii_letters

#How many password you want to create
count = int(input('\nEnter how many password you want to create: '))
i = 1
while i <= count:
    #combine the data
    all = lower + upper + num + symbols

    #use random 
    temp = random.sample(all,length)

    #create the password 
    password = "".join(temp)

    #print the password
    print(password)

    i += 1 