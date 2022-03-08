class Animal:
    nombre =''
    sexo=''
    patas=0
    #metodo constructor: este metodo se llamara cuando vayamoa a crear una nueva instancia
    # de la clase
    def __init__(self, nombre, sexo, nro_patas):
        nombre=nombre
        sexo=sexo
        patas=nro_patas

    def descripcion(self):
        return 'Yo soy un {}, soy {}, y tengo {} patas'.format(
            self.nombre, 
            self.sexo, 
            self.patas
            )

foca=Animal('Foca','M',2)
caballo=Animal('Caballo','M',4)
gato=Animal('Gato','F',4)

print(foca.descripcion())
print(caballo.descripcion())
print(gato.descripcion())