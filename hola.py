#import funciones as fn
from funciones import *
menu()
opc=validar_opciones((1,2,3,4))
if opc==1:
   sumar_2_numeros()
elif opc==2:
    num1=validar_numero()
    num2=validar_numero()
    restar_2_numeros(num1,num2)
elif opc==3:
    print("Super total de la multiplicación:",multiplicar_2_numeros())
else:
    num1=int(input("Ingrese primer número: "))
    num2=int(input("Ingrese segundo número: "))
    total=dividir_dos_numeros(num1,num2)
    lista=[]
    lista.append(total)
    print(lista)