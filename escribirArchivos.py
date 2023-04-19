def main():
    file = "archivo.txt"
    msg = "hola mundo\n"
    
    def escribir(file,msg):
      f = open(file,"w")
      f.write(msg)
      f.close()
      
    def leer(file):
        f = open(file,'r')
        contenido = f.read()
        print(contenido)
        f.close()
    
    escribir(file,msg) 
    leer(file)
    
if __name__ == "__main__":
    main()