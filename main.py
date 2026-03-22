

# Definicion de la class
# primera letra del nombre de la clase simpre mayuscula
#class
class Libro:
    #objetos
    #las funciones que estan dentro de las clases se llaman metodos
    # y estos metodos piden unos 
    # __init__ es un metodo constructor
    def __init__(self, titulo, autor, isbm , disponible=True):
        self.titulo= titulo
        self.autor= autor
        self.isbm= isbm
        self.disponible= disponible
        # podemos agregar 1 _ bajo para decir que nuestra variable es privada. es un parametro mental para identificarla como privada.
        self._veces_prestado= 0
    # metodo para imprimir la represetacion str de la clase
    def __str__(self):
        #retorna un string
        return  f"Libro: {self.titulo}\n"f"autor: {self.autor}\n" f"ISBM: {self.isbm} \n"f"disponibilidad: {self.disponible}\n"

    def prestar(self):
        if self.disponible:
            self._veces_prestado +=1
            self.disponible = False
            return f"{self.titulo} prestado exitosamente. total prestados: {self._veces_prestado}"
        return f"{self.titulo} No esta disponible"
    def cantidades(self):
            return self._veces_prestado > 5

    def devolver(self):
        self.disponible = True
        return f"{self.titulo} devuelto y disponible nuevamente"

    def gef_veces_prestado(self):
        return self._veces_prestado
    
    def set_veces_prestado(self, veces_prestado):
        self._veces_prestado = veces_prestado

#y hacer el prin de todos mediante for
mi_libro = Libro("100 años de soledad","Gabriel garcia marquez",932, True)
otro_libro = Libro("el principito","Saint-Exupery",323,True)

catalogo =[mi_libro,otro_libro]
for contador in catalogo:
    print( contador)


mi_libro.set_veces_prestado(10)
print(mi_libro.gef_veces_prestado())

print(mi_libro.prestar())
print(mi_libro.devolver())
print(mi_libro.prestar())
print(mi_libro.devolver())
print(mi_libro.prestar())
print(mi_libro.devolver())
print(mi_libro.prestar())
print(mi_libro.devolver())
print(mi_libro.prestar())
print(mi_libro.devolver())
print(mi_libro.prestar())

print(mi_libro.cantidades())


