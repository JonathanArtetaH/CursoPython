from datetime import date

print('Hola desde la consola')

sum = 1 + 2 # 3
product = sum * 2
print(product)

# Tipos de datos
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

# Fechas
print(date.today())
print("Hoy es: " + str(date.today()))

#Ingresar texto por cosnola 
name = input("Introduzca su nombre ")
print("Saludos: " + name)


# Suma de dos numeros
print("Calculadora")
first_number = input("Ingrese primer número: ")
second_number = input("Ingrese segundo número: ")
print(int(first_number) + int(second_number))