
monto= int(input('Ingresa tu monto: '))

if (monto>500): 
    print('Usted no es beneficiario del bono yanapay')
elif (monto>250 or monto<=500):
    print('Usted si es beneficiario del bono')
else:
    print('Usted si es beneficiario del bono yanapay ademas de un balon de gas')
