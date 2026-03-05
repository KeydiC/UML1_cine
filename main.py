from models import *

ocupadoss=["A2"] 
salaa=Sala(4, "04", "IMAX", 100, ocupadoss)
peli=Pelicula("Zootopia 2", 108, "A", "Animacion")
func=Funcion(101, peli, salaa, "16:00", 150)
usr=Usuario(88, "Jax", "jax@gmail.com", "555", 150)

reserva = True
while reserva:
    print("\n ....Reservas.......")
    print("Usuario:", usr.nombre, "(Puntos:", usr.puntosFidelidad, ")")
    print("Película:", peli.titulo, "| Sala:", salaa.nombre)
    print("Asiento A2 oocupado")
    print("--- INVENTARIO ---")
    produc1=Producto(1,"Palomitas G", 85)
    produc2=Producto(2,"Refresco M", 45)
    produc3=Producto(3,"Hot Dog", 60)
    produc4=Producto(4,"Nachos", 70)
    produc5=Producto(5,"Chocolate", 35)
    produc6=Producto(6,"Agua", 30)
    produc7=Producto(7,"Combo 1", 210)
    produc8=Producto(8,"Boleto 2D", 80)
    produc9=Producto(9,"Boleto 3D", 95)
    produc10=Producto(10,"Vaso", 150)

    print(produc1.detalle())
    print(produc2.detalle())
    print(produc3.detalle())
    print(produc4.detalle())
    print(produc5.detalle())
    print(produc6.detalle())
    print(produc7.detalle())
    print(produc8.detalle())
    print(produc9.detalle())
    print(produc10.detalle())
    
    res=Reserva(707, usr, func)
    
    exito=False
    while exito==False:
        txt=input("Seleccione sus asientos (separados por coma A1, A2 etc): ")
        listaa=txt.split(",")
        
        if res.verificar_asientos(listaa):
            exito=True
            print("Monto base: $", res.montoTotal)
        else:
            print("[SISTEMA]: seleccione asientos disponibles")

  
    print("\n GESTIÓN COMERCIAL")
    opc=input("Tienes codigo de promocion?(s/n): ")
    ahorro_final = 0
    if opc=="S" or opc=="s":
        cod=input("Codigo: ")
        ahorro_final=res.aplicar_promo(cod)
        if ahorro_final>0:
            print("[SISTEMA]: Validando codigo... ¡EXITO! (Descuento del 20% aplicado)")


    print("\nResumen de Reserva #707:")
    print("----------------------------------------")
    print("Usuario:", usr.nombre)
    print("Función: Dune (16:00 hrs)") 
    print("Asientos:", res.asientos)
    print("Total Final: $", res.montoTotal, "(Ahorraste $", ahorro_final, ")")
    print("----------------------------------------")
    print("Estado: PAGADO Ticket listo .w.")
    

    cont=input("\notra venta? (s/n): ")
    if cont=="n" or cont=="N":
        reserva=False