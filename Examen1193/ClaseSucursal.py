# Definimos la clase Sucursal1193
class Sucursal1193:
    # Inicializamos los atributos con valores vacíos o 0
    codigo_de_sucursal = "1193"
    Ubicacion = "Calle Piña"
    Horario = "7:00 am a 8:00 pm"
    Numero_de_telefono = "6563514062"
    Email = "a.22308051281193"
    Estado = "Chihuahua"
    Nombre_sucursal = "Garcia Trucks"

    # Función para mostrar los datos del Sucursal
    def mostrar_datos1193(self):
        print(f"codigo_de_sucursal: {self.codigo_de_sucursal}")
        print(f"Ubicacion: {self.Ubicacion}")
        print(f"Horario: {self.Horario}")
        print(f"Numero_de_telefono: {self.Numero_de_telefono}")
        print(f"Email: {self.Email}")
        print(f"Estado: {self.Estado}")
        print(f"Nombre_sucursal: {self.Nombre_sucursal}")

    # Función para listar 5 Sucursal en una lista
    def Listar_sucu(self):
        lista_sucu = [
            "Sucursal Ford", 
            "Sucursal Chevrolet", 
            "Sucursal GMC", 
            "Sucursal Nissan", 
            "Sucursal suzuki"
        ]
        for x in lista_sucu:
            print (x)
        return lista_sucu
    # Función para crear una tupla
    def Tupla_sucur(self):
        tupla_suc = (
            "suc. Morelos", 
            "suc. Mexico", 
            "suc. EUA", 
            "suc. Francia", 
            "suc. Yucatan"
        )
        for x in tupla_suc:
            print (x)
        return tupla_suc

    # Función para crear un diccionario de Sucursal
    def Dicionario_Sucursal(self):
        diccionario_su = {
            "id sucursal Ford": 1193,
            "id sucursal Chevrolet": 1209,
            "id sucursal GMC": 1207,
            "id sucursal Nissan": 9090,
            "id sucursal Suzuki": 9087
        }
        for x in diccionario_su:
            print (x)
        return diccionario_su
    
    # Función para dar de alta a un cliente
    def altas(self):
        print("Se realizó correctamente.")

    # Función para dar de baja a un cliente
    def bajas(self):
        print("Se realizó incorrectamente.")

# Creación del objeto sucursal
Sucursal = Sucursal1193()

# Asignación de datos a los atributos
codigo_de_sucursal = "1193"
Ubicacion = "Calle Piña"
Horario = "7:00 am a 8:00 pm"
Numero_de_telefono = "6563514062"
Email = "a.22308051281193"
Estado = "Chihuahua"
Nombre_sucursal = "Garcia Trucks"

# Utilización de los objetos
# Mostrar datos de sucursal
Sucursal.mostrar_datos1193()

# Llamadas a las funciones
print("\nLista de sucursal:")
print(Sucursal.Listar_sucu())

print("\nTupla de sucursal:")
print(Sucursal.Tupla_sucur())

print("\nDiccionario de sucursal:")
print(Sucursal.Dicionario_Sucursal())

# Operaciones de alta y baja
Sucursal.altas()
Sucursal.bajas()
