class Persona:
    def __init__(self, id, nombre, email, tel):
        self.idPersona=id
        self.nombre=nombre
        self.email=email
        self.telefono=tel

    def login(self):
        print("\n- Bienvienido ", self.nombre, "-")

    def logout(self):
        print(self.nombre, " cerro sesion")

class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, telefono, puntos):
        super().__init__(idPersona, nombre, email, telefono)

        self.puntosFidelidad=puntos

class Sala:
    def __init__(self, idEspacio, nombre, tipo, cap, lista):
        self.idEspacio=idEspacio
        self.nombre=nombre
        self.tipo=tipo
        self.capacidadTotal=cap
        self.ocupados=lista

class Pelicula:
    def __init__(self, titulo, duracion, clasif, gen):
        self.titulo=titulo
        self.duracion=duracion
        self.clasificacion=clasif
        self.genero=gen

class Funcion:
    def __init__(self, idF, peli, sala, hora, precio):
        self.idFuncion=idF
        self.pelicula=peli
        self.sala=sala
        self.horarioInicio=hora
        self.precioBase=precio

class Reserva:
    def __init__(self, idR, usuario, funcion):
        self.idReserva=idR
        self.usuario=usuario
        self.funcion=funcion
        self.asientos=[]
        self.montoTotal=0

    def verificar_asientos(self, elegidos):
        for i in elegidos:
            if i in self.funcion.sala.ocupados:
                print("[ERROR]: El asiento", i, "ya esta ocupado, checa eso")
                return False
        self.asientos=elegidos
        for i in elegidos:
            self.funcion.sala.ocupados.append(i)
            
        self.montoTotal=len(elegidos)*self.funcion.precioBase
        print("[OK]: Asientos", elegidos, "reservados")
        return True

    def aplicar_promo(self, cod):
        cod_limpio=cod.strip()
        if cod_limpio=="PROMO_ESTUDIANTE":
            ahorro=self.montoTotal*.20
            self.montoTotal=self.montoTotal-ahorro
            return ahorro
        return 0

class Producto:
    def __init__(self, id, nom, precio):
        self.id=id
        self.nom=nom
        self.precio=precio

    def detalle(self):
        return "ID:", self.id, "|", self.nom, "$", self.precio