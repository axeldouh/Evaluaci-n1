import time
while True:
    print("**************************************************")
    print("*                menu de interacción             *")
    print("*                                                *")
    print("*   1) ingresar direcciones o urls a verificar   *")
    print("*   2) especificar cantidad de pings a realizar  *")
    print("**          3) cerrar el programa                *")
    print("*                                                *")
    print("**************************************************")
    selec= int(input("selecciona una opcion: "))
    if selec== 1:
        print("*****************************************")
        print("*   bienvenido al menu de direcciones   *")
        print("*****************************************")
        dir1=input(" a continuación ingrese un maximo de 4 direcciónes ip o url a revisar: ")
        opc1=int(input("¿desea agregar alguna dirección más? 1 para SI - 2 para NO: "))
        if opc1==1:
            dir2=input("por favor escriba siguiente dirección o url a revisar ")
            opc1=int(input("¿desea agregar alguna dirección más? 1 para SI - 2 para NO: "))
            dir3=input("por favor escriba siguiente dirección o url a revisar ")
            opc1=int(input("¿desea agregar alguna dirección más? 1 para SI - 2 para NO: "))
            dir4=input("por favor escriba siguiente dirección o url a revisar ")
            print("la(s) dirección(es) agrega(das) recientemente son:", dir1,"-" , dir2, "-" ,dir3, "-", dir4, "-")

        if opc1==2:
            print("la(s) dirección(es) agrega(das) recientemente son:", dir1)
            print("gracias por su preferencia, será redireccionado al menu principal")
            time.sleep(3)
    if selec ==2:
        print("********************************************")
        print("*   bienvenido al administrador de pings   *")
        print("********************************************")
        opc1==int(input("ingrese la cantidad de pings para las direcciones agregadas anteriormente:"))
        print("la cantidad de pings para las direcciones", dir1, "-" ,dir2, "-" ,dir3, "-" ,dir4,"es:", opc1 )
    if selec==3:
        print("cerrando programa, gracias por su preferencia")
        break