import radar
import medio
import blanco
import generador
import datetime
import detector


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 0
    frecuencia = math.pi / 8

    #TODO construir un nuevo genrador de senales
    #Done
    un_generador = generador.Generador(amplitud, fase, frecuencia)

    #TODO construir un detector
    #Done
    un_detector = detector.Detector()

    #TODO construir un nuevo radar
    #Done
    un_radar = radar.Radar(un_generador, un_detector)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)

    #TODO contruir un nuevo blanco
    un_blanco = blanco.Blanco(amplitud_de_frecuencia_del_blanco, \
    tiempo_inicial_del_blanco, tiempo_final_del_blanco )

    #TODO contruir un medio
    un_medio = medio.Medio(un_blanco)

    #TODO construir un radar
    un_radar = radar.Radar(un_generador, un_detector)

    #detectar
    detecto = un_radar.detectar(un_medio, tiempo_inicial, tiempo_final)

    if detecto:
        print "El radar detecto un blanco!"
    else:
        print "El rada no detecto nada!"

if __name__ == "__main__":
    main()
