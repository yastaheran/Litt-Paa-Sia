"""
It is important that the name of the names in syntax- and theme-file are in
the same order
"""
#!/usr/bin/env python
import sys
import re
    
def main(syntax, theme, sourcefile):
    #m = re.search(?P<group_name>…)
    #m.groupdict()

    dictcolor = {}
    dictsyntax = {}

    endcode = "\033[0m"
   
# Syntax, saves the syntax info in a dictionary
    for line in syntax:
        l = line.split(" : ")
        dictsyntax[l[1]] = l[0]
# Colors, saves the color info in a dictionary
    for line in theme:
        l = line.split(" : ")
        dictcolor[l[0]] = '\033[' + l[1]
# The source file, colors the source file by reading each line in the file
# --> split line
# --> look for a match in the syntax dictionary
# if match --> color it
    for line in sourcefile:
        l = line.split('')
        for l in line:
            for key1, key2 in zip(dictsyntax, dictcolor):
                match = re.match(dictsyntax[key1], l)
                if match:
                    color = dictcolor[key2]
                    print(color + line + endcode)
                else:
                    print(line)
                
if __name__ == "__main__":
   main(sys.argv[1], sys.argv[2], sys.argv[3])