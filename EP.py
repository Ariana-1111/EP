from datetime import datetime
import random

# Códigos de color ANSI para el estilo visual en consola
AZUL_CLARO = "\033[96m"
VERDE = "\033[92m"
MORADO_BAJITO_NEGRO = "\033[4;48;5;189;30m"
RESET = "\033[0m"
ANCHO = 78

#ALCANCE DE VARIABLES GLOBALES Tarifas fijas y contador general
COSTO_DIAGNOSTICO_FIJO = 40.0
COSTO_POR_TERAPIA = 45.0
META_DIARIA_PACIENTES = 10
atenciones_hoy = 0

#LISTAS
CODIGOS_PREDETERMINADOS = [
    "AX-1234", "AX-4321", "AX-2580", "AX-7890", "AX-3698",
    "AX-1470", "AX-8523", "AX-9632", "AX-5412", "AX-6745"
]

CATALOGO_ENFERMEDADES = [
    "Artritis", "Artrosis", "Diabetes", "Gastritis",
    "Higado graso", "Presion alta", "NA"
]

CATALOGO_ZONAS_DOLOR = [
    "Cabeza", "Cintura", "Codo", "Cuello",
    "Espalda", "Gluteo", "Hombro", "Pantorrilla", "Pierna", "Rodillas", "NA"
]

CATALOGO_DIAGNOSTICOS = [
    "Articulacion movida", "Cadera trabada", "Cifosis", "Ciatica",
    "Contractura espalda", "Dismetria de piernas", "Espolon calcaneo",
    "Escoliosis", "Hernia", "Irritacion diafragmatica", "Lordosis",
    "Lumbalgia", "Necrosis", "Osteofitos",
    "Sacroileitis", "Sind. cauda equina", "Tendinitis", "Torticolis", "NA"
]


#1MÓDULO DE VALIDACIÓN POR RECORRIDO DE CADENAS
# FUNCIÓN CON PARÁMETRO Y RETORNO Verifica carácter por carácter si es entero
def es_numero_entero(texto):
    if len(texto) == 0:
        return False
    #ESTRUCTURA REPETITIVA FOR Recorre cada carácter del string
    for caracter in texto:
        if caracter < "0" or caracter > "9":
            return False
    return True


#FUNCIÓN CON PARÁMETRO Y RETORNO Verifica si un texto es decimal válido
def es_numero_decimal(texto):
    if len(texto) == 0 or texto == ".":
        return False
    cantidad_puntos = 0
    # ESTRUCTURA REPETITIVA FOR Recorre cada carácter de la cadena
    for caracter in texto:
        if caracter == ".":
            cantidad_puntos += 1
        elif caracter < "0" or caracter > "9":
            return False
    if cantidad_puntos <= 1:
        return True
    else:
        return False


#FUNCIÓN CON PARÁMETRO Y RETORNO Verifica que una palabra solo tenga letras
def es_solo_letras(palabra):
    if len(palabra) == 0:
        return False
    letras_validas = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ"
    #Comprueba que cada carácter esté dentro del alfabeto
    for caracter in palabra:
        if caracter not in letras_validas:
            return False
    return True


#FUNCIÓN CON PARÁMETROS Y RETORNO Validación estricta de mínimo 3 palabras con 3 letras cada una
def validarnombre(mensajeinicio, mensajeerror):
    valido = False
    #STRUCTURA REPETITIVA WHILE Repite hasta ingresar un nombre real
    while not valido:
        #CADENAS DE CARACTERES .strip() y .split()
        texto = input(mensajeinicio).strip()
        palabras = texto.split()
        if len(palabras) >= 3:
            valido = True
            #ESTRUCTURA REPETITIVA FORRevisa palabra por palabra
            for palabra in palabras:
                if len(palabra) < 3 or not es_solo_letras(palabra):
                    valido = False
        if not valido:
            print(mensajeerror)
    #CADENAS DE CARACTERES .upper() normaliza a mayúsculas
    return texto.upper()


#FUNCIÓN CON PARÁMETROS Y RETORNO Valida DNI de 8 dígitos evitando duplicados
def validardni(fichas):
    dnivalido = False
    #ESTRUCTURA REPETITIVA WHILE Bucle de control de entrada
    while not dnivalido:
        dni = input("Ingrese DNI del paciente (8 digitos): ").strip()
        if len(dni) == 8 and es_numero_entero(dni):
            #BÚSQUEDA EN LISTA Comprueba si el DNI ya está registrado
            repetido = False
            for i in range(len(fichas)):
                if fichas[i]["dni"] == dni:
                    repetido = True
            if repetido:
                print("   [!] Error: Ya existe una ficha registrada con este DNI.")
            else:
                dnivalido = True
        else:
            print("   [!] Lo que estas ingresando no es valido, el DNI debe tener 8 numeros.")
    return dni


#FUNCIÓN CON RETORNO Valida que sean 9 dígitos y empiece con 9
def validarcelular():
    celularvalido = False
    while not celularvalido:
        celular = input("Telefono celular (9 digitos, inicia con 9): ").strip()
        if len(celular) == 9 and celular[0] == "9" and es_numero_entero(celular):
            celularvalido = True
        else:
            print("     [!] Celular no valido, verifica e ingresa 9 numeros empezando con 9.")
    return celular


#FUNCIÓN CON PARÁMETROS Y RETORNO Lee un entero dentro de un rango sin cerrarse jamás
def validar_entero_rango(mensaje, minimo, maximo):
    valido = False
    numero = 0
    while not valido:
        entrada = input(mensaje).strip()
        if es_numero_entero(entrada):
            numero = int(entrada)
            if minimo <= numero <= maximo:
                valido = True
            else:
                print(f"    [!] El numero debe estar entre {minimo} y {maximo}. Intenta nuevamente.")
        else:
            print("   [!] Lo que estas ingresando no es valido, por favor ingresa un numero entero.")
    return numero


#FUNCIÓN CON PARÁMETROS Y RETORNO Lee un decimal dentro de un rango
def validar_decimal_rango(mensaje, minimo, maximo):
    valido = False
    numero = 0.0
    while not valido:
        entrada = input(mensaje).strip()
        if es_numero_decimal(entrada):
            numero = float(entrada)
            if minimo <= numero <= maximo:
                valido = True
            else:
                print(f"    [!] El valor debe estar entre {minimo} y {maximo}. Intenta nuevamente.")
        else:
            print("   [!] Lo que estas ingresando no es valido, por favor ingresa un valor numerico.")
    return numero


#FUNCIÓN CON PARÁMETROS Y RETORNO Permite elegir varias opciones o terminar con 0 ("Ninguna")
def seleccionar_multiples_opciones(titulo, catalogo):
    borde_catalogo = "╭" + "─" * (ANCHO - 2) + "╮"
    borde_catalogo_inf = "╰" + "─" * (ANCHO - 2) + "╯"
    texto_titulo = f"--- {titulo} ---"
    print(f"\n{borde_catalogo}")
    print(f"│{texto_titulo:^{ANCHO - 2}}│")
    print(f"{borde_catalogo_inf}")
    
    #RECORRIDO INDEXADO DE LISTA Muestra las opciones con su número correspondiente
    for i in range(len(catalogo) - 1):
        print(f" [{i + 1}] {catalogo[i]}")
    #La última opción NA se asigna al número 0
    print(f" [0] {catalogo[-1]}")

    valido = False
    resultado_final = ""

    while not valido:
        entrada = input(f"Seleccione opcion(es) ej: 1 o 1,3 (use 0 para NA): ").strip()
        if entrada != "":
            partes = entrada.split(",")
            elegidos = []
            todo_correcto = True

            for parte in partes:
                limpio = parte.strip()
                if es_numero_entero(limpio):
                    num = int(limpio)
                    if num == 0:
                        elegidos = [catalogo[-1]]
                        break
                    elif 1 <= num <= len(catalogo) - 1:
                        nombre_opcion = catalogo[num - 1]
                        if nombre_opcion not in elegidos:
                            elegidos.append(nombre_opcion)
                    else:
                        print(f"   [!] Error: El numero {num} supera la cantidad de opciones.")
                        todo_correcto = False
                else:
                    print("   [!] Lo que estas ingresando no es valido, usa solo numeros seguido de una coma.")
                    todo_correcto = False

            if todo_correcto and len(elegidos) > 0:
                resultado_final = ", ".join(elegidos)
                valido = True
        else:
            print("   [!] Debes seleccionar al menos una opcion o ingresar 0.")

    return resultado_final


#FUNCIÓN CON PARÁMETROS Y RETORNO Selecciona al azar un código AX-XXXX predeterminado sin repetir
def obtener_codigo_predeterminado(fichas):
    disponibles = []
    for cod in CODIGOS_PREDETERMINADOS:
        usado = False
        for i in range(len(fichas)):
            if fichas[i]["codigo"] == cod:
                usado = True
        if not usado:
            disponibles.append(cod)
    if len(disponibles) > 0:
        return random.choice(disponibles)
    else:
        return "AX-" + str(random.randint(1000, 9999))


#FUNCIÓN CON RETORNO Suma S/ 40 de diagnóstico + (terapias * S/ 45)
def calcular_costo_total(terapias):
    subtotal_terapias = terapias * COSTO_POR_TERAPIA
    total = COSTO_DIAGNOSTICO_FIJO + subtotal_terapias
    return total

#2MÓDULO DE PRESENTACIÓN Y REPORTES 
def mostrar_ficha_paciente(ficha):
    subtotal_terapias = ficha["terapias"] * COSTO_POR_TERAPIA
    titulo_ficha = f"FICHA CLINICA QUIROPRACTICA AXIS - CODIGO: {ficha['codigo']}"
    print("\n╭" + "─" * (ANCHO - 2) + "╮")
    print(f"│{titulo_ficha:^{ANCHO - 2}}│")
    print("╰" + "─" * (ANCHO - 2) + "╯")
    print(f" Fecha y Hora de Registro: {ficha['fecha']}")
    print(f" Paciente: {ficha['nombre']} | DNI: {ficha['dni']}")
    print(f" Edad: {ficha['edad']} años | Peso: {ficha['peso']} kg | Talla: {ficha['talla']} m")
    print(f" Telefono Celular: {ficha['telefono']}")
    print("-" * ANCHO)
    print(f" Enfermedades registradas: {ficha['enfermedades']}")
    print(f" Zonas de dolor:           {ficha['dolores']}")
    print(f" Diagnostico quiropractico:{ficha['diagnostico']}")
    print("-" * ANCHO)
    print(f" Costo de Diagnostico: {VERDE}S/ {COSTO_DIAGNOSTICO_FIJO:.2f}{RESET}")
    print(f" Costo de Terapias ({ficha['terapias']} x {VERDE}S/ 45{RESET}): {VERDE}S/ {subtotal_terapias:.2f}{RESET}")
    print(f" COSTO TOTAL A PAGAR:         {VERDE}S/ {ficha['costo_total']:.2f}{RESET}")
    print(f" Observaciones:               {ficha['observaciones']}")
    print("=" * ANCHO)


def main():
    global atenciones_hoy

    fichas = []

    ejecutando = True
    while ejecutando:
        titulo_axis = "SISTEMA DE GESTION CLINICA - CENTRO QUIROPRACTICO 'AXIS'"
        subtitulo_1 = "Av. Nuevo Cajamarca | Encargado: Cesar Luis"
        subtitulo_2 = f"Total Fichas: {len(fichas)} | Atendidos hoy: {atenciones_hoy}/{META_DIARIA_PACIENTES}"

        print("\n╔" + "═" * (ANCHO - 2) + "╗")
        print(f"║{AZUL_CLARO}{titulo_axis:^{ANCHO - 2}}{RESET}║")
        print(f"║{subtitulo_1:^{ANCHO - 2}}║")
        print(f"║{subtitulo_2:^{ANCHO - 2}}║")
        print("╚" + "═" * (ANCHO - 2) + "╝")
        print("\nBienvenido al sistema de gestion del Centro Quiropractico Axis.")
        print("Selecciona una de las siguientes opciones para continuar:")
        print(" [1] Registrar nueva Ficha Quiropractica")
        print(" [2] Buscar ficha de paciente por DNI")
        print(" [3] Ordenar fichas alfabeticamente") #Metodo Burbuja
        print(" [4] Ordenar fichas por Costo de Mayor a Menor") #Metodo Seleccion
        print(" [5] Listar todas las fichas e ingresos acumulados")
        print(" [0] Salir")

        opcion = input("\nSelecciona una opcion: ").strip()

        if opcion == "1":
            borde_val = "╭" + "─" * (ANCHO - 2) + "╮"
            borde_val_inf = "╰" + "─" * (ANCHO - 2) + "╯"
            titulo_registro = "REGISTRO DE NUEVA FICHA QUIROPRACTICA"
            print(f"{borde_val}")
            print(f"│{titulo_registro:^{ANCHO - 2}}│")
            print(f"{borde_val_inf}")
            
            fecha_hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
            print(f"Fecha y hora de ficha registrada: {fecha_hora_actual}")

            dni = validardni(fichas)
            nombre = validarnombre(
                "Nombre completo: ",
                "   [!] Nombre no valido, escribe al menos 3 palabras con minimo 3 letras."
            )
            edad = validar_entero_rango("Edad del paciente: ", 1, 110)
            peso = validar_decimal_rango("Peso en kg: ", 10.0, 250.0)
            talla = validar_decimal_rango("Talla en metros (ej. 1.60): ", 0.50, 2.30)
            telefono = validarcelular()

            enfermedades = seleccionar_multiples_opciones("SELECCIONE ENFERMEDAD(ES)", CATALOGO_ENFERMEDADES)
            dolores = seleccionar_multiples_opciones("SELECCIONE ZONA(S) DE DOLOR", CATALOGO_ZONAS_DOLOR)
            diagnostico = seleccionar_multiples_opciones("SELECCIONE DIAGNOSTICO(S) DE COLUMNA", CATALOGO_DIAGNOSTICOS)

            terapias = validar_entero_rango("\nCantidad de terapias indicadas: ", 1, 20)

            observaciones = input("Observaciones clinicas (ENTER para NA): ").strip()
            if observaciones == "":
                observaciones = "Sin observaciones adicionales."

            codigo_ficha = obtener_codigo_predeterminado(fichas)
            costo_final = calcular_costo_total(terapias)

            nueva_ficha = {
                "codigo": codigo_ficha,
                "fecha": fecha_hora_actual,
                "dni": dni,
                "nombre": nombre,
                "edad": edad,
                "peso": peso,
                "talla": talla,
                "telefono": telefono,
                "enfermedades": enfermedades,
                "dolores": dolores,
                "diagnostico": diagnostico,
                "terapias": terapias,
                "costo_total": costo_final,
                "observaciones": observaciones
            }

            fichas.append(nueva_ficha)
            atenciones_hoy += 1

            print(f"\n¡REGISTRO EXITOSO! Se guardo la ficha {codigo_ficha} con fecha {fecha_hora_actual}")
            mostrar_ficha_paciente(nueva_ficha)

        elif opcion == "2":
            dni_buscado = input("\nIngrese el DNI a buscar (sin errores): ").strip()
            posicion = -1
            for i in range(len(fichas)):
                if fichas[i]["dni"] == dni_buscado:
                    posicion = i

            if posicion != -1:
                mostrar_ficha_paciente(fichas[posicion])
            else:
                print(f"   [!] No se encontro ningun paciente con el DNI {dni_buscado}.")

        elif opcion == "3":
            n = len(fichas)
            for i in range(n - 1):
                for j in range(n - 1 - i):
                    if fichas[j]["nombre"].lower() > fichas[j + 1]["nombre"].lower():
                        auxiliar = fichas[j]
                        fichas[j] = fichas[j + 1]
                        fichas[j + 1] = auxiliar

            print("\n   GENIAL! Fichas ordenadas alfabeticamente:") #Metodo Burbuja
            for i in range(n):
                f = fichas[i]
                print(f" {i + 1}. {f['nombre']} | DNI: {f['dni']} | Fecha: {f['fecha']} | Total: {VERDE}S/ {f['costo_total']:.2f}{RESET}")

        elif opcion == "4":
            n = len(fichas)
            for i in range(n - 1):
                mejor = i
                for j in range(i + 1, n):
                    if fichas[j]["costo_total"] > fichas[mejor]["costo_total"]:
                        mejor = j
                if mejor != i:
                    auxiliar = fichas[i]
                    fichas[i] = fichas[mejor]
                    fichas[mejor] = auxiliar

            print("\n   GENIAL! Fichas ordenadas de Mayor a Menor Costo:") #Metodo Seleccion
            for i in range(n):
                f = fichas[i]
                print(f" {i + 1}. {VERDE}S/ {f['costo_total']:.2f}{RESET} ({f['terapias']} terapias + {VERDE}S/ 40{RESET} diag.) | {f['nombre']} | Fecha: {f['fecha']}")

        elif opcion == "5":
            borde_list = "╭" + "─" * (ANCHO - 2) + "╮"
            borde_list_inf = "╰" + "─" * (ANCHO - 2) + "╯"
            titulo_listado = "LISTADO GENERAL DE FICHAS CLINICAS Y RECAUDACION"
            print(f"\n{borde_list}")
            print(f"│{titulo_listado:^{ANCHO - 2}}│")
            print(f"{borde_list_inf}")
            recaudacion_total = 0.0
            for i in range(len(fichas)):
                f = fichas[i]
                recaudacion_total += f["costo_total"]
                print(f" {i + 1}. {MORADO_BAJITO_NEGRO}[{f['codigo']}]{RESET} Fecha: {f['fecha']} | DNI: {f['dni']} | {f['nombre']}")
                print(f"    Enfermedades: {f['enfermedades']} | Dolor: {f['dolores']} | Diag: {f['diagnostico']}")
                print(f"    Terapias: {f['terapias']} (x S/ 45) + Diag. (S/ 40) -> TOTAL: {VERDE}S/ {f['costo_total']:.2f}{RESET}")
                print("-" * ANCHO)
            print(f" TOTAL PACIENTES REGISTRADOS: {len(fichas)} | INGRESO TOTAL ACUMULADO: {VERDE}S/ {recaudacion_total:.2f}{RESET}")
            print("=" * ANCHO)

        elif opcion == "0":
            print("\nCerrando sistema del Centro Quiropractico Axis ¡Hasta luego!")
            ejecutando = False
        else:
            print("\n   [!] Opcion no valida, ingresa un numero del 0 al 5.")
main()# Sistema Clinica Axis Final
# Version final Axis
