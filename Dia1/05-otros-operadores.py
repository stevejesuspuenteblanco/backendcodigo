#operadores de comparacion
numero1,numero2
#igual que
#mayor que | mayor igual que
#menor que | menor igual que
#diferente de

#Operadores de comparacion
#is
#is not
#sirve para ver si estan apuntando a la misma direccion de memoria
verduras=['apio','lechuga','zapallo']
verduras2=verduras
verduras3=['apio','lechuga','zapallo']
#['brocoli','espinaca','succhini']
#NOTA: las colecciones de datos son variables mutables
#(que cuando cambio su contenido este se vera reflejado
#en todas las copias de dicha variable)
verduras2[0]='peregil'
verduras[1]='manzana'
#el metodo copy() lo que hace es copia todo el contenido de la 
# variable pero se guardara en una nueva posicion d ememoria
verduras4=verduras.copy()
verduras4[0]='huatacay'
print(verduras2 is verduras)


#validar si el nombre del usuario es eduardo y que sea peruano o colombiano
nombre='eduardo',
nacionalidad='cubano'

print(nombre=='eduardo' and (nacionalidad == 'peruano' or nacionalidad == 'colombiano'))
