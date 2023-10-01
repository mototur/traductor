#Elaborar un programa que tenga un archivo de texto
#llamado EN-ES.txt el cual contiene las traducciones de palabras
#del ingles al espanol

DICCIONARIO = {
   "dog":"perro",
   "chair":"silla",
   "table":"mesa",
    "water":"agua",
    "purple":"morado"
}
 
opcion = 0
while opcion != 4:
    print("Elija una opcion \n")
    print("1. Traducir de ESP-ING \n 2.Traducir de ING-ESP \n 3. Agregar una palabra \n 4. Salir \n")
    opcion = int(input("Elija una opcion a realizar."))

    if (opcion == 1):
       palabra= input("Escriba la palabra a Traducir \n")
       if  DICCIONARIO.get (palabra)!= None:
            print (palabra , "->", DICCIONARIO.get(palabra))
    else:
        print("La palabra no existe")
