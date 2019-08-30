class IdLocal:
    def __init__(self,local,nro):
        self.nro=nro
        self.local=local
    def __repr__(self):
        return "[%s,%i]" % (self.local, self.nro)
    

listaLocal = [IdLocal("",0)] * 10

def alta ():
    for i in range (0,10):
        if listaLocal[i].local== "":
            local= int (input("Ingrese Local:"))
            nro= (input("Ingrese Nro Sucursal:"))
            listaLocal[i]=IdLocal(nro,local)
            return

f= alta()

def baja ():
    
    return
def mostrar ():
    
    return
