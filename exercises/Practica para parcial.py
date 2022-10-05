class Vehiculo:
    def __init__ (self,patente:str, descripcion=''):
        self.patente = patente
        self.descripcion = descripcion
    
    def mostrar(self):
        print( f"Patente:{self.patente} {self.descripcion}" )

    def validarPatente(self):
        if len(self.patente) != 6 and len(self.patente) != 8:
            return False
        else:
            return True

asd = Vehiculo('123asd')

class Estadia:
    tarifa = 15
    def __init__(self, entrada, salida, Vehiculo):
        self.entrada = entrada
        self.salida = salida
        self.Vehiculo = Vehiculo
    
    def mostrar(self):
        self.Vehiculo.mostrar()
        print( f'Hora de entrada:{self.entrada}, Hora de salida:{self.salida}')
    
    def calcularTarifaTotal(self):
        if self.Vehiculo.validarPatente() == False or self.salida - self.entrada < 0:
            return print('Error no puede estar en esta estadia')
        
        return print ((self.salida - self.entrada) * self.tarifa)
        


asd2 = Estadia(16, 15, asd)
asd2.mostrar()
asd2.calcularTarifaTotal()

