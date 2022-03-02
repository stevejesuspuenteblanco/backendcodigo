#IF - ELSE
#python al no utilizar las llaves para defini bloque de un
#comportamiento diferente tenemos que utilizar tabulaciones
#edad= input('Ingresa tu edad: ')
#se convierte a otro tipo de dato
edad= int(input('Ingresa tu edad: '))
if (edad>18): 
    print('La persona es mayor de edad')
    print('otra impresion')
#se usa cuando la primera condicion fallo y pasa a una segunda
elif edad>15:
    print('Puedes ingresar a la preparatoria')
elif edad>10:
    print('Puedes vacunarte con la vacuna')
else:
    print('La persona es menor de edad')
#siempre se debe respetar la tabulacion
#el else aveces es opcional no siempre se usa con un if

print ('Finalizo el programa :)')


#validar si un numero (ingresos de una persona )ingresado por teclado es :
# si es mayor a 500 indicar que el numero


