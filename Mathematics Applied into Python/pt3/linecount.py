def linecount(filename):
    file_text=open(filename,'r')
    lines_cont=0
    char_cont=0
    for eachline in file_text:
        lines_cont=lines_cont+1
        char_cont=char_cont+len(eachline)
    file_text.close()
    return lines_cont, char_cont
#programa principal
lineas,caracteres= linecount('cocodrile.txt')
print(lineas,'',caracteres)
