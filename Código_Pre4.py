import string
import math
import random
import numpy as np

#Función generadora de claves de encriptación
def key():
    for i in range(2):
        for j in range(2):
            clave[i][j]=random.randint(0,25)                                    #matriz de encriptación (números aleatorios de 0 a 25)
    deter[0]=round(np.linalg.det(clave))%26
    if valida(deter[0])== bool():                                               #verificamos si el determinante de la clave es válido
      key()
    deter[0]+=26*(deter[0]<0)                                                   #convertimos los negativos a positivos modular 26

#función para determinar si una clave es válida
def valida(determinant):
  var = bool(1)                                                                 #variable booleana, la iniciamos como TRUE 
  invalid=[2,4,6,8,10,12,13,14,16,18,20,22,24]                                  #números que no tienen inverso modular 26
  if determinant%26==0 or invalid.count(deter[0]%26)>0:                         #el determinante no puede ser múltiplo de 26
   var = bool()                                                                 #var = FALSE (la clave NO es válida)
  else:
    var = bool(1)                                                               #var = TRUE (la clave es válida)
  return var


#Función de encriptación
def Encryption():

    encriptado.append(np.matmul(subpalabra,np.transpose(clave)))                #multiplicamos matriz por vector
    for i in range(len(encriptado)):
        encriptado[i] %= 26                                                     #modulo 26 de cada elemento de la clave

    return encriptado

#Función de decriptación
def Decryption(F,C):
    Fil = 0
    Col = 0
    for i in range(len(clave)):                                                 #fila
        if i == F:
            continue                                                            #No se incluyen los elementos de la fila actual en la submatriz
        Col = 0
        for j in range(len(clave)):                                             #columna
            if j == C:
                continue                                                        #No se incluyen los elementos de la columna actual en la submatriz
            sub[Fil][Col] = clave[i][j]
            Col +=  1
        Fil+=1
    inv[F][C]=round(np.linalg.det(sub))                                         #determinante de la submatriz
    inv[F][C]*=math.pow(-1,C+F+2)                                        
    inv[F][C]=inv[F][C]%26
    inv[F][C]*=deter[1]
    inv[F][C]=inv[F][C]%26
    inv[F][C]+=26*(inv[F][C]<0)

#función que asocia el abecedario con sus valores
def mensaje():
    mensaje=""                                                                  #en mensaje guardamos las letras
    for i in range(len(encriptado)):   
        for j in range(2):
            mensaje+=let[nums.index(encriptado[i][j])]                          # el indice de a corresponde a 0, b es 1...                 
    return mensaje


#función que calcula el inverso modular 26 de la clave
def detinv():
  deter[1]=1                                                                    #en esta sección calculamos
  while(not ((deter[0]*deter[1])-1)%26==0):                                     #el inverso modular 26
    deter[1]+=1                                                                 #del determinante de la clave
                                                                                #explicacion al final del codigo
#Variables
let = string.ascii_lowercase +" "                                               #letras de nuestro abecedario
cad = ""                                                                        #cadena a encriptar
longitud=0                                                                      #longitud de la cadena
clave=[[-1,0],[0,0]]                                                            #clave de encriptación
deter=[0,0]                                                                     #aqui guarmamos el determinante de la clave
                                                                                #y su inverso
subpalabra =[0,0]                                                               #variable de apoyo para encriptar y decriptar
sub = [[0]*(len(clave)-1) for i in range(len(clave)-1)]                         #subamtriz para calcular la clave inversa
encriptado = []                                                                 #palabra encriptada
inv =  [[0]*(len(clave)) for i in range(len(clave))]                            #inverso de la matriz clave
nums = [x for x in range(len(let))]                                             #numero asociado a cada letra
user = 0                                                                        #eleccion del usuario
errorletra = bool(0)                                                            #por si el usuario escribe una letra en el menú
print("BBVA BANCOMER".center(100))
print("SISTEMA DE COMUNICACIÓN CIFRADO".center(100))
while 1:
  print("----- ¿Qué desea hacer? ----- \n")
  print("[0] Ya cuento con mi clave BBVA \n")
  print("[1] Para escribir su mensaje \n")
  print("[2] Para encriptar (Si no cuenta con una BBVA clave, se le dará una) \n")
  print("[3] Para decriptar (Debe contar con una BBVA clave) \n")
  print("[4] Para abrir la configuración \n")
  print("[5] Para comunicarse con un técnico \n")
  print("[6] Para obtener el enlace de términos y condiciones \n")
  print("[7] Para salir \n")
  user = (input())
  if user.isnumeric()==0:
      print("Error, se ha escrito una caracter inválido, por favor introduce número del 1 al 7 sin decimales")
      continue
  #mensajes de error
  if int(user) >7:
      print("\n Error. Se escribió un numero mayor que 7, por favor introduce un numero del 1 al 7 sin decimales. \n")
  elif int(user)<0:
      print("\n Error. Se introdujo un número menor que 1, porpor favor introduce un numero del 1 al 7 sin decimales. \n")

  if int(user)==0:                                                              #si el usuario ya tiene clave
    for i in range(2):
        for j in range(2):
            clave[i][j]=(input("\n Introduzca un numero para la clave: \n"))
            if clave[i][j].isnumeric()==0:
                freno = bool(1)
                break
        if freno:
            break
    if freno:
        print("su clave NO puede contener números")
        continue
        print("\n Tu clave BBVA es la siguiente: \n ", clave)
    deter[0]=round(np.linalg.det(clave))%26                                     #calculamos el determinante de la clave
    if valida(deter[0])==bool(1):                                               #si la clave es válida
      detinv()                                                                  #podemos calcular su inverso
    else:
      print("BBVA clave no valida, use una proporcionada por el sistema de cifrado oficial")
      print("para cualquier inconveniente comuníquese con soporte técnico ")
      clave[1][0:2]=0                                                           #si la clave no es válida, reiniciamos la variable
      clave[2][0:2]=0                               

  if int(user) ==1:
    cad=input("\n Porfavor escriba su mensaje -SIN ESPACIOS- \n")               #leemos el mensaje del usuario
    freno = bool()                                                              #variable multiproposito
    for i in range(0,len(cad)):                                                 #revisamos elemento por elemento
        if cad[i].isnumeric()==1:                                               #si hay caracteres numericos
            freno = bool(1)                                                     #vamos a detener el programa
    if freno:
        print("Su mensaje NO puede contener números")
        print("Puede ingresar números como palabras, ejemplo: 'dos' \n")
        continue
    cad.lower()                                                                 #todo en minúscula
    longitud = len(cad)                                                         #longitud original del mensaje
    if len(cad)%2 != 0:                                                         #la longitud del mensaje debe ser par
      cad+=" "
    palabra=[0 for i in range(len(cad))]                                        #Números asociados a las letras de cad
    print()
#**********************************************************
    index = 0                                                                   #variable de indexazción
    for i in range(len(cad)):                                                   #Asignamos a cada letra de cad
      for j in range(len(let)):                                                 # un valor de acuerdo a la variable
        if cad[i]==let[j]:                                                      #nums
          palabra[index]=nums[j]                                                #ejemplo, "a" vale 0, "b" vale 1...
          index+=1
    print("\n Palabra ingresada: \n", palabra)
#**********************************************************
    print("\n ¿Su mensaje esta encriptado? \n")
    print(" [1] Si")
    print(" [2] No")
    user=int(input())
    if int(user)== 1:                                                                #si el mensaje del usuario ya está encriptado
      index = 0                                                                 #guardamos la el mensaje en la variable "encriptado"
      encriptado = [[0,0] for i in range(int(len(palabra)/2))]                  #separamos la palabra en pares, ejemplo "xc bv fr..." 
      for i in range(int(len(palabra)/2)):                                      #el vector encriptado se verá al final así:
        encriptado[i][0:2]=palabra[index:index+2]                               #[[5,12],[22,11],[34,56]] ESTO SOLO ES UN EJEMPLO
        index+=2

  elif int(user)==2:                                                                 #encriptacion
    if cad=="":
        print("Error, debes escribir un mensaje primero")
    else:
        if clave[0][0]==-1:                                                         #si el usuario no tiene clave, le damos una
            key()                                                                     #generamos la clave
            detinv()                                                                  #inverso del determinante de la clave
        print("\n Clave BBVA: \n", clave)
#**********************************************************
        index = 0
        for i in range(int(len(palabra)/2)):                                        #vamos a agrupar los caracteres en pares
            subpalabra[0:2]=palabra[index:index+2]                                    # y encriptarlos
            index+=2                                                                  #ejemplo: "help" primero encriptamos he
        encriptado=Encryption()                                                   #encriptamos el mensaje
        print("\n Palabra Encriptada \n", mensaje())
        print()  
#**********************************************************

  elif int(user)==3:                                                                 #decriptación
   if cad=="":
      print("\nError, debes escribir un mensaje primero\n")
   else:
          
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        for i in range(len(clave)):                                                 #calculamos el inverso de la clave
            for j in range(len(clave)):                                               #https://youtu.be/JK3ur6W4rvw?t=648
                Decryption(i,j)
        print()
        print("\n Clave BBVA de decriptacion: \n", inv)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#//////////////////////////////////////////////////////////

        for i in range(len(encriptado)):                                            #multiplicamos cada par de caracteres
            encriptado[i]=np.matmul(encriptado[i],inv)                                #por la clave inversa
        for i in range(len(encriptado)):
            for j in range(2):                                                        #modular 26 de cada elemento de
                encriptado[i]%=26                                                       #la palabra encriptada

#//////////////////////////////////////////////////////////
        print("\n Mensaje descifrado: \n",mensaje()[0:longitud])                    #usamos la longitud inicial del mensaje porque si la cadena
        print()                                                                     #tienen una longitud impar, debemos agregar " " a la cadena
        encriptado=[]                                                               #" " sería el caracter 26, pero 26 no exite en mod26
        cad=""                                                                      #se interpreta esto " "como 0 y por ende añada "a" al final
                                                                                #debemos remover el caracter "a"


  elif int(user)==4:                                                                 #configuración
    print("\n Borrar esta linea y agregar la configuración \n")
  elif int(user)==5:
    print ("\n Su mensaje ha sido enviado a un operador técnico. \n ¡Gracias por elegirnos!. \n")
  elif int(user)==6:
    print("\n https://www.bbva.mx/personas/faq/productos/tarjetas/promociones/terminos-puntos.html ")                                                                 #salir
    
  elif int(user)==7:
    exit() 


#inverso modular 26
#El inverso modular 26 de un numero n es p tal que np%26=1
#en el codigo tenenmos un while que va multiplicando el
#determinante por un factor que incrementa a razón de 1
#hasta encontrar el numero que satisfaga la propiedad
#del inverso modular
