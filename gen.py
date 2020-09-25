import json


class Producto:
    def __init__(self, nombre: str, precio: float, foto: str, calificacion: float, descripcion: str, categoria: str):
        self.nombre = nombre
        self.precio = precio
        self.foto = foto
        self.calificacion = calificacion
        self.descripcion = descripcion
        self.categoria = categoria


class Cliente:
    def __init__(self, nombre: str, correo: str, contrasena: str, ciudad: str, foto: str, carrito: list, mascotas: list):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.ciudad = ciudad
        self.foto = foto
        self.carrito = carrito
        self.mascotas = mascotas


class Paseador:
    def __init__(self, nombre: str, valoracion: float, descripcion: str, ciudad: str, foto: str, animales: list):
        self.nombre = nombre
        self.valoracion = valoracion
        self.descripcion = descripcion
        self.ciudad = ciudad
        self.foto = foto
        self.animales = animales


class Animal:
    def __init__(self, nombre: str, foto: str, productos: list):
        self.nombre = nombre
        self.foto = foto
        self.productos = productos


productos = []
# Perros
# Salud y Bienestar
productos.append(Producto("NexGard Antipulgas", 34320, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/1/5151151105110440002_2.jpg',
                          4.5, "Antipulgas para perros de 4.1 a 10 Kg.", "Salud y bienestar"))
productos.append(Producto("Galgocal Antiparasitario", 2490, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/1/5151151105110220004.jpg',
                          4, "Galgocal Antiparasitario Interno para Perros y Gatos. 200. 2 Tabletas.", "Salud y bienestar"))
productos.append(Producto("Bravecto Antiparasitario", 89100, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/1/5151151105110340004_3.jpg",
                          4, "Bravecto Antiparasitario. Perros de 20 a 40 Kg. Tableta 1000 mg.", "Salud y bienestar"))
productos.append(Producto("NexGard Spectra Antipulgas", 62423, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/1/5151151105110480005_1.jpg",
                          4.6, "NexGard Spectra Antipulgas para Perros de 30.1 a 60 Kg.", "Salud y bienestar"))
productos.append(Producto("Canisan D Antihelmintico", 8016, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/1/5151151105110500001_1_2.jpg',
                          4.3, "Canisan D Antihelmintico para Perros y Gatos. 2.5 ml.", "Salud y bienestar"))
productos.append(Producto("Suplemento Alimenticio Pelo y Derme", 87045, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/8/5858658605860000123_1_-min.jpg',
                          4.3, "Suplemento Alimenticio Pelo y Derme 1500 por 60 tabletas", "Salud y bienestar"))
# Comida
productos.append(Producto("Chunky Perros Adultos", 119079, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111100173.jpg",
                          4.1, "Chunky Perros Adultos. Pollo. 25 kg.", "Comida"))
productos.append(Producto("Nutra-Nuggets Cachorros Pollo y Maiz", 132024, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111100380_ed-final-min.jpg',
                          4.4, "Nutra-Nuggets Cachorros Pollo y Maiz 7.5 k", "Comida"))
productos.append(Producto("Max Professional Line", 91180, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111101261-min.jpg",
                          4.3, "Max Professional Line. Perros Adultos Razas Pequeñas. Pollo y Arroz. 8 Kg.", "Comida"))
productos.append(Producto("PRO PAC Ultimates. Sin Granos.", 71479, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111101651.jpg",
                          4.2, "PRO PAC Ultimates. Sin Granos. Cordero y Papas. 2.5Kg.", "Comida"))
productos.append(Producto("Nutrion Concentrado", 90795, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111100404_ed.jpg",
                          4.5, "Nutrion Concentrado Perros Adultos. 30 Kg.", "Comida"))
productos.append(Producto("Hills Prescription Diet", 513201, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111102436-min.jpg",
                          4.8, "Hills Prescription Diet Perros Metabolic + Mobility 24 Lb", "Comida"))
# Juguetes
productos.append(Producto("Pelota con sonido", 23810, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/3/3/333310772_2.jpg",
                          4.2, "Pelota con sonido ratón recargable con snaks.", "Juguetes"))
productos.append(Producto("Pelota Luminosa", 28753, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/3/3/333310613.jpg",
                          4.4, "Pelota Luminosa para Perro Max Glow Erratic", "Juguetes"))
productos.append(Producto("Hueso con sonido", 9996, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/3/5/353500148_1.jpg",
                          4.3, "Hueso con sonido pequeno para perros", "Juguetes"))
p_perros = [json.dumps(o.__dict__) for o in productos]
productos.clear()

# Gatos
# Salud y Bienestar
productos.append(Producto("Advocate Antiparasitario", 30020, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/1/5151251215121170005_3.jpg',
                          4.8, "Advocate Antiparasitario. Gatos de hasta 4 Kg.", "Salud y bienestar"))
productos.append(Producto("Comfortis Antipulgas", 27712, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/1/5151151105110410004_ed.jpg',
                          4.2, "Comfortis Antipulgas para Perros y Gatos. 270 mg. (De 4.6 a 9 Kg)", "Salud y bienestar"))
productos.append(Producto("Antiparasitario Drontal", 16972, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/1/5151151105110110004.jpg',
                          4.7, "Antiparasitario Drontal para gatos.", "Salud y bienestar"))
productos.append(Producto("Mirrapel Suplemento Nutricional", 17896, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/8/5858658605860000108.jpg",
                          4.3, "Mirrapel Suplemento Nutricional para Perros y Gatos. Oleoso. 120 ml.", "Salud y bienestar"))
productos.append(Producto("Bonavit", 10928, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/5/8/5858658605860000009.jpg",
                          4.8, "Bonavit suspension 120Ml.", "Salud y bienestar"))
# Comida
productos.append(Producto("Agility Gold Gatos", 109762, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111110730.jpg',
                          4.2, "Agility Gold Gatos. Sin Granos. 7 Kg.", "Comida"))
productos.append(Producto("Nutra-Nuggets", 115672, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111110143_ed-final-min_2.jpg',
                          4.5, "Nutra-Nuggets Formula de Mantenimiento para Gatos 7.5 k", "Comida"))
productos.append(Producto("Taste of the Wild Gatos.", 71128, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111111027_ed-min_1.jpg',
                          4, "Taste of the Wild® Gatos. Rocky Mountain. Venado y Salmon. 5 Lb.", "Comida"))
productos.append(Producto("Max cat gatos adultos", 106313, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111111046.jpg',
                          4.2, "Max cat gatos adultos pollo y arroz 10,1 Kg", "Comida"))
productos.append(Producto("Cat Chow Concentrado", 99704, 'https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111110020.jpg',
                          4.1, "Cat Chow Concentrado para Gatitos. 8 Kg.", "Comida"))
# Juguetes
productos.append(Producto("Juguete de ratón blanco", 24378, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/3/3/333302717.jpg",
                          4, "Juguete de ratón blanco con sonido para gatos.", "Juguetes"))
productos.append(Producto("Juguete de ratón billy jean", 20062, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/3/3/333302708.jpg",
                          4.3, "Juguete de ratón billy jean para gatos.", "Juguetes"))
productos.append(Producto("Juguete Gato. Wubba.", 23070, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/3/3/333302386_diana_lo_busco_.jpg",
                          4.7, "Juguete Gato. Wubba. Peluche. Ratón.", "Juguetes"))
p_gatos = [json.dumps(o.__dict__) for o in productos]
productos.clear()

# Otros
productos.append(Producto("Solla Broiler", 2625, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/0/101000057.jpg",
                          4.1, "Solla Broiler Engorde 1 Kg", ""))
productos.append(Producto("Comida para Loros, Cacatuas y Guacamayas", 15997, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111150012.jpg",
                          4.3, "Comida para Loros, Cacatuas y Guacamayas. Penta Grama. 1 kg.", ""))
productos.append(Producto("Incros Vital. Comida Peces", 12119, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111130050.jpg",
                          4.6, "Incros Vital. Comida Peces. 100 g.", ""))
productos.append(Producto("Conejina corriente", 2237, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/1/1/111120007.jpg",
                          4.2, "Conejina corriente 1Kg.", ""))
productos.append(Producto("Cat Can Multipet Cleaner", 20150, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/3/1/313160022_1_.jpg",
                          4.4, "Cat Can Multipet Cleaner en espuma Perro y gato 200 ml", ""))
productos.append(Producto("Ferplast Juguete Hamster", 22446, "https://www.agrocampo.com.co/media/catalog/product/cache/1/small_image/360x360/9df78eab33525d08d6e5fb8d27136e95/3/3/333300998-min.jpg",
                          4.3, "Ferplast Juguete Hamster Queso Tiny & Natural", ""))
p_otros = [json.dumps(o.__dict__) for o in productos]
productos.clear()

pic = 'https://icons-for-free.com/iconfiles/png/512/client+consumer+customer+person+profile+user+icon-1320086667172538072.png'
clientes = []
clientes.append(Cliente("Alberto Jimenez", "a.jimenez@gmail.com", "a123",
                        "Bogota", pic, [], []))
clientes.append(Cliente("Rigoberto Uran", "a.uran@gmail.com",
                        "rigo", "Boyaca", pic, [], []))
clientes.append(Cliente("Alberto Salinas", "a.salinas@gmail.com",
                        "salinas123", "Medellin", pic, [], ["perro"]))
clientes.append(Cliente("Rodolfo Aicardi", "a.aicardi@gmail.com",
                        "rodo321", "Bogota", pic, [], ["gato"]))
clientes.append(Cliente("Gabriel Mejia", "gb.mejia@gmail.com",
                        "gab123", "Cali", pic, [], ["perro", "gato"]))
clientes.append(Cliente("Valentina Acosta", "v.acosta@gmail.com",
                        "vacs321", "Cali", pic, [], []))
clientes = [json.dumps(o.__dict__) for o in clientes]

pas = 'https://www.hogarmania.com/archivos/201309/paseador-contento-668x400x80xX.jpg'
paseadores = []
paseadores.append(Paseador("Cesar Millan", 5, "He convivido con animales toda mi vida, tengo manejo sobre mascotas, he vivido con diferentes razas en mi vida como Pastor Aleman, Scottish Terrier, Fox Terrier, French Poodle y actualmente con un Pitbull.",
                           "Bogota", pas, ["perro"]))
paseadores.append(Paseador("Carmen Aparicio", 4, "Siempre he querido tener perritos (tuve uno cuando era niña y murio de viejito); por esto, me gustaria colaborarte en el cuidado del tuyo y que puedas estar tranquil@",
                           "Bogota", pas, ["perro"]))
paseadores.append(Paseador("David Pardo", 4.2, "Habiendo tenido perros desde los 5 años, Lucky y Dingo (ambos Pastores Alemanes), Susy (Pequinesa), Bamby (Dachshuond), Puppy (Shih Tzu) y Mancha (Cimarron Uruguayo); me considero con capacidad para tratar a su perro",
                           "Cali", pas, ["perro"]))
paseadores.append(Paseador("Mauricio Arango", 4.3, "Tengo 30 años soy de bogota Soy una persona con esposa y dos hijos y un pastor alemán de 11 meses llamada lola soy amoroso y cariñosa con ella",
                           "Bogota", pas, ["perro"]))
paseadores.append(Paseador("Liliana Beltran", 4.2, "Hola, mi nombre es Liliana y adoro los perros! Siempre he querido tener todo el contacto posible con ellos y aunque en este momento no tengo uno, sí he tenido anteriormente un Fox Terrier",
                           "Medellin", pas, ["perro"]))
paseadores.append(Paseador("Alan Garzon", 4, "Actualmente tengo dos perros que amo mucho, desde niño he crecido con perros por lo que siento gran amor y respeto hacia los perritos.",
                           "Medellin", pas, ["perro"]))
paseadores.append(Paseador("Paula Giraldo", 4.5, "Mi nombre es Paula y me esfuerzo para ser y estar mejor de lo que estuve y fui ayer. Mi compromiso con mi trabajo se traduce en el amor incondicional que mis clientes sienten",
                           "Bogota", pas, ["perro"]))
paseadores = [o.__dict__ for o in paseadores]

animales = []
animales.append(Animal("Perro", "https://criptopasion.com/wp-content/uploads/2019/04/20180109-JHPhGppU0zc44h7bp06E.jpg",
                       ["NexGard Antipulgas", "Galgocal Antiparasitario", "Bravecto Antiparasitario",
                        "Chunky Perros Adultos", "NexGard Spectra Antipulgas", "Canisan D Antihelmintico"]))
animales.append(Animal("Gato", "https://images.theconversation.com/files/350865/original/file-20200803-24-50u91u.jpg?ixlib=rb-1.1.0&rect=37%2C29%2C4955%2C3293&q=45&auto=format&w=926&fit=clip",
                       ["Advocate Antiparasitario", "Agility Gold Gatos", "Comfortis Antipulgas",
                        "Antiparasitario Drontal", "Mirrapel Suplemento Nutricional",
                        "Bonavit"]))
animales = [o.__dict__ for o in animales]

# Imprimir todos los objetos de una lista
resp = "["
for o in paseadores:
    resp += str(o) + ",\n"
resp = resp[:-2]
resp += "]"
print(resp)
