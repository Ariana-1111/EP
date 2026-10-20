Algoritmo Sistema_Clinica_Axis
    // declaracion de variables para el registro y control de pacientes
    Definir seleccion, n, i, j, pos, edad, terapias, atenciones Como Entero
    Definir dniBuscar, dniNuevo, nombreNuevo, telefonoNuevo, codigoNuevo Como Cadena
    Definir enfermedadNueva, dolorNuevo, diagnosticoNuevo, observacionesNueva, fechaNueva Como Cadena
    Definir edadAux Como Entero
    Definir pesoNuevo, tallaNueva, costoNuevo, recaudacion, subtotal, auxReal Como Real
    Definir auxCadena Como Cadena
    Definir encontrado Como Logico
	
    // arreglos paralelos para conservar los datos de cada ficha
    Dimension codigo[100], fecha[100], dni[100], nombre[100]
    Dimension edadP[100], peso[100], talla[100], telefono[100]
    Dimension enfermedades[100], dolores[100], diagnosticos[100]
    Dimension terapiasP[100], costos[100], observaciones[100]
	
    // inicializacion de contadores y opcion inicial del menu
    n <- 0
    atenciones <- 0
    seleccion <- -1
	
    // ciclo principal de navegacion entre las opciones del sistema
    Mientras seleccion <> 0 Hacer
        Escribir ""
        Escribir "=================================================="
        Escribir " SISTEMA DE GESTION CLINICA - CENTRO QUIROPRACTICO AXIS"
        Escribir " Av. Nuevo Cajamarca | Encargado: Cesar Luis"
        Escribir " Fichas registradas: ", n
        Escribir " Atendidos hoy: ", atenciones, "/10"
        Escribir "=================================================="
        Escribir "1. Registrar nueva ficha quiropractica"
        Escribir "2. Buscar ficha por DNI"
        Escribir "3. Ordenar fichas alfabeticamente"
        Escribir "4. Ordenar fichas por costo de mayor a menor"
        Escribir "5. Listar fichas e ingresos acumulados"
        Escribir "0. Salir"
        Escribir "Selecciona una opcion:"
        Leer seleccion
		
        Segun seleccion Hacer
            1:
                // registro de una ficha con limite maximo de 100 pacientes
                Si n < 100 Entonces
                    Escribir ""
                    Escribir "--- REGISTRO DE NUEVA FICHA ---"
                    Escribir "Ingrese fecha de registro (dd/mm/aaaa):"
                    Leer fechaNueva
					
                    // validacion del formato del dni y control de duplicados
                    encontrado <- Verdadero
                    Mientras encontrado Hacer
                        Escribir "Ingrese DNI del paciente (8 digitos):"
                        Leer dniNuevo
                        encontrado <- Falso
                        Si Longitud(dniNuevo) <> 8 Entonces
                            encontrado <- Verdadero
                            Escribir "Error: el DNI debe tener 8 digitos."
                        SiNo
                            Para i <- 1 Hasta n Hacer
                                Si dni[i] = dniNuevo Entonces
                                    encontrado <- Verdadero
                                FinSi
                            FinPara
                            Si encontrado Entonces
                                Escribir "Error: ya existe una ficha con ese DNI."
                            FinSi
                        FinSi
                    FinMientras
					
                    Escribir "Ingrese nombre completo:"
                    Leer nombreNuevo
                    // control de rangos permitidos para edad, peso y talla
                    Escribir "Edad del paciente (1 a 110):"
                    Leer edad
                    Mientras edad < 1 O edad > 110 Hacer
                        Escribir "Edad no valida. Ingrese una edad entre 1 y 110:"
                        Leer edad
                    FinMientras
					
                    Escribir "Peso en kg (10 a 250):"
                    Leer pesoNuevo
                    Mientras pesoNuevo < 10 O pesoNuevo > 250 Hacer
                        Escribir "Peso no valido. Ingrese un valor entre 10 y 250:"
                        Leer pesoNuevo
                    FinMientras
					
                    Escribir "Talla en metros (0.50 a 2.30):"
                    Leer tallaNueva
                    Mientras tallaNueva < 0.50 O tallaNueva > 2.30 Hacer
                        Escribir "Talla no valida. Ingrese un valor entre 0.50 y 2.30:"
                        Leer tallaNueva
                    FinMientras
					
                    // comprobacion basica de longitud y prefijo del celular
                    encontrado <- Falso
                    Mientras No encontrado Hacer
                        Escribir "Telefono celular (9 digitos, inicia con 9):"
                        Leer telefonoNuevo
                        Si Longitud(telefonoNuevo) = 9 Entonces
                            Si SubCadena(telefonoNuevo, 0, 0) = "9" Entonces
                                encontrado <- Verdadero
                            SiNo
                                Escribir "El celular debe comenzar con 9."
                            FinSi
                        SiNo
                            Escribir "El celular debe tener 9 digitos."
                        FinSi
                    FinMientras
					
                    Escribir ""
                    // asignacion de categorias mediante opciones numericas
                    Escribir "Seleccione enfermedad:"
                    Escribir "1. Artritis"
                    Escribir "2. Artrosis"
                    Escribir "3. Diabetes"
                    Escribir "4. Gastritis"
                    Escribir "5. Higado graso"
                    Escribir "6. Presion alta"
                    Escribir "0. NA"
                    Leer seleccion
                    Segun seleccion Hacer
                        1: enfermedadNueva <- "Artritis"
                        2: enfermedadNueva <- "Artrosis"
                        3: enfermedadNueva <- "Diabetes"
                        4: enfermedadNueva <- "Gastritis"
                        5: enfermedadNueva <- "Higado graso"
                        6: enfermedadNueva <- "Presion alta"
                        De Otro Modo: enfermedadNueva <- "NA"
                    FinSegun
					
                    Escribir "Seleccione zona de dolor:"
                    Escribir "1. Cabeza  2. Cintura  3. Codo  4. Cuello"
                    Escribir "5. Espalda  6. Gluteo  7. Hombro  8. Pantorrilla"
                    Escribir "9. Pierna  10. Rodillas  0. NA"
                    Leer seleccion
                    Segun seleccion Hacer
                        1: dolorNuevo <- "Cabeza"
                        2: dolorNuevo <- "Cintura"
                        3: dolorNuevo <- "Codo"
                        4: dolorNuevo <- "Cuello"
                        5: dolorNuevo <- "Espalda"
                        6: dolorNuevo <- "Gluteo"
                        7: dolorNuevo <- "Hombro"
                        8: dolorNuevo <- "Pantorrilla"
                        9: dolorNuevo <- "Pierna"
                        10: dolorNuevo <- "Rodillas"
                        De Otro Modo: dolorNuevo <- "NA"
                    FinSegun
					
                    Escribir "Seleccione diagnostico:"
                    Escribir "1. Articulacion movida  2. Cadera trabada  3. Cifosis"
                    Escribir "4. Ciatica  5. Contractura espalda  6. Dismetria de piernas"
                    Escribir "7. Espolon calcaneo  8. Escoliosis  9. Hernia"
                    Escribir "10. Irritacion diafragmatica  11. Lordosis  12. Lumbalgia"
                    Escribir "13. Necrosis  14. Osteofitos  15. Sacroileitis"
                    Escribir "16. Sind. cauda equina  17. Tendinitis  18. Torticolis  0. NA"
                    Leer seleccion
                    Segun seleccion Hacer
                        1: diagnosticoNuevo <- "Articulacion movida"
                        2: diagnosticoNuevo <- "Cadera trabada"
                        3: diagnosticoNuevo <- "Cifosis"
                        4: diagnosticoNuevo <- "Ciatica"
                        5: diagnosticoNuevo <- "Contractura espalda"
                        6: diagnosticoNuevo <- "Dismetria de piernas"
                        7: diagnosticoNuevo <- "Espolon calcaneo"
                        8: diagnosticoNuevo <- "Escoliosis"
                        9: diagnosticoNuevo <- "Hernia"
                        10: diagnosticoNuevo <- "Irritacion diafragmatica"
                        11: diagnosticoNuevo <- "Lordosis"
                        12: diagnosticoNuevo <- "Lumbalgia"
                        13: diagnosticoNuevo <- "Necrosis"
                        14: diagnosticoNuevo <- "Osteofitos"
                        15: diagnosticoNuevo <- "Sacroileitis"
                        16: diagnosticoNuevo <- "Sind. cauda equina"
                        17: diagnosticoNuevo <- "Tendinitis"
                        18: diagnosticoNuevo <- "Torticolis"
                        De Otro Modo: diagnosticoNuevo <- "NA"
                    FinSegun
					
                    Escribir "Cantidad de terapias indicadas (1 a 20):"
                    Leer terapias
                    Mientras terapias < 1 O terapias > 20 Hacer
                        Escribir "Ingrese una cantidad entre 1 y 20:"
                        Leer terapias
                    FinMientras
					
                    Escribir "Observaciones clinicas (escriba NA si no hay):"
                    Leer observacionesNueva
					
                    // calculo del costo y generacion del codigo de ficha
                    n <- n + 1
                    codigoNuevo <- "AX-" + ConvertirATexto(1000 + n)
                    subtotal <- terapias * 45
                    costoNuevo <- 40 + subtotal
					
                    // almacenamiento de los datos en sus arreglos respectivos
                    codigo[n] <- codigoNuevo
                    fecha[n] <- fechaNueva
                    dni[n] <- dniNuevo
                    nombre[n] <- nombreNuevo
                    edadP[n] <- edad
                    peso[n] <- pesoNuevo
                    talla[n] <- tallaNueva
                    telefono[n] <- telefonoNuevo
                    enfermedades[n] <- enfermedadNueva
                    dolores[n] <- dolorNuevo
                    diagnosticos[n] <- diagnosticoNuevo
                    terapiasP[n] <- terapias
                    costos[n] <- costoNuevo
                    observaciones[n] <- observacionesNueva
                    atenciones <- atenciones + 1
					
                    Escribir ""
                    Escribir "REGISTRO EXITOSO. Codigo de ficha: ", codigoNuevo
                    Escribir "Fecha: ", fechaNueva
                    Escribir "Paciente: ", nombreNuevo, " | DNI: ", dniNuevo
                    Escribir "Edad: ", edad, " | Peso: ", pesoNuevo, " kg | Talla: ", tallaNueva, " m"
                    Escribir "Telefono: ", telefonoNuevo
                    Escribir "Enfermedad: ", enfermedadNueva
                    Escribir "Zona de dolor: ", dolorNuevo
                    Escribir "Diagnostico: ", diagnosticoNuevo
                    Escribir "Costo de diagnostico: S/ 40"
                    Escribir "Costo de terapias: S/ ", subtotal
                    Escribir "COSTO TOTAL: S/ ", costoNuevo
                    Escribir "Observaciones: ", observacionesNueva
                SiNo
                    Escribir "No se pueden registrar mas de 100 fichas."
                FinSi
				
            2:
                // busqueda secuencial de una ficha mediante el dni
                Escribir "Ingrese el DNI que desea buscar:"
                Leer dniBuscar
                pos <- 0
                Para i <- 1 Hasta n Hacer
                    Si dni[i] = dniBuscar Entonces
                        pos <- i
                    FinSi
                FinPara
                Si pos > 0 Entonces
                    Escribir "Ficha encontrada: ", codigo[pos]
                    Escribir "Paciente: ", nombre[pos], " | DNI: ", dni[pos]
                    Escribir "Fecha: ", fecha[pos]
                    Escribir "Edad: ", edadP[pos], " | Peso: ", peso[pos], " | Talla: ", talla[pos]
                    Escribir "Telefono: ", telefono[pos]
                    Escribir "Enfermedad: ", enfermedades[pos]
                    Escribir "Zona de dolor: ", dolores[pos]
                    Escribir "Diagnostico: ", diagnosticos[pos]
                    Escribir "Terapias: ", terapiasP[pos]
                    Escribir "Costo total: S/ ", costos[pos]
                    Escribir "Observaciones: ", observaciones[pos]
                SiNo
                    Escribir "No se encontro una ficha con ese DNI."
                FinSi
				
            3:
                // ordenamiento burbuja por nombre, intercambiando la ficha completa
                Para i <- 1 Hasta n - 1 Hacer
                    Para j <- 1 Hasta n - i Hacer
                        Si nombre[j] > nombre[j + 1] Entonces
                            auxCadena <- nombre[j]
                            nombre[j] <- nombre[j + 1]
                            nombre[j + 1] <- auxCadena
							
                            auxCadena <- codigo[j]
                            codigo[j] <- codigo[j + 1]
                            codigo[j + 1] <- auxCadena
                            auxCadena <- fecha[j]
                            fecha[j] <- fecha[j + 1]
                            fecha[j + 1] <- auxCadena
                            auxCadena <- dni[j]
                            dni[j] <- dni[j + 1]
                            dni[j + 1] <- auxCadena
                            auxCadena <- telefono[j]
                            telefono[j] <- telefono[j + 1]
                            telefono[j + 1] <- auxCadena
                            auxCadena <- enfermedades[j]
                            enfermedades[j] <- enfermedades[j + 1]
                            enfermedades[j + 1] <- auxCadena
                            auxCadena <- dolores[j]
                            dolores[j] <- dolores[j + 1]
                            dolores[j + 1] <- auxCadena
                            auxCadena <- diagnosticos[j]
                            diagnosticos[j] <- diagnosticos[j + 1]
                            diagnosticos[j + 1] <- auxCadena
                            auxCadena <- observaciones[j]
                            observaciones[j] <- observaciones[j + 1]
                            observaciones[j + 1] <- auxCadena
							
                            edadAux <- edadP[j]
                            edadP[j] <- edadP[j + 1]
                            edadP[j + 1] <- edadAux
                            auxReal <- peso[j]
                            peso[j] <- peso[j + 1]
                            peso[j + 1] <- auxReal
                            auxReal <- talla[j]
                            talla[j] <- talla[j + 1]
                            talla[j + 1] <- auxReal
                            edadAux <- terapiasP[j]
                            terapiasP[j] <- terapiasP[j + 1]
                            terapiasP[j + 1] <- edadAux
                            auxReal <- costos[j]
                            costos[j] <- costos[j + 1]
                            costos[j + 1] <- auxReal
                        FinSi
                    FinPara
                FinPara
                Escribir "Fichas ordenadas alfabeticamente:"
                Para i <- 1 Hasta n Hacer
                    Escribir i, ". ", nombre[i], " | DNI: ", dni[i], " | Fecha: ", fecha[i], " | Total: S/ ", costos[i]
                FinPara
				
            4:
                // ordenamiento por seleccion del costo mas alto al mas bajo
                Para i <- 1 Hasta n - 1 Hacer
                    pos <- i
                    Para j <- i + 1 Hasta n Hacer
                        Si costos[j] > costos[pos] Entonces
                            pos <- j
                        FinSi
                    FinPara
                    Si pos <> i Entonces
                        auxReal <- costos[i]
                        costos[i] <- costos[pos]
                        costos[pos] <- auxReal
						
                        auxCadena <- nombre[i]
                        nombre[i] <- nombre[pos]
                        nombre[pos] <- auxCadena
                        auxCadena <- codigo[i]
                        codigo[i] <- codigo[pos]
                        codigo[pos] <- auxCadena
                        auxCadena <- fecha[i]
                        fecha[i] <- fecha[pos]
                        fecha[pos] <- auxCadena
                        auxCadena <- dni[i]
                        dni[i] <- dni[pos]
                        dni[pos] <- auxCadena
                        auxCadena <- telefono[i]
                        telefono[i] <- telefono[pos]
                        telefono[pos] <- auxCadena
                        auxCadena <- enfermedades[i]
                        enfermedades[i] <- enfermedades[pos]
                        enfermedades[pos] <- auxCadena
                        auxCadena <- dolores[i]
                        dolores[i] <- dolores[pos]
                        dolores[pos] <- auxCadena
                        auxCadena <- diagnosticos[i]
                        diagnosticos[i] <- diagnosticos[pos]
                        diagnosticos[pos] <- auxCadena
                        auxCadena <- observaciones[i]
                        observaciones[i] <- observaciones[pos]
                        observaciones[pos] <- auxCadena
						
                        edadAux <- edadP[i]
                        edadP[i] <- edadP[pos]
                        edadP[pos] <- edadAux
                        auxReal <- peso[i]
                        peso[i] <- peso[pos]
                        peso[pos] <- auxReal
                        auxReal <- talla[i]
                        talla[i] <- talla[pos]
                        talla[pos] <- auxReal
                        edadAux <- terapiasP[i]
                        terapiasP[i] <- terapiasP[pos]
                        terapiasP[pos] <- edadAux
                    FinSi
                FinPara
                Escribir "Fichas ordenadas de mayor a menor costo:"
                Para i <- 1 Hasta n Hacer
                    Escribir i, ". S/ ", costos[i], " | ", terapiasP[i], " terapias | ", nombre[i], " | Fecha: ", fecha[i]
                FinPara
				
            5:
                // recorrido de fichas y acumulacion de los ingresos registrados
                recaudacion <- 0
                Escribir "LISTADO GENERAL DE FICHAS CLINICAS"
                Para i <- 1 Hasta n Hacer
                    recaudacion <- recaudacion + costos[i]
                    Escribir "-----------------------------------------"
                    Escribir i, ". Codigo: ", codigo[i], " | Fecha: ", fecha[i]
                    Escribir "DNI: ", dni[i], " | Paciente: ", nombre[i]
                    Escribir "Enfermedad: ", enfermedades[i], " | Dolor: ", dolores[i]
                    Escribir "Diagnostico: ", diagnosticos[i]
                    Escribir "Terapias: ", terapiasP[i], " | Total: S/ ", costos[i]
                FinPara
                Escribir "TOTAL DE PACIENTES: ", n
                Escribir "INGRESO TOTAL ACUMULADO: S/ ", recaudacion
				
            0:
                // finalizacion del ciclo principal del sistema
                Escribir "Cerrando sistema del Centro Quiropractico Axis. Hasta luego."
            De Otro Modo:
                Escribir "Opcion no valida. Ingresa un numero del 0 al 5."
        FinSegun
    FinMientras
FinAlgoritmo