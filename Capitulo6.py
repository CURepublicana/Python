#Capítulo 6: La estructura de control Decisión en Python
#Si lógico
Edad = int (entrada ("Ingrese su edad:"))
age = int(input("Enter your age:"))
if (age <=18):
    print("You are not eligible for voting, try next election!")
    print("Program ends")
#vamos a mantenerlo bastante simple y comenzar
#con la sentencia if. Esta es la forma más simple de las estructuras de control
#de la decisión, ya que sólo va a funcionar si el usuario pone en la entrada de la
#derecha, pero si el usuario coloca en la entrada incorrecta en función de sus
#condiciones, nada se mostrarán en el programa. Existen limitaciones para el
#uso de este, pero es un buen lugar para empezar a ver cómo funcionan. A
#continuación se muestra un ejemplo que se puede practicar en la primera vez
#que aprender a hacer las sentencias if.

edad = int (entrada ( "Ingrese su edad:"))
age = int(input("Enter your age:"))
if (age <=18):
    print("You are not eligible for voting, try next election!")
else
    print("Congratulations! You are eligible to vote. Check out your local
            polling station to find out more information!)
    print("Program ends")

#Utilizando las sentencias elif
#Por encima se trabajó en el caso y si ... else, los cuales pueden ser muy
#agradable si se está trabajando en la adición de algunos más opciones a su
#código y aceptar la respuesta de una manera determinada en base a lo que el
#usuario da a usted 

Print("Let’s enjoy a Pizza! Ok, let’s go inside Pizzahut!")
print("Waiter, Please select Pizza of your choice from the menu")
pizzachoice = int(input("Please enter your choice of Pizza:"))
if pizzachoice == 1:
    print(‘I want to enjoy a pizza napoletana’)
elif pizzachoice == 2:
    print(‘I want to enjoy a pizza rustica’)
elif pizzachoice == 3:
    print(‘I want to enjoy a pizza capricciosa’)
else:
    print("Sorry, I do not want any of the listed pizza’s, please bring a Coca Cola for me.")

