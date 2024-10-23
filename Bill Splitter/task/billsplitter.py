# write your code here
import statistics
import random
media = 0
clave_aleatoria = None

#stage 1
#take names form user input & store in a dictionary

diccionario = {}
i = 0

print("Enter the number of friends joining (including you):")
x = int(input())

if x <= 0:
    print("No one is joining for the party")
    exit(1)


print("Enter the name of every friend (including you), each on a new line:")
#Contamos el n veces los amigos y los almacenamos en el diccionario
while i < x:
    names = input()
    i +=1

#Añadimos los nombres de los amigos al diccionario y los ponemos a 0
    diccionario[names] = 0
#print(diccionario)


#stage 2 afegir input per a la final bill
#split the total bill entre tots els amics
#round the split a 2 decimals
#actualitzar el diccionari amb els valors
#imprimir el diccionari actualitzat
print("Enter the total bill value:")
bill = int(input())


#stage3
#feature lucky one
print('Do you want to use the "who is lucky?" feature? write Yes/No: ')
opt = input()

if opt == "Yes":
    clave_aleatoria = random.choice(list(diccionario.keys()))
    print(f"{clave_aleatoria} is the lucky one!")

#actualizamos la clave aleatoria a 0
    diccionario[clave_aleatoria] = 0

    if x <= 5 and bill % 10 == 0:
        x_e = x-1
        media = bill // x_e  # División entera
    else:
        x_e = x-1
        media = bill / x_e

elif opt == "No":
    print("No one is going to be lucky")
    media = bill / x

media_r = round(media,2)
#print(media_r)
diccionario[names] = media_r

# Actualizar el diccionario con la media
for name in diccionario:
    if clave_aleatoria is None or name != clave_aleatoria:  # No actualizar el afortunado
        diccionario[name] = media_r

print(diccionario)


