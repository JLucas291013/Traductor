import random 

password = "" 


contra_usuario =("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

longitud = (random.randint(1,63))

peticion_de_contra = int(input("cuantas digitos va a tener tu contraseña"))

for i in range (peticion_de_contra):
    password += random.choice(contra_usuario)





if peticion_de_contra  > 63:
    print("no puedes tener tantos digitos")


else:
    print("tu contraseña es:",password)

    





















