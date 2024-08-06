nombre_archivo=input("nombre archivo:")
path='C:\\Users\ivana_000\Desktop\\'
text_file=open(path+nombre_archivo+'.txt','r')
print(text_file.read())
text_file.close()
