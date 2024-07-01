titulo = f"""{"LISTADO DE CLIENTE"}
{"-" * 80}
{"CLIENTE":<20}{"DIRECCION":<20}{"SECTOR":<10}{"CIL.5":>10}{"CIL.15":>10}{"CIL.45":>10}  
{"-" * 80}
"""

menu = """
1. Registrar
2. Listar
3. Imprimir
4. Salir del Programa
"""
pedidos = []
sectores = ["centro", "colina","industrias"]

#:<20 # en que lado lo muestra (direccion), alinear 
  
def resgistrar():
    while True:
        try:
            clientenom = input("ingrese Nombre y Apellido").strip() # borrar los espacios de los costados
            direccion = input("ingrese direccion").strip()
            sector = input(f"sector{sectores}:").strip().lower()
            cil05 = int(input("cuantos cilindros de 5 Kgs: "))
            cil15 = int(input("cuantos cilindros de 15 Kgs: "))
            cil45 = int(input("cuantos cilindros de 45 Kgs: "))
            
            if len(clientenom)>0 and len(direccion)>0 and sector in sectores and cil05 >=0 and cil15>=0 and cil45>=0:
                pedidos.append([clientenom,direccion,sector,cil05,cil15,cil45])
                input("pedido agregado con exito")
                break
        except Exception as e:
            input(f"excepcion de menu: {str(e)}")
            
    
def listartodos(): # retorna todos los pedidos
    salida = titulo
    for p in pedidos:
        salida += f"{p[0]:<20}" # cliente
        salida += f"{p[1]:<20}" # direccion
        salida += f"{p[2]:<10}" # sector
        salida += f"{p[3]:>10}" # cil 5
        salida += f"{p[4]:>10}" # cil 15
        salida += f"{p[5]:>10}" # cil 45
        salida += "\n"
    return salida
        

def listarxsector(sector): # retorna los pedidos filtrados x sector
    salida = titulo
    for p in pedidos: # si sector recibido es igual al sector del pedido
        if sector == p[2]:
            salida += f"{p[0]:<20}" # cliente
            salida += f"{p[1]:<20}" # direccion
            salida += f"{p[2]:<10}" # sector
            salida += f"{p[3]:>10}" # cil 5
            salida += f"{p[4]:>10}" # cil 15
            salida += f"{p[5]:>10}" # cil 45
            salida += "\n"
    return salida

def imprimirhojaderuta(): # a generar un archivo
    sector = input(f"sector {sectores}: ").strip().lower()
    if sector in sectores:
        with open(sector+".txt","w") as archivo:
            archivo.write(listarxsector(sector))
    else:
        input("sector no valido")


while True:
    try:
        resp = input(menu)
        if resp == "4":
            break
        elif resp == "1":
            resgistrar()
        elif resp == "2":
            print(listartodos()) , #necesario el print
        elif resp == "3":
            imprimirhojaderuta()
        else:
            input("opcion incorrecta")

    except Exception as e:
        input(f"excepcion de menu: {str(e)}")titulo = f"""{"LISTADO DE CLIENTE"}
{"-" * 80}
{"CLIENTE":<20}{"DIRECCION":<20}{"SECTOR":<10}{"CIL.5":>10}{"CIL.15":>10}{"CIL.45":>10}  
{"-" * 80}
"""

menu = """
1. Registrar
2. Listar
3. Imprimir
4. Salir del Programa
"""
pedidos = []
sectores = ["centro", "colina","industrias"]

#:<20 # en que lado lo muestra (direccion), alinear 
  
def resgistrar():
    while True:
        try:
            clientenom = input("ingrese Nombre y Apellido").strip() # borrar los espacios de los costados
            direccion = input("ingrese direccion").strip()
            sector = input(f"sector{sectores}:").strip().lower()
            cil05 = int(input("cuantos cilindros de 5 Kgs: "))
            cil15 = int(input("cuantos cilindros de 15 Kgs: "))
            cil45 = int(input("cuantos cilindros de 45 Kgs: "))
            
            if len(clientenom)>0 and len(direccion)>0 and sector in sectores and cil05 >=0 and cil15>=0 and cil45>=0:
                pedidos.append([clientenom,direccion,sector,cil05,cil15,cil45])
                input("pedido agregado con exito")
                break
        except Exception as e:
            input(f"excepcion de menu: {str(e)}")
            
    
def listartodos(): # retorna todos los pedidos
    salida = titulo
    for p in pedidos:
        salida += f"{p[0]:<20}" # cliente
        salida += f"{p[1]:<20}" # direccion
        salida += f"{p[2]:<10}" # sector
        salida += f"{p[3]:>10}" # cil 5
        salida += f"{p[4]:>10}" # cil 15
        salida += f"{p[5]:>10}" # cil 45
        salida += "\n"
    return salida
        

def listarxsector(sector): # retorna los pedidos filtrados x sector
    salida = titulo
    for p in pedidos: # si sector recibido es igual al sector del pedido
        if sector == p[2]:
            salida += f"{p[0]:<20}" # cliente
            salida += f"{p[1]:<20}" # direccion
            salida += f"{p[2]:<10}" # sector
            salida += f"{p[3]:>10}" # cil 5
            salida += f"{p[4]:>10}" # cil 15
            salida += f"{p[5]:>10}" # cil 45
            salida += "\n"
    return salida

def imprimirhojaderuta(): # a generar un archivo
    sector = input(f"sector {sectores}: ").strip().lower()
    if sector in sectores:
        with open(sector+".txt","w") as archivo:
            archivo.write(listarxsector(sector))
    else:
        input("sector no valido")


while True:
    try:
        resp = input(menu)
        if resp == "4":
            break
        elif resp == "1":
            resgistrar()
        elif resp == "2":
            print(listartodos()) , #necesario el print
        elif resp == "3":
            imprimirhojaderuta()
        else:
            input("opcion incorrecta")

    except Exception as e:
        input(f"excepcion de menu: {str(e)}")