#Trabajo con clases y objetos
#Los objetos y las clases son importantes cuando se trata de trabajar en el
#lenguaje Python. Los objetos ayudan a definir las diferentes partes del código
#y mantenerlos todos organizados y fáciles de entender, mientras que las clases
#van a funcionar como los contenedores de los objetos para que los objetos que
#son similares entre sí para ayudar a que el código funcione mejor.
#CLASE ES EL CONTENEDOR DE OBJETOS
#OBJETO ES LA PARTE QUE CONTIENE EL CÓDIGO FUNCIONAL

#¿Cómo puedo crear una nueva clase?
#Así que lo primero que debemos ver es cómo crear una clase dentro de Python
#y por suerte este es un proceso bastante simple para trabajar. Al trabajar en
#una declaración para una clase, también debe tomar el tiempo para crear una
#nueva definición. Debe colocar el nombre de la clase justo después de su
#palabra clave y luego su superclase estará dentro del paréntesis.
class Vehicle(object):
#constructor
def_init_(self, steering, wheels, clutch, breaks, gears):
    self._steering = steering
    self._wheels = wheels
    self._clutch = clutch
    self._breaks =breaks
    self._gears = gears
#destructor
def_del_(self):
    print(“This is destructor….”)
#member functions or methods
def Display_Vehicle(self):
    print(‘Steering:’, self._steering)
    print(‘Wheels:’, self._wheels)
    print(‘Clutch:’, self._clutch)
    print(‘Breaks:’, self._breaks)
    print(‘Gears:’, self._gears)
#instantiate a vehicle option
myGenericVehicle = Vehicle(‘Power Steering’, 4, ‘Super Clutch’, ‘Disk Breaks’, 5)
myGenericVehicle.Display_Vehicle()

#Definición de clase
#Necesitará la definición de clase y la instanciación de objeto como parte de la
#sintaxis de la clase. Estos ayudan a decirle a su compilador lo que está
#pasando y le da los comandos que son necesarios
#invocar la definición de clase dentro de su código, sólo tendría que agregar la
#función object.method () o el objeto.attributo para ayudar a hacer esto.
object.method()

#Atributos especiales para agregar en el código
#Hay algunos atributos especiales que se reconocen justo dentro del código de
#Python. Es una buena idea aprender de qué se trata esto porque ayudan a que
#sea más fácil trabajar en cualquier código que desee. También es bueno tener
#la tranquilidad de saber que el intérprete verá estos atributos y sabrá cómo
#usarlos dentro del código. Algunos de los atributos que son importantes
#cuando se trabaja en Python son:
__bases__: se considera una tupla que contiene cualquiera de las superclases
__module__: aquí es donde vas a encontrar el nombre del módulo y también
mantendrá tus clases.
__name__: se mantendrá en el nombre de la clase.
__doc__: aquí es donde vas a encontrar la cadena de referencia dentro del
documento para tu clase.
__dict__: esta va a ser la variable para el dict. Dentro del nombre de la clase.

#Accediendo a los miembros de tu clase
#Hay algunas opciones diferentes que son capaces de utilizar cuando se trata de
#acceder a los miembros que están dentro de las clases que está utilizando. Y
#mientras que todos van a trabajar, ir con el método de acceso es visto como el
#mejor porque le permite encapsular, o proporcionar la información, dentro de
#la sintaxis para facilitar las cosas y para asegurarse de que usted es capaz de
#leer el Código fácil más adelante. Un buen ejemplo de cómo esto funciona
#incluye:
class Cat(object)
    itsAge = None
    itsWeight = None
    itsName = None
    #set accessor function use to assign values to the fields or member vars
def setItsAge(self, itsAge):
    self.itsAge = itsAge
def setItsWeight(self, itsWeight):
    #get accessor function use to return the values from a field
def getItsAge(self):
    return self.itsAge
def getItsWeight(self):
    return self.itsWeight
def getItsName(self):
    return self.itsName

objFrisky = Cat()
objFrisky.setItsAge(5)
objFrisky.setItsWeight(10)
objFrisky.setItsName(“Frisky”)

print(“Cats Name is:”, objFrisky.getItsname())
print(“Its age is:”, objFrisky.getItsAge())
print(“Its weight is:”, objFrisky.getItsName())

