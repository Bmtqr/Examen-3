import csv

estudiantes = {}

def registrar_estudiante (estudiantes):
    rut = (input ("Ingrese rut del estudiante: "))
    if rut in estudiantes:
        print ("Este rut ya se encuentra registrado.")
    else:
        nombre = input ("Ingrese nombre del estudiante: ")
        try:
            if nombre not in estudiantes:
                notas1 = float (input ("Ingrese primera nota del estudiante: "))
                notas2 = float (input ("Ingrese segunda nota del estudiante: "))
                notas3 = float (input ("Ingrese tercera nota del estudiante: "))
                notas4 = float (input ("Ingrese cuarta nota del estudiante: "))
                promedio = notas1 + notas2 + notas3 + notas4
                promedio = promedio // 4
                print (promedio)
                estudiantes [rut] = {
                    'rut' : rut,
                    'nombre' : nombre,
                    'nota1' : notas1,
                    'nota2' : notas2,
                    'nota3' : notas3,
                    'nota4' : notas4,
                    'nota presentacion' : notas4,
                    'nota final' : promedio
                }
            else:
                print ("Este alumno ya esta registrado.")
        except ValueError:
            print ()
            print ("[!] Ingrese caracter valido.")
            print ()
            

def ver_estudiantes (estudiantes):
    if not estudiantes:
        print ("No hay estudiantes registrados.")
    else:
        for estudiante, datos in estudiantes.items ():
            print (f"Rut: {datos['rut']}   Nombre: {datos['nombre']}   N1: {datos['nota1']}   N2: {datos['nota2']}   N3: {datos['nota3']}   N4: {datos['nota4']}   Nota Presentacion: {datos['nota presentacion']}    Nota Final: {datos['nota final']}")


def buscar_estudiante (estudiantes):
    buscar = input ("Ingrese rut del estudiante: ")
    if buscar in estudiantes:
        datos = estudiantes [buscar]
        print (f"Rut: {datos['rut']}   Nombre: {datos['nombre']}   N1: {datos['nota1']}   N2: {datos['nota2']}   N3: {datos['nota3']}   N4: {datos['nota4']}   Nota Presentacion: {datos['nota presentacion']}    Nota Final: {datos['promedio']}")



def convertir_csv (estudiantes):
    with open("nuevo_archivo.csv","w", newline="") as archivo_csv:
        campos = ['rut', 'nombre', 'nota1', 'nota2', 'nota3', 'nota4', 'nota presentacion', 'nota final']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for datos in estudiantes.values ():
           escritor_csv.writerow(datos)


while True:
    print ("1. Registrar estudiante.")
    print ("2. Ver estudiantes.")
    print ("3. Buscar estudiante.")
    print ("4. Convertir a CSV.")
    print ("5. Salir.")
    opcion = input ("Ingrese una opcion: ")

    if opcion == "1":
        registrar_estudiante (estudiantes)
    elif opcion == "2":
        ver_estudiantes (estudiantes)
    elif opcion == "3":
        buscar_estudiante (estudiantes)
    elif opcion == "4":
        convertir_csv (estudiantes)
    elif opcion == "5":
        break
