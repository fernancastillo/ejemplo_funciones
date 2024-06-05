def sumar_2_numeros():
    num1 = validar_numero()
    num2 = validar_numero()
    total= num1+num2
    print("El total de la sumas es:", total)
def restar_2_numeros(p_num1:float,p_num2:float):
    total=p_num1-p_num2
    print("El total de la resta es: ", total)
def multiplicar_2_numeros():
    num1=validar_numero()
    num2=validar_numero()
    total=num1*num2
    return total
def dividir_dos_numeros(p_num1:int, p_num2:int):
    total=p_num1/p_num2
    return total
def validar_numero():
    while True:
        try:
            num=float(input("Ingrese número: "))
            break
        except:
            print("ERROR! Debe ingresar un número entero!")
    return num
def menu():
    print("MENÚ")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
def validar_opciones(opciones):
    while True:
        try:
            opc=int(input("Ingrese opción: "))
            if opc in opciones:
                break
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("Error! Debe ingresar un número entero!")
    return opc