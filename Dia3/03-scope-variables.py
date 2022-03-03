# variable global
nombre='Eduardo'

#si definimos una variable de manera global pero la queremos modificar dentro
# de una funcion no sera posible ya que al mimento de querer modificarla nos pedira que esa
# variable exista de manera aislada dentro de esa funcion
def saludar():
    nombre=nombre*2
    print(nombre)

saludar()

#ahora definimos una variable local 

def x():
    ganancia=0.15

x()
print(ganancia)