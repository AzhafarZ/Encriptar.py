import string
import math
import random
import numpy as np

#Función generadora de claves de encriptación
def key():
    for i in range(len(vec)):
        for j in range(len(vec)):
            clave[i][j]=random.randint(0,25)                 #matriz de encriptación (números aleatorios)
    invalid=[2,4,6,8,10,12,13,14,16,18,20,22,24]             #números que no tienen inverso modular 26
    deter[0]=round(np.linalg.det(clave))%26
    if deter[0]%26==0 or invalid.count(deter[0]%26)>0:       #el determinante no puede ser múltiplo de 26
        key()
    deter[0]+=26*(deter[0]<0)                                #convertimos los negativos a positivos modular 26


#Función de encriptación
def Encryption():

    encriptado = np.matmul(vec,clave)                        #matriz por vector
    for i in range(len(encriptado)):
        encriptado[i] %= 26                                  #modulo 26 de cada elemento

    return encriptado

#Función de decriptación
def Decryption(F,C):
    Fil = 0
    Col = 0
    for i in range(len(clave)):           #fila
        if i == F:
            continue                      #No se incluyen los elementos de la fila actual en la submatriz
        Col = 0
        for j in range(len(clave)):       #columna
            if j == C:
                continue                  #No se incluyen los elementos de la columna actual en la submatriz
            sub[Fil][Col] = clave[i][j]
            Col +=  1
        Fil+=1
    inv[F][C]=round(np.linalg.det(sub))   #determinante de la submatriz
    inv[F][C]*=math.pow(-1,C+F+2)
    inv[F][C]=inv[F][C]%26
    inv[F][C]*=deter[1]
    inv[F][C]=inv[F][C]%26
    inv[F][C]+=26*(inv[F][C]<0)













#Variables
let = string.ascii_lowercase                               #letras de nuestro abecedario
cad = "hola "                                              #cadena a traducir
clave=[[3,3],[2,5]]                                        #clave de encriptación
vec=[7,4]                                                  #Números asociadas a cad
deter=[0,0]
sub = [[0]*(len(clave)-1) for i in range(len(clave)-1)]
encriptado = [0 for i in range(len(vec))]                  #palabra encriptada
inv =  [[0]*(len(clave)) for i in range(len(clave))]
nums = [x for x in range(len(let))]                        #numero asociado a cada letra
user = 0                                                   #eleccion del usuario

print("Qué desea hacer?")
print("1 para encriptar")
print("2 para decriptar")
print("3 para abrir la configuración")
print("4 para salir")
user = int(input())


if user==1:
  #encriptacion
  key()                                                     #generamos la clave
  deter[1]=1                                                #en esta sección calculamos
  while(not ((deter[0]*deter[1])-1)%26==0):                 #el inverso modular 26
    deter[1]+=1                                             #del determinante
  encriptado=Encryption()                                   #encriptamos el mensaje
  print("hola")

elif user==2:
  #decriptación
  for i in range(len(clave)):
    for j in range(len(clave)):
      Decryption(i,j)
  encriptado=np.matmul(encriptado,np.transpose(inv))
  for i in range(len(encriptado)):
    encriptado[i]%=26

elif user==3:
  #configuracion
  pass
elif user==4:
  exit()
