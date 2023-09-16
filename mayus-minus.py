#Plantear una función que reciba un string en mayúsculas o minúsculas
#y retorne la cantidad de letras "a" o "A".

def contarletras_a(text):
    letras_a = text.count("a") + text.count("A")
    return letras_a

solicitud = input("Por favor, ingresa un texto: ")

cantidad = contarletras_a(solicitud)

print(f"La cantidad de letras (a) (mayúsculas y minúsculas) en el texto es: {cantidad}")
