import re
import hashlib

import os

def comparar_archivos(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        if(lines2[-2] == "\n"):
            lines3 = lines2[0:-2]
        else:
            lines3 = lines2[0:-1]

        if lines1 != lines3:
           print("Los archivos no tienen el mismo inicio. No cumple la primera condicion")
           return False

        last_line = lines2[-1].strip()
        if re.match(r'^[0-9a-fA-F]{8}(\t?|\s+?)[0-9a-f]{2}(\t?|\s+?)100$', last_line):
            print("Cumple la primera condicion")
            return True
        else:
            print("No cumple la primera condicion")
            print(last_line)
            return False

def HashFile(file):
    BLOCK_SIZE = 65536 # The size of each read from the file

    file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file

    return file_hash.hexdigest()

def ZeroPrefix(hash):
    i=0
    while len(hash)>i:
        if hash[i] == "0":
            i= i+1
        else:
            break
    return i

relacion ={}
file1 = 'SGSSI-23.CB.03.txt'  
 
directorio = './candidatos' #Cambiar por la carpeta que tu tengas

archivos = os.listdir(directorio)

for archivo in archivos:
    file2 = os.path.join(directorio, archivo)
    print("\n"+str(archivo))
    hash = HashFile(file2)
    zeros = ZeroPrefix(hash)
    primera = comparar_archivos(file1, file2)
    if(zeros > 0):
        print("Cumple la segunda condicion")
    else:
        print("No cumple la segunda condicion")
        print(hash)
    if(primera and zeros >0):
        relacion[archivo]=zeros

ganador = max(relacion, key=relacion.get) #En caso de empate el primero que encuentra
max_zeros = relacion[ganador]
print(relacion)
print(str(ganador) + " " +str(max_zeros))