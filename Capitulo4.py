##Capítulo 4: Trabajando con herencias
#Las herencias pueden ser una adición fresca a su código que puede ahorrar
#mucho tiempo al escribir él hacia fuera también. Esto es algo que prevalece
#dentro de los lenguajes OOP, ya que le ayudan a reutilizar código y hacer
#ajustes a la nueva versión de la misma, ahorrando mucho tiempo y haciendo
#que la escritura de código sea más eficiente que antes. También ayuda a hacer
#que el código sea más fácil de leer, ya que no tendrá que volver a escribir
#tantas cosas a largo plazo y puede mantener todo en una línea según lo
#necesite.
#Básicamente, una herencia es una que tomar una parte de su código y luego
#hacer una segunda clase con él. La segunda clase tendrá la misma información
#que la primera clase, pero luego puede hacer ajustes y cambiarla tanto como
#desee sin tener ningún efecto en lo que sucede con la primera clase (no se
#realizarán cambios en esa primera clase Incluso cuando usted hace cambios a
#la segunda). Usted puede hacer una línea de herencias, haciendo algunos
#ajustes según lo necesite dependiendo de lo que le gustaría que suceda dentro
#del código. A medida que hagas más herencias en el código, empezarás a ver
#cuánto tiempo puede ahorrar y cuánto más limpio y más agradable será tu código
#Example of inheritance
#base class
class Student(object):
    def__init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
#Graduate class inherits or derived from Student class
class GraduateStudent(Student):
    def__init__(self, name, rollno, graduate):
    Student__init__(self, name, rollno)
        self.graduate = graduate
        def DisplayGraduateStudent(self):
            print”Student Name:”, self.name)
            print(“Student Rollno:”, self.rollno)
            print(“Study Group:”, self.graduate)

#Post Graduate class inherits from Student class
class PostGraduate(Student):
    def__init__(self, name, rollno, postgrad):
    Student__init__(self, name, rollno)
        self.postgrad = postgrad
    def DisplayPostGraduateStudent(self):
        print(“Student Name:”, self.name)
        print(“Student Rollno:”, self.rollno)
        print(“Study Group:”, self.postgrad)

#instantiate from Graduate and PostGraduate classes
objGradStudent = GraduateStudent(“Mainu”, 1, “MS-Mathematics”)
objPostGradStudent = PostGraduate(“Shainu”, 2, “MS-CS”)
objPostGradStudent.DisplayPostGraduateStudent()

#When you type this into your interpreter, you are going to get the results:
(‘Student Name:’, ‘Mainu’)
(‘Student Rollno:’, 1)
(‘Student Group:’, ‘MSC-Mathematics’)
(‘Student Name:’, ‘Shainu’)
(‘Student Rollno:’, 2)
(‘Student Group:’, ‘MSC-CS’)

#¿Por qué anularía la clase base?
#Hay algunas veces mientras trabaja en su código cuando es importante anular
#su clase base para convertirlo en una nueva clase derivada. Esto significa que
#usted va a mirar la clase base y reemplazar el comportamiento de la misma
#para que ahora esté presente dentro de la clase de hijo que está intentando
#crear.

#Sobrecarga
#Otra cosa que usted puede aprender a hacer cuando se trabaja en la herencia es
#un proceso llamado sobrecarga. Cuando se pasa y se sobrecarga, se está
#tomando un identificador y se utiliza para definir más de un método;Por lo
#general será sólo dos métodos dentro de la clase, pero puede ser más. Los dos
#métodos tienen que estar en la misma clase, pero tendrían diferentes
#parámetros que se asocian con él. Este método se va a utilizar la mayoría de
#las veces cuando se desea que los métodos para ejecutar el mismo tipo de
#tarea, pero que le gustaría contar con su trabajo con diferentes parámetros.

#Trabajar con la herencia múltiple
#Otra de las características que son capaces de trabajar con la hora en Python
#es una cosa que se conoce como herencia múltiple. Esto es similar a una
#herencia normal, pero vamos a ir un paso más allá. Con este tipo de herencia,
#usted será capaz de tomar una clase y darle dos o más clases padre. Esto
#realmente puede ayudar a hacer crecer su código sin tener un lío de códigos
#por todo el lugar y tener que repetir a sí mismo dentro del código todo el
#tiempo.
#¿Qué pasará cuando se está trabajando en la herencia múltiple, que está
#creando una nueva clase, clase 3, que se deriva de las características que ha
#tenido en Clase 2, Clase 2 y luego se creó a partir de las características de
#Clase 1. Class3 va a tener algunas características que vinieron de Clase 2,
#pero también debe tener algunas características de Clase 1 en ella
#también. Cada capa se tienen algunas de las características de la anterior, pero
#que son capaces de hacer algunos cambios para ayudar a que el código
#funcione de una manera nueva a su gusto dentro de Python.
