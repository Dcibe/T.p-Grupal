##ARCHIVO
class IdLocal:
    def __init__(self,local,nro):
        self.nro=nro
        self.local=local
    def __repr__(self):
        return "[%s,%i]" % (self.local, self.nro)
    
##LISTA
listaLocal = [IdLocal("",0)] * 10   
for f in range(0,6):
    listaLocal[f]= IdLocal("Sucursal", f * 2)
    
##Oredena la lista
def ordenar ():
    for i in range(0,9):
        for j in range(0,9):
            if listaLocal[j].local.lower() > listaLocal[j + 1].local.lower():
                if listaLocal[j+1].local != "":
                    aux= listaLocal[j]
                    listaLocal[j]= listaLocal[j + 1]
                    listaLocal[j + 1]= aux
            elif listaLocal[j].local == "":
                    aux= listaLocal[j]
                    listaLocal[j]= listaLocal[j + 1]
                    listaLocal[j + 1]= aux
    return

##Alta a una nueva sucursal
def alta ():
    for i in range (0,10):
        if listaLocal[i].local== "":
            local= (input("Ingrese Local:"))
            while True:
                try:
                    nro= int(input("Ingrese Nro Sucursal:"))
                    ordenar()
                    break
                except ValueError:
                    print("El dato ingresado no es un numero")
            listaLocal[i]=IdLocal(local,nro)
            return

f= alta()
##Baja una sucursal
def baja ():
    while True:
        try:
            sucursal= int(input("Baja sucursal Nº: "))
            break
        except ValueError:
            print("El dato ingresado no es un numero")
    for i in range (0,10):
        if listaLocal[i].nro==sucursal:
            listaLocal[i]=IdLocal("",0)
            ordenar()
            return
    
    return print( "Numero de sucursal ingresado es invalido" )
b= baja()

##Interfaz Grafca
def mostrar ():
    
    return
