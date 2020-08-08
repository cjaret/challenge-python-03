# Resolve the problem!!
import re
import os
import sys

def run():

    minusculas = []
    
    with open(os.path.join(sys.path[0], "encoded.txt"), 'r', encoding="utf-8") as f:
        
        for line in f.readlines():
            minusculas.append(re.findall("[a-z]", line))
        
        clave = ''.join(map(str, minusculas))
        clave = re.findall("[a-z]", line)
        clave = ''.join(clave)

        print(clave)


if __name__ == '__main__':
    run()
