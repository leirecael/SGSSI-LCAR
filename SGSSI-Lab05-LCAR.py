import hashlib
import time
import random

def HashFile(file):
    BLOCK_SIZE = 65536 # The size of each read from the file

    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file

    return file_hash.hexdigest()

def writeFile(c,file1,file2):
    f1 = open(file2, "w")
    f2 = open(file1, "r")
    lines = f2.readlines()
    f1.writelines(lines)
    f1.write(str("{}\tec\t100".format(c)))
    f1.close()
    f2.close() 

def ZeroPrefix(hash):
    i=0
    while len(hash)>i:
        if hash[i] == "0":
            i= i+1
        else:
            break
    return i

def cod():
    cod = ''.join(random.choices('0123456789abcdef', k=8))
    return cod

file1 = ".\SGSSI-23.CB.02.txt"
file2 = ".\SGSSI-23.CB.02.1.txt"
numzero = 0
hexcomb = "aaaaabab"
inicio = time.time()
truehash = 0
while(1):
    c = cod()
    writeFile(c,file1,file2)
    hash = HashFile(file2)
    
    newnum = ZeroPrefix(hash)
    if newnum>numzero:
        numzero = newnum
        hexcomb = c
        truehash = hash
    fin = time.time()
    if(fin-inicio>=60):
        print(truehash)
        print(hexcomb)
        print(numzero)
        break;
writeFile(hexcomb,file1,file2)
  


