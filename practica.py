import os 
os.system("cls")

lista_productos =f'''   {"INVENTARIO DE PRODUCTOS DE BELLEZA "}
{"-"*80}
{"NOMBRE ":<20}{"PRECIO ":<20}{"STOCK ":>20}{"CATEGORIA":>20}
{"Crema corporal":<20}{"14.990":<20}{"5":>20}{"piel":>20}
{"-"*80}
'''


menu_Productos='''
1. Agregar Producto
2. Listar Producto
3. Buscar producto por categoria
4. Actualizar stock
5. Salir
'''
productos =[]
categoria = ["Piel","cabello", "maquillaje"]
def agregar_Prod():
    while True:
        try:
            nomProd = input("Ingrese el nombre del producto: ").strip().lower()
            valor = int(input("Ingrese valor del producto: "))
            stock = int(input("Ingrese cantidad de productos: "))
            print("Especifique su categoria ", categoria)
            categ = input("Aqui: ")

            if len(nomProd)>0 and valor>0 and stock>0 and categ in categoria:
                productos.append([nomProd, valor ,stock,categ])
                input("Producto agregado con éxito!")
                break
            else:
                input("Producto mal ingresado, vuelva a intentarlo")
        except Exception as e:
            input(f"Excepción de ingreso, vuelva a intentarlo {str(e)}")
    
    print(productos)

def listar():
    salida = lista_productos
    for i in productos:
        salida += f"{i[0]:<20}" # nombre del producto
        salida += f"{i[1]:<20}" # valor
        salida += f"{i[2]:>20}" # stock
        salida += f"{i[3]:>20}" # categoria
        salida += f"\n"
    return salida

def buscarXcat(categ):
    salida = lista_productos
    input(f"En que categoria desea buscar su producto")
    for i in productos:
        if categ  == i[3]:
            salida += f"{i[0]:<20}" # nombre del producto
            salida += f"{i[1]:<20}" # valor
            salida += f"{i[2]:>20}" # stoc
            salida += f"{i[3]:<20}" # categoria
            salida += f"\n"
    return salida

def actualizar_Stock():
    categ = input(f"Categoria del producto {categoria}: ").strip().lower()
    if categ in categoria:
        with open(categ+".txt","w") as archivo:
            archivo.write(buscarXcat(categ))

while True:
    try:
        opc = input(menu_Productos)
        if opc == "5":
            break
        elif opc == "1":
            agregar_Prod()
        elif opc == "2":
            print(listar())
        elif opc == "3":
            print(buscarXcat(categoria))
        elif opc == "4":
            actualizar_Stock()

    except Exception as e:
        input(f"Excepción de menú principal {str(e)}")