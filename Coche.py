class Coche():
    """se establece la clase coche"""
    def __init__(self, modelo, marca, color, tanque_full, tanque_actual, rendimiento, km_recorrido, velocidad, moverse):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.tanque_full = tanque_full
        self.tanque_actual = tanque_actual
        self.rendimiento = rendimiento
        self.km_recorrido = km_recorrido
        self.velocidad = velocidad
        self.moverse = False

    def cargar_gas(self, cantidad):
        if self.tanque_actual + cantidad > self.tanque_full:
            print("limite del tanque sobrepasado")
        elif self.tanque_actual + cantidad <= self.tanque_full:
                # self.tanque_actual += self.tanque_full
                self.tanque_actual += cantidad
                print("Gasolina en el tanque", self.tanque_actual)
        else:
            print("No se puede cargar esa catidad de gasonina")

    def encender(self):#el auto esta apagado o encendido
    # validar estado del tanque actual--------------------------------------
        if self.tanque_actual > 0:
            self.moverse = True
            print("El auto esta encendido")
        else:
            self.moverse = False
            print("el auto esta apagado")

    def apagar(self):
        if self.moverse == True:
            self.moverse = False
        print("El auto se detuvo")

    # def estado(self):#se toma el valor de encender y se aplica el estado del auto
    #     if (self.moverse):
    #         return "El auto esta encendido"
    #     else:
    #         return "El auto esta apagado"

    def avanzar(self):
        if self.moverse = True
        # Validar que el auto este encendido------------------

        if self.tanque_actual != 0:
            self.km_recorrido += 10 # Kilometros por hora
            self.velocidad += 10
            self.tanque_actual -=  self.km_recorrido / self.rendimiento
            self.tanque_full -=  self.tanque_actual / self.rendimiento
            print("Se recorrieron:", self.km_recorrido,"km")
        if self.tanque_actual <= 0:
            self.tanque_actual == 0
            print("Se ha terminado la gasolina")
    #
    # def detenerse(self):
    #     if self.velocidad > 0:
    #         self.velocidad == 10
    #         print("El coche se detuvo", self.velocidad)
    #     elif self.velocidad == 0:
    #         print("El coche no se mueve", self.velocidad)
    #


#numeros despues de rojo: tatanque_full, tanque_actual, rendimiento, km_recorrido, velocidad, moverse
# class_instance = Coche()
my_coche = Coche("2017","Hummer","Negro",80, 0, 8, 0, 0, False)
print("caracteristicas del coche:","\n modelo:",my_coche.modelo,"\n marca",my_coche.marca,"\n color",my_coche.color)
# my_coche.encender()
# print(my_coche.estado())
my_coche.encender()
my_coche.cargar_gas(10)
my_coche.avanzar()
my_coche.avanzar()
my_coche.avanzar()
my_coche.avanzar()
my_coche.avanzar()
my_coche.avanzar()
my_coche.avanzar()
my_coche.avanzar()
my_coche.apagar()
# my_coche.detenerse()
