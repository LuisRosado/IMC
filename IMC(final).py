#IMC 3

A = int(input('Ingrese su estatura (en centimetros) : '))

B = int(input('Ingrese su peso (en kilogramos) : '))

C = (B/(A*A))*10000

print("Tu IMC es: ",C)

if ((C <=25) & (C >=18)):

    print('Esta en su peso ideal')
else:
    if(C<18):
        print('Usted tiene bajo peso')
    if(C>25):
        print('Usted tiene sobrepeso')
