class IdLocal:
    def __init__(self,local,nro):
        self.nro=nro
        self.local=local
    def __repr__(self):
        return "[%s,%i]" % (self.local, self.nro)
    

listaLocal = [IdLocal("",0)] * 10

for f in range(0,6):
    listaLocal[f]= IdLocal("Sucursal", f * 2)

def alta ():
    for i in range (0,10):
        if listaLocal[i].local== "":
            local= (input("Ingrese Local:"))
            while True:
                try:
                    nro= int(input("Ingrese Nro Sucursal:"))
                    break
                except ValueError:
                    print("El dato ingresado no es un numero")
            listaLocal[i]=IdLocal(local,nro)
            return

f= alta()

def baja ():
    
    return
def mostrar ():
    
    return
