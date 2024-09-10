Taller1 = float(input("Ingrese la nota del taller 1: "))
if Taller1 > 5:
    print("nota no valida")
elif Taller1 < 0:
    print("nota no valida")

Taller2 = float(input("Ingrese la nota del taller 2: "))
if Taller2 > 5:
    print("nota no valida")
elif Taller2 < 0:
    print("nota no valida")

Cuestionario1 = float(input("Ingrese la nota del cuestionario 1: "))
if Cuestionario1 > 5:
    print("nota no valida")
elif Cuestionario1 < 0:
    print("nota no valida")

Cuestionario2 = float(input("Ingrese la nota del cuestionario 2: "))
if Cuestionario2 > 5:
    print("nota no valida")
elif Cuestionario2 < 0:
    print("nota no valida")

ProyectoFinal = float(input("Ingrese la nota del proyecto final : "))
if ProyectoFinal > 5:
    print("nota no valida")
elif ProyectoFinal < 0:
    print("nota no valida")

NotaTaller1 = 0.20*Taller1
NotaTaller2 = 0.15*Taller2
NotaCuestionario1 = 0.22*Cuestionario1
NotaCuestionario2 = 0.10*Cuestionario2
NotaProyectoFinal = 0.33*ProyectoFinal

nota_Final = NotaTaller1+NotaTaller2+NotaCuestionario1+NotaCuestionario2+NotaProyectoFinal

redondeado = round (nota_Final,2)
print("la nota final es de:", redondeado)
