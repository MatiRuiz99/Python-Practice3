class Vehiculo:
    def __init__ (self,patente:str, descripcion=''):
        self.patente = patente
        self.descripcion = descripcion
    
    def mostrar(self):
        print( f"Patente:{self.patente} {self.descripcion}" )

    def validarPatente(self):
        if len(self.patente) != 6 or len(self.patente) != 8:
            print('Patente invalida')
        else:
            print('Patente valida')

asd = Vehiculo('123asd')
asd.validarPatente()
asd.mostrar()

class Estadia(Vehiculo):
    def __init__(self, entrada, salida):
        self.entrada = entrada
        self.salida = salida
    
    def mostrar(self):
        Vehiculo.mostrar
        print( f'Hora de entrada:{self.entrada}, Hora de salida:{self.salida}')


asd2 = Vehiculo('123asd', 'desc', 13, 15)

