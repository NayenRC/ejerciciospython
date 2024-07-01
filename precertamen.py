# Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso: 
# Una empresa necesita desarrollar una aplicación que permita registrar los sueldos brutos de los trabajadores y calcular el líquido a 
# pagar. Para ello necesita que la aplicación cumpla con las siguientes funcionalidades 
# 1. Registrar trabajador 
# 2. Listar los todos los trabajadores 
# 3. Imprimir planilla de sueldos 
# 4. Salir del Programa
import os
os.system("cls")

lista = f"""{
"Trabajador":<20}{"Cargo":<20}{"Sueldo Bruto":<20}{"Salud Desc.":>20}{"Desc. AFP":>20}{"Líquido a pagar":>20}
{"Homero Simpson":<20}{"CEO":<20} {"1000000":<20} {"70000":>20}{"120000":>20} {"810000":>20}
"""

menu = '''
1. Registrar trabajador 
2. Listar los todos los trabajadores 
3. Imprimir planilla de sueldos 
4. Salir del Programa
'''
trabajadores = []
cargos =['ceo','desarrollador', 'analista']

def registrar():
    while True:
        try:
            nomApe = input("Ingresa tu nombre y apellido: ")
            print("Cargos disponibles: ", cargos)
            car = input("Ingresa cargo:").strip().lower() #.strip() elimina los espacios en los extremos . lower() pasa todo en minusculas
            sueldo = (int(input("Sueldo Bruto: ")))
            salud = round(sueldo * 0.07)
            afp = round(sueldo * 0.12)
            liquido = round(sueldo - salud - afp)
            if len(nomApe)>0 and len(car)>0 and sueldo>0 and car in cargos:
                trabajadores.append([nomApe,car,sueldo,afp,salud,liquido])
                input("Trabajador registrado con exito!")
                break
            else:
                input("Falta ingresar algo ")
        except:
            input("Expeción, al registrarse.")

def listar():
    salida = lista
    for i in trabajadores:
        salida += f"{i[0]:<20}" #nombre
        salida += f"{i[1]:<20}" #cargo
        salida += f"{i[2]:<20}"#sueldo
        salida += f"{i[3]:>20}" #descsalud
        salida += f"{i[4]:>20}" #desc AFP
        salida += f"{i[5]:>20}" #sueldo liquido
        salida +="\n"
    return salida

def listarXcargo(car):
    salida = lista
    for i in trabajadores:
        if car == i[1]:
            salida += f"{i[0]:<20}" #nombre
            salida += f"{i[1]:<20}" #cargo
            salida += f"{i[2]:<20}"#sueldo
            salida += f"{i[3]:>20}" #descsalud
            salida += f"{i[4]:>20}" #desc AFP
            salida += f"{i[5]:>20}" #sueldo liquido
            salida +="\n"
    return salida

def imprimir():
    car = input(f"Cargo {cargos}: ").strip().lower()
    if car in cargos:
        with open(car+".txt","w") as archivo:
            archivo.write(listarXcargo(car))
    else:
        input("cargo no valido")


while True:
    try:
        opc =int(input(menu))
        if opc == "4":
            break
        elif opc == 1:
            registrar()
        elif opc ==2:
            print(listar())
        elif opc == 3:
            imprimir()
    
    
    except Exception as e:
       input (f"Excepcion de menu principal: {str(e)}")