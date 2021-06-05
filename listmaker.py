#####################################################################
#                                                                   #
#  Amjad's Social Media Username Generator                          # 
#  v0.1                                                             #
#  Uses the User Requirements of Instagram, Twitter and Snapchat    #
#  Program was written at 5/6/2021                                  #
#                                                                   #
#####################################################################

import string
import random
import os 
import time

dir_path = os.path.dirname(os.path.realpath(__file__)) #current directory

num = int(input("number of chars:"))
limit = int(input("number of words:"))

text = list(''.join((string.ascii_lowercase,string.ascii_lowercase, string.digits, "_", ".")).strip())
fileNum = 1
while os.path.isfile(f'{dir_path}//randomizer {fileNum}.txt'):
    fileNum = fileNum + 1
randomizedFile = open(f'{dir_path}//randomizer {fileNum}.txt',"a")
print(f"text file created at {dir_path}//randomizer {fileNum}.txt")
print("starting in 3 seconds...")
time.sleep(3)

def generate():
    i=0
    word = []
    while i < num:
        i+=1
        word.append(random.choice(text))
    print(''.join(word))
    randomizedFile.write(''.join(word))
    randomizedFile.write("\n")
tic = time.perf_counter() #Program timer start
count = 0
while count<=limit:
    count += 1
    generate()
toc = time.perf_counter() #Program timer stop
randomizedFile.close()
print(f"Program finished in {toc - tic:0.4f} seconds")