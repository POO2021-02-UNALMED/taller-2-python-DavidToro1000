class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self, color):
        if (color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color=color
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro(self, registro):
        self.registro=registro
    def asignarTipo(self, tipo):
        if (tipo=="gasolina" or tipo=="electrico"):
            self.tipo=tipo
class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        Auto.cantidadCreados=cantidadCreados
    def cantidadAsientos(self):
        cont=0
        for a in self.asientos:
            if (a!=None):
                cont+=1
        return(cont)
    def verificarIntegridad(self):
        if (self.motor.registro!=self.registro):
            return("Las piezas no son originales")
        for i in self.asientos:
            if (i.registro!=self.registro):
                return("Las piezas no son originales")
        return("Auto original")